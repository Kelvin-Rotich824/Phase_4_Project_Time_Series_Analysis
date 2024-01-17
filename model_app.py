import streamlit as st
import pandas as pd
from prophet import Prophet
import joblib
# Load your time-series data
df = pd.read_csv("zillow_data")
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

data_diff2.reset_index(inplace=True)
data_diff2 = data_diff2.rename(columns={'Date': 'ds', 'value': 'y'})

model = joblib.load('prophet_model.pkl') 
model.fit(data_diff2)

# Define a function to make predictions
def predict_future(n_months):
    future_dates = model.make_future_dataframe(periods=n_months, freq='MS')  # Monthly frequency
    forecast = model.predict(future_dates)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]  # Include uncertainty

# Create the Streamlit app
st.title("Monthly Time Series Forecast App") 
# Enable user input for prediction horizon
n_months = st.number_input("Enter number of months to forecast:", min_value=1, value=12)

# Generate predictions based on user input
forecast_data = predict_future(n_months)

# Display forecast components
st.subheader("Forecast Components")
fig = model.plot_components(forecast_data)
st.write(fig)

# Display forecast data
st.subheader("Forecast Table")
st.write(forecast_data)
