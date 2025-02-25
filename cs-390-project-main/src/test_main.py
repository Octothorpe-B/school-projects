"""File to ensure main.py produces the correct outputs."""

import pytest
import ecdsa
import json
import main
import datetime
import unittest


def test_PatientChain():
    """Test to ensure that searching the fields works correctly."""
    # Create a chain object.
    obj = main.PatientChain()

    # Open the json file and save data in json_data_file.
    with open("data.json", "r") as f:
        json_data_file = json.load(f)

    # Add each record into an individual block.
    for counter, record in enumerate(json_data_file):
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        public_key = private_key.get_verifying_key().to_string().hex()
        obj.add_block(
            counter,
            public_key,
            record["Condition"],
            record["Medications"],
            record["Appointments"],
            record["Insurance"],
            record["Sharing Settings"],
        )

    # Determine if the data was placed and in the correct index and placement.
    assert len(str(obj.blocks[1].index)) != 0
    assert len(str(obj.blocks[1].time)) != 0
    assert len(str(obj.blocks[1].public_key)) != 0
    assert len(str(obj.blocks[1].conditions)) != 0
    assert len(str(obj.blocks[1].medications)) != 0
    assert len(str(obj.blocks[1].appointments)) != 0
    assert len(str(obj.blocks[1].insurance_provider)) != 0
    assert len(str(obj.blocks[1].sharing_settings)) != 0

    assert obj.blocks[1].index == 1
    assert obj.blocks[1].conditions == "Peanut Allergy"
    assert obj.blocks[1].medications == "Epinephrine Autoinjector"
    assert obj.blocks[1].appointments == "2/15"
    assert obj.blocks[1].insurance_provider == "USAA"
    assert obj.blocks[1].sharing_settings == "True"


def test_PatientBlock():
    """Test to ensure that the fields in the patientblock works."""
    # Generate public and private keys.
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key().to_string().hex()

    # Create a block object.
    obj = main.PatientBlock(
        1,
        datetime.datetime.utcnow(),
        public_key,
        "Peanut Allergy",
        "Epinephrine Autoinjector",
        "2/15",
        "USAA",
        "True",
        "prev_hash",
    )

    assert len(str(obj.index)) != 0
    assert len(str(obj.time)) != 0
    assert len(str(obj.public_key)) != 0
    assert len(str(obj.conditions)) != 0
    assert len(str(obj.medications)) != 0
    assert len(str(obj.appointments)) != 0
    assert len(str(obj.insurance_provider)) != 0
    assert len(str(obj.sharing_settings)) != 0

    assert obj.index == 1
    assert obj.conditions == "Peanut Allergy"
    assert obj.medications == "Epinephrine Autoinjector"
    assert obj.appointments == "2/15"
    assert obj.insurance_provider == "USAA"
    assert obj.sharing_settings == "True"


