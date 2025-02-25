"""Recognize speaking from a audio clip."""

from google.cloud import speech_v1p1beta1
from google.cloud import texttospeech_v1
from google.cloud.speech_v1p1beta1 import enums
from google.cloud import storage
from google.cloud import texttospeech
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
import us
import get_data


def setup():
    """Ensures that credentials are used in API requests."""

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print("Credentials verified.")
    print(buckets)


def record_input_audio_file(requested_time):
    """Records audio from a microphone and saves it."""
    sample_rate = 44100
    seconds = requested_time

    print("I'm listening.")
    recording = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    print("I'll answer your question.")
    write("recordings/audio_output.wav", sample_rate, recording)


def upload_audio(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    # print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))
    print("Thinking...")


def speech_to_text(audio_file):
    """Translate speech from an audio file to text."""

    client = speech_v1p1beta1.SpeechClient()

    # The language of the supplied audio
    american_english_language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.MP3
    config = {
        "language_code": american_english_language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    audio = {"uri": audio_file}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Question: {}".format(alternative.transcript))
        # print(u"Diagnostics: ", response)

    return format(alternative.transcript)


def text_to_speech(text):
    """Synthesizes speech from the input string of text."""

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
    )

    audio_configuration = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input_text, voice, audio_configuration)

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        # print('Saved to "output.mp3"')


def answer_question(message):
    """Answer questions from the user related to the coronavirus."""

    if "what" and "weather" in message:
        answer = "It's going to be rainy tomorrow, with light winds. Slight chance of raining cats and dogs."

    if "what" "do" "carrots" and "parsnips" in message:
        answer = (
            "You need to save them all, hide them around the house if you need to! Roasted"
            "carrots are extremely delicious, especially with sauteeed parsnips. I hear"
            "from my secret sources that grandparents love eating them every night for dinner. Go ahead and"
            "remove the apple pie, ice cream, and cake to make more room for the vegetables."
        )

    if "a" in message:
        united_states = [
            "Alaska",
            "Alabama",
            "Arkansas",
            "American Samoa",
            "Arizona",
            "California",
            "Colorado",
            "Connecticut",
            "District of Columbia",
            "Delaware",
            "Florida",
            "Georgia",
            "Guam",
            "Hawaii",
            "Iowa",
            "Idaho",
            "Illinois",
            "Indiana",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Massachusetts",
            "Maryland",
            "Maine",
            "Michigan",
            "Minnesota",
            "Missouri",
            "Mississippi",
            "Montana",
            "North Carolina",
            "North Dakota",
            "Nebraska",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "Nevada",
            "New York",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Puerto Rico",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Virginia",
            "Virgin Islands",
            "Vermont",
            "Washington",
            "Wisconsin",
            "West Virginia",
            "Wyoming",
        ]

        c = 0

        # Find what state was asked for in the question and find the associated data.
        for states in united_states:
            if united_states[c] in message:
                s = united_states[c]
                state = us.states.lookup(united_states[c])
                abb = state.abbr
                pull_data = get_data.get_json_data()

                if "positive" and "test" and "results" in message:
                    positive_tested = get_data.get_positive_test_results_data(
                        abb, pull_data
                    )
                    output = (
                        "In the state of %s, the number of positive test results are %s."
                        % (s, positive_tested)
                    )
                    return output

                if "negative" and "test" and "results" in message:
                    negative_tested = get_data.get_negative_test_results_data(
                        abb, pull_data
                    )
                    output = (
                        "In the state of %s, the number of negative test results are %s."
                        % (s, negative_tested)
                    )
                    return output

                if "total" and "number" and "tested" in message:
                    total_tested = get_data.get_total_tested_data(abb, pull_data)
                    output = "In the state of %s, the total number of tests are %s." % (
                        s,
                        total_tested,
                    )
                    return output

                if "what" and "number" and "ventilator" in message:
                    number_on_ventilator = get_data.get_number_on_ventilator(
                        abb, pull_data
                    )
                    output = (
                        "In the state of %s, the total number of people on a ventilator is %s."
                        % (s, number_on_ventilator,)
                    )
                    return output

                if "what" and "number of" and "recovered" in message:
                    recovered = get_data.get_total_recovered_data(abb, pull_data)
                    output = (
                        "In the state of %s, the total number of recovered people is %s."
                        % (s, recovered,)
                    )
                    return output

                if "what" and "number of" and "deaths" in message:
                    deaths = get_data.get_total_death_data(abb, pull_data)
                    output = (
                        "In the state of %s, the total number of deaths are %s."
                        % (s, deaths,)
                    )
                    return output

                if "all" and "statistics" in message:
                    positive_tested = get_data.get_positive_test_results_data(
                        abb, pull_data
                    )
                    negative_tested = get_data.get_negative_test_results_data(
                        abb, pull_data
                    )
                    total_tested = get_data.get_total_tested_data(abb, pull_data)
                    number_on_ventilator = get_data.get_number_on_ventilator(
                        abb, pull_data
                    )
                    recovered = get_data.get_total_recovered_data(abb, pull_data)
                    deaths = get_data.get_total_death_data(abb, pull_data)

                    output = (
                        "In the state of %s, the number of positive test results are %s, the number "
                        "of negative test results are %s, and the total number of all tests are %s. "
                        "The number of people on a ventilator is currently %s. The amount of recovered "
                        "people is %s and the number of deaths is currently %s."
                        % (
                            s,
                            positive_tested,
                            negative_tested,
                            total_tested,
                            number_on_ventilator,
                            recovered,
                            deaths,
                        )
                    )

                    return output
            c = c + 1


if __name__ == "__main__":
    # Audio files directories and settings to transcribe the audio file.
    CLOUD_AUDIO_FILE = "gs://bucket_audio_storage/audio_upload.wav"
    user_question = "recordings/audio_output.wav"
    bucket_name = "bucket_audio_storage"
    uploaded_file = "audio_upload.wav"
    recording_time = 6

    # Run the programs functions, output the answer in text and audio.
    setup()
    record_input_audio_file(recording_time)
    upload_audio(bucket_name, user_question, uploaded_file)
    message = speech_to_text(CLOUD_AUDIO_FILE)
    answer = answer_question(message)
    text_to_speech(answer)
    print("Answer: ", answer)
    playsound("output.mp3")
