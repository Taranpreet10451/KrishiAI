# KrishiAI

**KrishiAI** is a Machine Learning–based project that predicts whether a soil sample is **fertile or not**.  
This repository focuses on the **model development and data analysis** part of a larger **IoT + AI** system aimed at enhancing agricultural productivity through intelligent soil assessment.

---

## Project Overview

- Built a **Soil Quality Classifier** using supervised machine learning.
- Performed **data preprocessing, training, and evaluation** within a Jupyter Notebook.
- Generated an **automated YData Profiling report** for exploratory data analysis.
- Serialized the trained model using **Pickle** for reuse in real-time prediction systems.

---

## Technologies Used

- **Python**
- **Scikit-learn**
- **Pandas**, **NumPy**
- **YData Profiling**
- **Pickle**

---

## Repository Structure
```
KrishiAI/
│
├── Datasets/  Training and testing data .csv files
├── final.ipynb  Model building and analysis notebook
├── Soil_Quality_Classifier  It uses a saved model to translate raw soil data into a simple fertility label
├── random_forest_pkl.pkl  Pre-trained ML model
├── Soil_Analysis_Report.html  YData profiling report
```

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Taranpreet10451/KrishiAI.git
   cd KrishiAI
2. **Install Dependencies**
   ```bash
   pip install pandas numpy scikit-learn ydata-profiling
3. **Open the Juoyteer Notebook**
   ```bash
   jupyter notebook Soil_quality_Classifier.ipynb
4. **(Optional) View the profilling report**
  - Open Soil_Analysis_Report.html in your browser.

---

## Results
- The trained model successfully classifies soil samples as fertile or not fertile based on input features.
- YData Profiling helped in identifying key correlations and ensuring dataset quality before model training.

---

## Author
- Taranpreet Kaur
- B.Tech in Computer Engineering

---

## License
- Released under the MIT License
