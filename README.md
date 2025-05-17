
# KrishiAI

**KrishiAI** is an AI-powered application designed to assist farmers in making informed decisions regarding crop selection and soil fertility. By leveraging machine learning models, it provides recommendations based on soil data to enhance agricultural productivity.

---

## Features

- **Soil Fertility Analysis**: Utilizes machine learning models to assess soil fertility based on input parameters.
- **Crop Recommendation**: Suggests suitable crops for cultivation based on soil characteristics.
- **Data Visualization**: Provides visual insights into soil data for better understanding.

---

## Tech Stack

- **Programming Languages**: Python, HTML
- **Libraries & Frameworks**:
  - Jupyter Notebook
  - Scikit-learn
  - Pandas
  - NumPy
  - Matplotlib
- **Machine Learning Model**: Random Forest Classifier

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Taranpreet10451/KrishiAI.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd KrishiAI
   ```

3. **Create a Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not available, manually install the necessary libraries.*

---

## Usage

1. **Run Jupyter Notebook**:

   ```bash
   jupyter notebook
   ```

2. **Open and Execute Notebooks**:

   - `Soil_Fertility.ipynb`: Analyze soil fertility.
   - `Soil_Quality_ML_serve.ipynb`: Train and evaluate the machine learning model.

3. **Use the Web Interface**:

   - Open `Soil_Data.html` in a web browser to interact with the application's frontend.

---

## Project Structure

```
KrishiAI/
├── Crop_recommendation.csv
├── Raw Data Soil Fertility.csv
├── Soil Fertility Data (Modified Data).csv
├── Soil_Data.html
├── Soil_Fertility.ipynb
├── Soil_Quality_ML_serve.ipynb
├── Untitled.ipynb
├── dataset1.csv
├── main.py
├── random_forest_pkl.pkl
├── sample.py
```

---

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repo and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

