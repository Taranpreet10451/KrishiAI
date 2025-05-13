import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
data = pd.read_csv("C:/Users/Taran/Desktop/KrishiAi/Raw Data Soil Fettility.csv")

# Display dataset information
print("Dataset loaded successfully.")
print("Number of rows:", len(data))
print("Number of columns:", len(data.columns))

# Create a minimal profile report
profile = ProfileReport(
    data,
    minimal=True,  # Simpler report for faster processing
    correlations=None,
    interactions=None,
    missing_diagrams=None,
)

# Save the report
profile.to_file("Soil_Data.html")
print("Profile report saved as 'Soil_Data.html'")

