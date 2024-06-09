# ECG-APP

## Description
The ECG-APP is a Streamlit-based application designed to analyze and display electrocardiogram (ECG) data. It allows users to load and view ECG data for specific individuals, select specific ECG tests, and analyze the data to find peaks and estimate the heart rate. The application also provides visualizations of the ECG data with identified peaks.
This is the 4th small assignement of the programming exercise 2.

## Requirements
- Python 3.7 or higher
- Streamlit
- Pandas
- Scipy
- Numpy
- Plotly

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ECG-App.git
    cd ECG-App
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure the `person_db.json` file is located in `../EKG_App/data/`.

2. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

3. The application will open in your default web browser. Follow these steps to use the app:
    - Enter the ID of the person whose ECG data you want to view.
    - The app will display the person's details including their first name, last name, and date of birth.
    - Select an ECG test from the list provided.
    - The app will analyze the selected ECG test, find peaks, and estimate the heart rate.
    - The ECG data along with the identified peaks will be visualized.

## Project Structure
- `main.py`: The main script that runs the Streamlit application.
- `ecgdata.py`: Contains the `EKGdata` class for handling ECG data operations.
- `classes.py`: Contains the `Person` class for handling person data operations.
- `data/`: Directory where the `person_db.json` file should be placed.

## Functions
### main.py
- **`st.title("ECG-APP")`**: Sets the title of the Streamlit application.
- **`st.write("### ECG Data")`**: Writes a subheader for the ECG data section.
- **`Person.load_person_data()`**: Loads person data from the JSON file.
- **`Person.get_person_list(persons)`**: Retrieves a list of person names.
- **`Person.find_person_data_by_id(person_id)`**: Finds and returns person data by ID.
- **`EKGdata.load_by_id(user_name.id)`**: Loads ECG data for a specific user ID.
- **`EKGdata.find_peaks(link)`**: Finds peaks in the ECG data.
- **`EKGdata.estimate_hr(peaks)`**: Estimates the heart rate from the peaks.
- **`EKGdata.plot_time_series(link, peaks)`**: Plots the ECG time series data and highlights peaks.

### classes.py
- **`Person.load_person_data()`**: Loads the person database from a JSON file.
- **`Person.get_person_list(person_data)`**: Returns a list of all person names from the person data.
- **`Person.find_person_data_by_id(suchstring)`**: Finds and returns person data by ID.
- **`__init__(self, person_dict)`**: Initializes a `Person` object with data from a dictionary.

### ecgdata.py
- **`EKGdata.__init__(self, ekg_dict)`**: Initializes an `EKGdata` object with data from a dictionary.
- **`EKGdata.load_by_id(suchstring)`**: Loads ECG data for a specific user ID.
- **`EKGdata.read_ecg_data(ecg_path)`**: Reads ECG data from a file.
- **`EKGdata.find_peaks(path)`**: Finds peaks in the ECG data.
- **`EKGdata.estimate_hr(peaks)`**: Estimates the heart rate from the peaks.
- **`EKGdata.plot_time_series(path, peaks)`**: Plots the ECG time series data and highlights peaks.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Scipy](https://www.scipy.org/)
- [Numpy](https://numpy.org/)
- [Plotly](https://plotly.com/)
