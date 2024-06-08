import json
import pandas as pd
from ecgdata import EKGdata
from classes import Person

"""print("This is a module with some functions to read the person data")
persons = Person.load_person_data()
person_names = Person.get_person_list(persons)

print("Welcome to Personfinder")
person_id = int(input("Enter ID of Persson: "))
Name = input("Name of Person: ")
person_dict = Person.find_person_data_by_id(person_id)
user_name = person_dict["firstname"]
user_name = Person(person_dict)
print(user_name.date_of_birth)"""


print("This is a module with some functions to read the EKG data")

id = int(input("ID des EKG: "))

ekg = EKGdata.load_by_id(id)
print(ekg)
peaks  = EKGdata.find_peaks(ekg['result_link'])
hr_mean = EKGdata.estimate_hr(peaks)
print(hr_mean)

EKGdata.plot_time_series(ekg['result_link'])

