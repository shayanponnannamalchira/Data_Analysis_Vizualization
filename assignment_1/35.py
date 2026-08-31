"""
Q35. Hospital Patient Data Analyzer
A hospital maintains the following patient information:
Patient ID
Patient name
Age
Disease
Develop a Python program using appropriate data structures to:
Store patient records.
Display patients above 60 years.
Count the number of patients with a particular disease.
Display unique diseases using a set.
Search for a patient using their ID.

Topics: Dictionaries + Lists + Sets + Loops + Conditions.
"""

patients = [
    {"id": 1, "name": "Amit", "age": 45, "disease": "Diabetes"},
    {"id": 2, "name": "Ravi", "age": 67, "disease": "Hypertension"},
    {"id": 3, "name": "Priya", "age": 72, "disease": "Diabetes"},
    {"id": 4, "name": "John", "age": 34, "disease": "Asthma"},
    {"id": 5, "name": "Kiran", "age": 61, "disease": "Hypertension"},
    {"id": 6, "name": "Anita", "age": 29, "disease": "Asthma"},
]

# Display patients above 60 years
print("Patients above 60 years:")
for patient in patients:
    if patient["age"] > 60:
        print(f"ID: {patient['id']}, Name: {patient['name']}, "
              f"Age: {patient['age']}, Disease: {patient['disease']}")

# Count the number of patients with a particular disease
disease_to_search = "Diabetes"
disease_count = 0
for patient in patients:
    if patient["disease"] == disease_to_search:
        disease_count += 1
print(f"\nNumber of patients with {disease_to_search}: {disease_count}")

# Display unique diseases using a set
unique_diseases = set()
for patient in patients:
    unique_diseases.add(patient["disease"])
print("\nUnique diseases in the hospital:", unique_diseases)


def search_patient_by_id(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


search_id = 3
result = search_patient_by_id(search_id)
if result:
    print(f"\nPatient found with ID {search_id}: {result}")
else:
    print(f"\nNo patient found with ID {search_id}")
