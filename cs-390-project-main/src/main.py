"""Main file to run blockchain and smart contracts."""

# Code adapted from these examples.
# reference: https://towardsdatascience.com/building-a-minimal-blockchain-in-python-4f2e9934101d
# reference: https://github.com/edenau/minimal-blockchain/blob/master/main.ipynb

import copy, datetime, hashlib, json, ecdsa


class PatientBlock:
    def __init__(
        self,
        index,
        time,
        public_key,
        conditions,
        medications,
        appointments,
        insurance_provider,
        sharing_settings,
        prev_hash,
    ):
        """Initialize and construct the aspects of the object of type block."""
        self.index = index
        self.time = time
        self.public_key = public_key
        self.conditions = conditions
        self.medications = medications
        self.appointments = appointments
        self.insurance_provider = insurance_provider
        self.sharing_settings = sharing_settings
        self.previous_hash = prev_hash
        self.hash = self.hashing()

    def hashing(self):
        """Generate the hash of a block using sha256 (utf-8)."""
        key = hashlib.sha256()
        key.update(str(self.index).encode("utf-8"))
        key.update(str(self.time).encode("utf-8"))
        key.update(str(self.public_key).encode("utf-8"))
        key.update(str(self.conditions).encode("utf-8"))
        key.update(str(self.medications).encode("utf-8"))
        key.update(str(self.appointments).encode("utf-8"))
        key.update(str(self.insurance_provider).encode("utf-8"))
        key.update(str(self.sharing_settings).encode("utf-8"))
        key.update(str(self.previous_hash).encode("utf-8"))
        return key.hexdigest()


