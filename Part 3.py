import os
import requests
import pandas as pd
from sqlalchemy import create_engine

# Constants
DATA_URL = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'  
LOCAL_FILE = 'yellow_taxi_trips_aug_2024.csv'
DB_CONNECTION_STRING = 'postgresql://lina:1234@localhost/taxi_trips'  

# Step 1: Download the dataset if it does not exist locally
if not os.path.exists(LOCAL_FILE):
    response = requests.get(DATA_URL)
    if response.status_code == 200:
        with open(LOCAL_FILE, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded dataset and saved as {LOCAL_FILE}.")
    else:
        print(f"Failed to download dataset: {response.status_code}")
        exit(1)
        
# Step 2: Load data into PostgreSQL
# Create a database engine
engine = create_engine(DB_CONNECTION_STRING)

# Load the dataset into a pandas DataFrame
df = pd.read_csv(LOCAL_FILE)

# Load the DataFrame into PostgreSQL
df.to_sql('yellow_taxi_trips', engine, if_exists='replace', index=False)
print("Data loaded into PostgreSQL database.")

# Step 3: Calculate average fare per day of the week
# Convert pickup_time to datetime
df['pickup_time'] = pd.to_datetime(df['pickup_datetime'])

# Extract day of the week and calculate average fare
df['day_of_week'] = df['pickup_time'].dt.day_name()
average_fare_per_day = df.groupby('day_of_week')['fare_amount'].mean().reset_index()

# Sort by the day of the week
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
average_fare_per_day['day_of_week'] = pd.Categorical(average_fare_per_day['day_of_week'], categories=days_order, ordered=True)
average_fare_per_day = average_fare_per_day.sort_values('day_of_week')

# Step 4: Save the summary report to CSV
average_fare_per_day.to_csv('average_fare_per_day.csv', index=False)
print("Summary report saved as average_fare_per_day.csv.")


