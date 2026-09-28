import csv

def display_patients():
    with open("patients.csv", "r") as file:
        reader = csv.DictReader(file)

        for patient in reader:
            print(patient)

def search_patient(patient_id):
    with open("patients.csv", "r") as file:
        reader = csv.DictReader(file)

        for patient in reader:
            if patient["Patient ID"] == patient_id:
                print("Patient Found:")
                print(patient)
                return

        print("Patient not found")

display_patients()

pid = input("Enter Patient ID to search: ")
search_patient(pid)