class test_smart_contract(unittest.TestCase):
    """Class to test the smart contract feature."""

    def test_patient(self):
        """Function to test if the smart contract is working correctly for a patient accessing data."""
        # Testing the first record in the data file.
        patient_block = 1
        # User type 0 - Patient accessing record.
        user_type = 0
        # Name of the patient.
        name = "Alex"

        # Create a chain object.
        obj = main.PatientChain()

        # Open the json file and save data in json_data_file.
        with open("data.json", "r") as f:
            json_data_file = json.load(f)

        # Add each record into an individual block.
        for counter, record in enumerate(json_data_file):
            private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
            public_key = private_key.get_verifying_key().to_string().hex()
            obj.add_block(
                counter,
                public_key,
                record["Condition"],
                record["Medications"],
                record["Appointments"],
                record["Insurance"],
                record["Sharing Settings"],
            )

        for counter, record in enumerate(json_data_file):
            if counter == int(patient_block) - 1:
                patient_to_share_from = record["Name"]
                auth_family_member = record["Authorized Family Members"]
                sharing_code = record["Sharing Code"]

        main.input = lambda x: "1234"

        # Create a smart contract passing the index of the patient block, sharing settings, username, authorized family member names, and sharing code.
        new_smart_contract = main.smart_contract(
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Run the smart contract.
        contract_successful = main.smart_contract.share_patient_data(
            new_smart_contract,
            obj,
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Ensure that the contract was successful.
        assert contract_successful == True

    def test_doctor(self):
        """Function to test if the smart contract is working correctly for a patient accessing data."""
        # Testing the first record in the data file.
        patient_block = 1
        # User type 1 - Doctor accessing record.
        user_type = 1
        # Name of the doctor.
        name = "Dr. Alex"

        # Create a chain object.
        obj = main.PatientChain()

        # Open the json file and save data in json_data_file.
        with open("data.json", "r") as f:
            json_data_file = json.load(f)

        # Add each record into an individual block.
        for counter, record in enumerate(json_data_file):
            private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
            public_key = private_key.get_verifying_key().to_string().hex()
            obj.add_block(
                counter,
                public_key,
                record["Condition"],
                record["Medications"],
                record["Appointments"],
                record["Insurance"],
                record["Sharing Settings"],
            )

        for counter, record in enumerate(json_data_file):
            if counter == int(patient_block) - 1:
                patient_to_share_from = record["Name"]
                auth_family_member = record["Authorized Family Members"]
                sharing_code = record["Sharing Code"]

        main.input = lambda x: "1234"

        # Create a smart contract passing the index of the patient block, sharing settings, username, authorized family member names, and sharing code.
        new_smart_contract = main.smart_contract(
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Run the smart contract.
        contract_successful = main.smart_contract.share_patient_data(
            new_smart_contract,
            obj,
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Ensure that the contract was successful.
        assert contract_successful == True

    def test_family_member(self):
        """Function to test if the smart contract is working correctly for a patient accessing data."""
        # Testing the first record in the data file.
        patient_block = 1
        # User type 2 - Family member accessing record.
        user_type = 2
        # Name of the family member accessing the record.
        name = "Jordan Byrne"

        # Create a chain object.
        obj = main.PatientChain()

        # Open the json file and save data in json_data_file.
        with open("data.json", "r") as f:
            json_data_file = json.load(f)

        # Add each record into an individual block.
        for counter, record in enumerate(json_data_file):
            private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
            public_key = private_key.get_verifying_key().to_string().hex()
            obj.add_block(
                counter,
                public_key,
                record["Condition"],
                record["Medications"],
                record["Appointments"],
                record["Insurance"],
                record["Sharing Settings"],
            )

        for counter, record in enumerate(json_data_file):
            if counter == int(patient_block) - 1:
                patient_to_share_from = record["Name"]
                auth_family_member = record["Authorized Family Members"]
                sharing_code = record["Sharing Code"]

        main.input = lambda x: "1234"

        # Create a smart contract passing the index of the patient block, sharing settings, username, authorized family member names, and sharing code.
        new_smart_contract = main.smart_contract(
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Run the smart contract.
        contract_successful = main.smart_contract.share_patient_data(
            new_smart_contract,
            obj,
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Ensure that the contract was successful.
        assert contract_successful == True

    def test_insurance_provider(self):
        """Function to test if the smart contract is working correctly for an insurance provider accessing patient data."""
        # Testing the first record in the data file.
        patient_block = 1
        # User type 3 - Insurance provider accessing record.
        user_type = 3
        # Name of the insurance provider.
        name = "USAA"

        # Create a chain object.
        obj = main.PatientChain()

        # Open the json file and save data in json_data_file.
        with open("data.json", "r") as f:
            json_data_file = json.load(f)

        # Add each record into an individual block.
        for counter, record in enumerate(json_data_file):
            private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
            public_key = private_key.get_verifying_key().to_string().hex()
            obj.add_block(
                counter,
                public_key,
                record["Condition"],
                record["Medications"],
                record["Appointments"],
                record["Insurance"],
                record["Sharing Settings"],
            )

        for counter, record in enumerate(json_data_file):
            if counter == int(patient_block) - 1:
                patient_to_share_from = record["Name"]
                auth_family_member = record["Authorized Family Members"]
                sharing_code = record["Sharing Code"]

        main.input = lambda x: "1234"

        # Create a smart contract passing the index of the patient block, sharing settings, username, authorized family member names, and sharing code.
        new_smart_contract = main.smart_contract(
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Run the smart contract.
        contract_successful = main.smart_contract.share_patient_data(
            new_smart_contract,
            obj,
            int(patient_block),
            obj.blocks[int(patient_block)].sharing_settings,
            user_type,
            patient_to_share_from,
            name,
            auth_family_member,
            sharing_code,
        )

        # Ensure that the contract was successful.
        assert contract_successful == True