class PatientChain:
    def __init__(self):  # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]

    def get_genesis_block(self):
        return PatientBlock(
            0,
            datetime.datetime.utcnow(),
            "Genesis",
            "arbitrary",
            "arbitrary",
            "arbitrary",
            "arbitrary",
            "arbitrary",
            "arbitrary",
        )

    def add_block(
        self,
        index,
        public_key,
        conditions,
        medications,
        appointments,
        insurance_provider,
        sharing_settings,
    ):
        self.blocks.append(
            PatientBlock(
                index + 1,
                datetime.datetime.utcnow(),
                public_key,
                conditions,
                medications,
                appointments,
                insurance_provider,
                sharing_settings,
                self.blocks[len(self.blocks) - 1].hash,
            )
        )

    def get_chain_size(self):  # exclude genesis block
        return len(self.blocks) - 1

    def verify(self, verbose=True):
        flag = True
        for i in range(1, len(self.blocks)):
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print(f"Wrong block index at block {i}.")
            if self.blocks[i - 1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print(f"Wrong previous hash at block {i}.")
            if self.blocks[i].hash != self.blocks[i].hashing():
                flag = False
                if verbose:
                    print(f"Wrong hash at block {i}.")
            if self.blocks[i - 1].time >= self.blocks[i].time:
                flag = False
                if verbose:
                    print(f"Backdating at block {i}.")
        return flag

    def fork(self, head="latest"):
        if head in ["latest", "whole", "all"]:
            return copy.deepcopy(self)  # deepcopy since they are mutable
        else:
            c = copy.deepcopy(self)
            c.blocks = c.blocks[0 : head + 1]
            return c


class smart_contract:
    """Class to create, store, and execute a smart contract."""

    def __init__(
        self,
        patient_block_number,
        permission,
        user_type,
        person_to_share_from,
        person_to_share_to,
        auth_family_member,
        sharing_code,
    ):
        """Function to initialize a smart contract object."""
        self.patient_block_number = patient_block_number
        self.permission = permission
        self.user_type = user_type
        self.person_to_share_from = person_to_share_from
        self.person_to_share_to = person_to_share_to
        self.auth_family_member = auth_family_member
        self.sharing_code = sharing_code

    def share_patient_data(
        self,
        obj,
        patient_block_number,
        permission,
        user_type,
        person_to_share_from,
        person_to_share_to,
        auth_family_member,
        sharing_code,
    ):
        """Function to share patient information only if it meets a set of criteria."""
        contract_successful = False
        # If sharing is enabled by the patient perform the appropriate sharing techniques by the type of person that is accessing the data.
        if bool(permission):
            # Case: Giving data to the patient.
            if int(user_type) == 0:
                if person_to_share_from == person_to_share_to:
                    code = input("Enter your Sharing Code\n")
                    if int(code) == sharing_code:
                        print(
                            f"Contract criteria met, sharing information about {person_to_share_from} at block {patient_block_number}...\n"
                        )
                        print("Block ", patient_block_number)
                        print("Timestamp ", obj.blocks[patient_block_number].time)
                        print("Index ", obj.blocks[patient_block_number].index)
                        print(
                            "Public Key ", obj.blocks[patient_block_number].public_key
                        )
                        print("Condition ", obj.blocks[patient_block_number].conditions)
                        print(
                            "Medications ", obj.blocks[patient_block_number].medications
                        )
                        print(
                            "Appointments ",
                            obj.blocks[patient_block_number].appointments,
                        )
                        print(
                            "Insurance Provider ",
                            obj.blocks[patient_block_number].insurance_provider,
                        )
                        print(
                            "Sharing Settings ",
                            obj.blocks[patient_block_number].sharing_settings,
                        )
                        print("Hash ", obj.blocks[patient_block_number].hash)
                        contract_successful = True
                    else:
                        print("Code not authorized.")

            # Case: Sharing information to a doctor
            elif int(user_type) == 1:
                if "Dr." in person_to_share_to:
                    print("Doctor Authenticated.\n")
                    code = input("Enter your Sharing Code\n")
                    if int(code) == sharing_code:
                        print(
                            f"Contract criteria met, sharing information about {person_to_share_from} at block {patient_block_number}...\n"
                        )
                        print("Block ", patient_block_number)
                        print("Timestamp ", obj.blocks[patient_block_number].time)
                        print("Index ", obj.blocks[patient_block_number].index)
                        print(
                            "Public Key ", obj.blocks[patient_block_number].public_key
                        )
                        print("Condition ", obj.blocks[patient_block_number].conditions)
                        print(
                            "Medications ", obj.blocks[patient_block_number].medications
                        )
                        print(
                            "Appointments ",
                            obj.blocks[patient_block_number].appointments,
                        )
                        print(
                            "Insurance Provider ",
                            obj.blocks[patient_block_number].insurance_provider,
                        )
                        print(
                            "Sharing Settings ",
                            obj.blocks[patient_block_number].sharing_settings,
                        )
                        print("Hash ", obj.blocks[patient_block_number].hash)
                        contract_successful = True
                    else:
                        print("Sharing Code incorrect.")
                else:
                    print(
                        "Please make sure you indicated you were a doctor at the beginning."
                    )
            # Case: Sharing with A Family Member of patient
            elif int(user_type) == 2:
                print("Validating Name")
                if person_to_share_to == auth_family_member:
                    print("Name Validated")
                    code = input("Enter Your Sharing Code.\n")
                    if int(code) == sharing_code:
                        print(
                            f"Contract criteria met, sharing information about {person_to_share_from} at block {patient_block_number}...\n"
                        )
                        print("Block ", patient_block_number)
                        print("Timestamp ", obj.blocks[patient_block_number].time)
                        print("Index ", obj.blocks[patient_block_number].index)
                        print(
                            "Public Key ", obj.blocks[patient_block_number].public_key
                        )
                        print("Condition ", obj.blocks[patient_block_number].conditions)
                        print(
                            "Medications ", obj.blocks[patient_block_number].medications
                        )
                        print(
                            "Appointments ",
                            obj.blocks[patient_block_number].appointments,
                        )
                        print(
                            "Insurance Provider: ",
                            obj.blocks[patient_block_number].insurance_provider,
                        )
                        print(
                            "Sharing Settings: ",
                            obj.blocks[patient_block_number].sharing_settings,
                        )
                        print("Hash: ", obj.blocks[patient_block_number].hash)
                        contract_successful = True
                    else:
                        print("Family Member or Share Code Does Not Match Records.")
                else:
                    print(
                        "Your name doesn't match the authorized family member records."
                    )
            # Case: Sharing with an insurance provider
            elif int(user_type) == 3:
                # If the person to share to matches the insurance on file share the information with the insurer.
                if (
                    person_to_share_to
                    == obj.blocks[int(patient_block_number)].insurance_provider
                ):
                    print("Insurance Recognized")
                    code = input("Enter The Sharing Code.\n")
                    # If the code is authorized share the information.
                    if int(code) == sharing_code:
                        print(
                            f"Contract criteria met, sharing information about {person_to_share_from} at block {patient_block_number}...\n"
                        )
                        print("Block ", patient_block_number)
                        print("Timestamp ", obj.blocks[patient_block_number].time)
                        print("Index ", obj.blocks[patient_block_number].index)
                        print(
                            "Public Key: ", obj.blocks[patient_block_number].public_key
                        )
                        print(
                            "Condition: ", obj.blocks[patient_block_number].conditions
                        )
                        print(
                            "Medications: ",
                            obj.blocks[patient_block_number].medications,
                        )
                        print(
                            "Appointments: ",
                            obj.blocks[patient_block_number].appointments,
                        )
                        print(
                            "Insurance Provider: ",
                            obj.blocks[patient_block_number].insurance_provider,
                        )
                        print(
                            "Sharing Settings: ",
                            obj.blocks[patient_block_number].sharing_settings,
                        )
                        print("Hash: ", obj.blocks[patient_block_number].hash)
                        contract_successful = True

        # Case: Sharing not enabled, don't run any share checking processes.
        else:
            print(
                "Contract criteria not met.\nTry again when all criteria meet the mark for sharing\n"
            )
        return contract_successful


# Run the main processes of this program to run a patient blockchain and start a smart contract.
if __name__ == "__main__":
    # Save the user's name and user type
    name = input("What is your name?\n")
    user_type = input(
        f"Welcome {name}! Who are you?\n0 - Patient\n1 - Doctor\n2 - Family Member of patient\n3 - Insurance Provider\n"
    )

    # If the user indicated they were a doctor add the "dr." prefix to their name
    if int(user_type) == 1:
        name = "Dr. " + name

    # Generate a public and private key for the user.
    print("Generating your unique Public and Private Keys...\n")
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key().to_string().hex()
    print(
        f"{name}, here are your public and private keys.\nPublic Key: {public_key}\nPrivate Key: {private_key.to_string().hex()}\n"
    )

    # Read and save data from data.json file.
    with open("data.json", "r") as f:
        json_data_file = json.load(f)

    # Create a patientchain object.
    c = PatientChain()

    # Generate a public and private key for each patient record and add each series of information to the ledger.
    for counter, record in enumerate(json_data_file):
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        public_key = private_key.get_verifying_key().to_string().hex()
        c.add_block(
            counter,
            public_key,
            record["Condition"],
            record["Medications"],
            record["Appointments"],
            record["Insurance"],
            record["Sharing Settings"],
        )

    # Verify the contents of the blockchain.
    verification_result = PatientChain.verify(c)
    if verification_result == True:
        print("Blockchain Verified.")
    else:
        print("Blockchain not verified.")

    # Always repeat the prompt and processes for running the main commands unless indicated otherwise from the user.
    is_running = True

    while is_running:
        # Capture the users decision about what command needs to be run.
        choice = input(
            "\nWhat would you like to do?\n0 - Output One Block\n1 - Output All Blocks\n2 - Add A New Block\n3 - Create A Smart Contract\nPress Any Other Number To Exit\n"
        )

        # Case: Decision to output a particular block in a blockchain.
        if int(choice) == 0:
            block_to_access = input("What block would you like to access?\n")
            # Only output block info if inputted block number exists in the blockchain.
            if int(block_to_access) <= PatientChain.get_chain_size(c):
                print("\nBlock ", block_to_access)
                print("Timestamp ", c.blocks[int(block_to_access)].time)
                print("Index ", c.blocks[int(block_to_access)].index)
                print("Public Key ", c.blocks[int(block_to_access)].public_key)
                print("Condition ", c.blocks[int(block_to_access)].conditions)
                print("Medications ", c.blocks[int(block_to_access)].medications)
                print("Appointments ", c.blocks[int(block_to_access)].appointments)
                print(
                    "Insurance Provider ",
                    c.blocks[int(block_to_access)].insurance_provider,
                )
                print(
                    "Sharing Settings ", c.blocks[int(block_to_access)].sharing_settings
                )
                print("Hash ", c.blocks[int(block_to_access)].hash)
            # If the inputted block number does not exist output an error message.
            else:
                print(
                    f"ERROR: You tried to access a block that doesn't exist.\nTry an index within the values of 1 and {PatientChain.get_chain_size(c)}.\n"
                )

        # Case: Decision to output all blocks in the blockchain.
        elif int(choice) == 1:
            length = PatientChain.get_chain_size(c)
            for block in range(1, length + 1):
                print("Block ", block)
                print("Timestamp ", c.blocks[block].time)
                print("Index ", c.blocks[block].index)
                print("Public Key ", c.blocks[block].public_key)
                print("Condition ", c.blocks[block].conditions)
                print("Medications ", c.blocks[block].medications)
                print("Appointments ", c.blocks[block].appointments)
                print("Insurance Provider ", c.blocks[block].insurance_provider)
                print("Sharing Settings ", c.blocks[block].sharing_settings)
                print("Hash ", c.blocks[block].hash)
                print()

        # Case: Decision to add a block to the blockchain.
        elif int(choice) == 2:
            # Collect information about the blocks that need to be added.
            condition = input("Enter a condition.\n")
            medication = input("Enter a medication.\n")
            appointments = input("Enter an appointment.\n")
            insurance = input("Enter an insurance provider.\n")
            sharing = input("Enter your sharing settings.\n")

            # Generate a private and public key and append new block to the ledger.
            private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
            public_key = private_key.get_verifying_key().to_string().hex()
            c.add_block(
                counter,
                public_key,
                condition,
                medication,
                appointments,
                insurance,
                sharing,
            )

            print("Block added!")

            # Output the newly generated block at the appropriate blockchain index.
            index = PatientChain.get_chain_size(c) + 1
            print("Block ", index)
            print("Timestamp ", c.blocks[index].time)
            print("Index ", c.blocks[index].index)
            print("Public Key ", c.blocks[index].public_key)
            print("Condition ", c.blocks[index].conditions)
            print("Medications ", c.blocks[index].medications)
            print("Appointments ", c.blocks[index].appointments)
            print("Insurance Provider ", c.blocks[index].insurance_provider)
            print("Sharing Settings ", c.blocks[index].sharing_settings)
            print("Hash ", c.blocks[index].hash)

            # Verify the blockchain once a new block has been added.
            PatientChain.verify(c)
            print("Blockchain Verified!\n")

        # Case: Decision to create a smart contract
        elif int(choice) == 3:
            # Obtain the patient block with which to start a smart contract.
            patient_block = input(
                "Enter the patient block to create a sharing contract with.\n"
            )

            # Gather information about the selected patient block from the json file.
            for counter, record in enumerate(json_data_file):
                if counter == int(patient_block) - 1:
                    patient_to_share_from = record["Name"]
                    auth_family_member = record["Authorized Family Members"]
                    sharing_code = record["Sharing Code"]

            # Create a smart contract passing the index of the patient block, sharing settings, username, authorized family member names, and sharing code.
            new_smart_contract = smart_contract(
                int(patient_block),
                c.blocks[int(patient_block)].sharing_settings,
                user_type,
                patient_to_share_from,
                name,
                auth_family_member,
                sharing_code,
            )

            print(
                f"Starting a data sharing contract between {name} and {patient_to_share_from}.\n"
            )

            # Run the smart contract.
            contract_successful = smart_contract.share_patient_data(
                new_smart_contract,
                c,
                int(patient_block),
                c.blocks[int(patient_block)].sharing_settings,
                user_type,
                patient_to_share_from,
                name,
                auth_family_member,
                sharing_code,
            )
        # Case: Decision not recognized.
        else:
            print("Exiting...\n")
            is_running = False
