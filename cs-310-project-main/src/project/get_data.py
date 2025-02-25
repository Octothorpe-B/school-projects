"""Gets data from the internet to answer questions."""

import json
import us
import urllib.request as request


def get_json_data():
    """Returns all of the statistics about the coronavirus in the United States."""
    with request.urlopen(
        "https://covidtracking.com/api/v1/states/current.json"
    ) as response:
        source = response.read()
        data_dict = json.loads(source)

    # for data in data_dict:
    # print(
    # data["state"], data["positive"], data["negative"], data["totalTestResults"]
    # )

    return data_dict


def get_positive_test_results_data(state, data):
    """With a state input variable it returns the positive test results from a specific state."""
    data_list = data

    for i in data_list:
        if i["state"] == state:
            return i["positive"]


def get_negative_test_results_data(state, data):
    """Using an inputted state it gets the amount of negative tests results in a specific state."""
    data_list = data

    for i in data_list:
        if i["state"] == state:
            return i["negative"]


def get_total_tested_data(state, data):
    """Takes an inputted state and gets the total amount of tested people in a specific state."""
    data_list = data

    for i in data_list:
        if i["state"] == state:
            return i["totalTestResults"]


def get_number_on_ventilator(state, data):
    """Takes an inputted state and gets the total amount of people on a ventilator."""
    data_list = data
    for i in data_list:
        if i["state"] == state:
            return i["onVentilatorCurrently"]


def get_number_in_intensive_care(state, data):
    """Takes an inputted state and gets the total amount of people in intensive care in a specific state."""
    data_list = data

    for i in data_list:
        if i["state"] == state:
            return i["inIcuCurrently"]


def get_total_recovered_data(state, data):
    """Takes an inputted state and gets the total amount of recovered people in a specific state."""
    data_list = data

    for i in data_list:
        if i["state"] == state:
            return i["recovered"]


def get_total_death_data(state, data):
    """Takes an inputted state and gets the total amount of deaths in a specific state."""
    data_list = data

    for i in data_list:
        if i["state"] == state:
            return i["death"]
