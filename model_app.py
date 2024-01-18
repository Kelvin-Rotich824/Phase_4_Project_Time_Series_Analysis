import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib
import pathlib

# Set the root directory of your GitHub repository
repo_root = pathlib.Path(__file__).parent.resolve()

# Define the paths to your CSV file and joblib file
csv_file_path = repo_root / "https://github.com/Kelvin-Rotich824/Phase_4_Project_Time_Series_Analysis" / "zillow_data.csv"
joblib_file_path = repo_root / "https://github.com/Kelvin-Rotich824/Phase_4_Project_Time_Series_Analysis" / "arima_model.pkl"

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Load the joblib file
model = load(joblib_file_path)

# Load the saved model

def melt_data(df):
    """
    Takes the zillow_data dataset in wide form or a subset of the zillow_dataset.  
    Returns a long-form datetime dataframe 
    with the datetime column names as the index and the values as the 'values' column.

    If more than one row is passes in the wide-form dataset, the values column
    will be the mean of the values from the datetime columns in all of the rows.
    """
    
    #Melt the DataFrame
    melted = pd.melt(df, id_vars=['RegionName', 'RegionID', 'SizeRank', 'City', 'State', 'Metro', 'CountyName'], var_name='Date')
    
    #Convert the 'Date' column to datatime format
    melted['Date'] = pd.to_datetime(melted['Date'], infer_datetime_format=True)
    
    #Drop rows with missing 'value' entries
    melted = melted.dropna(subset=['value'])

    #Group by 'Date' and calculate the mean of the 'value' column
    return melted.groupby('Date').aggregate({'value':'mean'})

data = melt_data(df)
data_diff = data.diff(periods=1).dropna()
data_diff2 = data_diff.diff(periods=1).dropna()

model.fit(data_diff2)

# Define a function to make predictions
# Function to make predictions
def predict_future(n_periods):
    forecast = model.predict(n_periods=n_periods)
    return forecast

# Create the Streamlit app
st.title("ARIMA Forecast App")

# Enable user input for prediction horizon
n_periods = st.number_input("Enter number of periods to forecast:", min_value=1)

# Generate predictions based on user input
forecast_data = predict_future(n_periods)

# Display forecast data
st.subheader("Forecast")
st.write(forecast_data)

# Visualize the forecast (optional)
st.line_chart(forecast_data)
