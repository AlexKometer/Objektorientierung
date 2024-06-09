import streamlit as st
from ecgdata import EKGdata
from classes import Person


st.title("ECG-APP")
st.write("### ECG Data")
ekg_list = []
link_list = []


persons = Person.load_person_data()
person_names = Person.get_person_list(persons)
person_id = st.number_input("Enter ID of Persson: ", min_value=1, max_value=3, value=1, step=1)
person_dict = Person.find_person_data_by_id(person_id)
user_name = person_dict["firstname"]
user_name = Person(person_dict)

st.write(user_name.firstname,user_name.lastname,user_name.date_of_birth)

ekg = EKGdata.load_by_id(user_name.id)


for element in ekg:
    ekg_list.append(element['id'])

selected = st.radio("Select a ECG",options=ekg_list, key="sbECG")

for element in ekg:
    if element['id'] == selected:
        link = element['result_link']
    else:
        print("No EKG found!")

peaks = EKGdata.find_peaks(link)

hr_mean = EKGdata.estimate_hr(peaks)
st.write(hr_mean,"bpm")

EKGdata.plot_time_series(link, peaks)

