class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def category(self):
        if self.treatment_cost >= 50000:
            return "Special"
        else:
            return "General"


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display(self):
        for p in self.patients:
            print("ID:", p.patient_id)
            print("Name:", p.name)
            print("Treatment Cost:", p.treatment_cost)
            print("Category:", p.category())
            print()


h = Hospital()

p1 = Patient(101, "Amit", 30000)
p2 = Patient(102, "Rahul", 75000)

h.add_patient(p1)
h.add_patient(p2)

h.display()
