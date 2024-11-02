import pandas as pd
from sqlalchemy import create_engine
import requests
##### Ingest Data ######
url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page' 
response = requests.get(url)
with open('yellow_taxi_trips_aug_2024.csv', 'wb') as file:
    file.write(response.content)
    
##### Load the dataset #####
df = pd.read_csv('yellow_taxi_trips_aug_2024.csv')
# Filter and rename columns
df_filtered = df[df['fare_amount'] > 10]
df_transformed = df_filtered.rename(columns={
	'trip_id': 'trip_id',
	'pickup_datetime': 'pickup_time',
	'dropoff_datetime': 'dropoff_time',
	'pickup_location_id': 'pickup_location',
	'dropoff_location_id': 'dropoff_location',
	'fare_amount': 'fare_amount'
})
# Save the transformed DataFrame if needed for verification
df_transformed.to_csv('transformed_data.csv', index=False)

###### Load into DB ######
# Database connection
engine = create_engine('postgresql://lina:1234@localhost/taxi_trips')
# Load data into PostgreSQL
df_transformed.to_sql('yellow_taxi_trips', engine, if_exists='append', index=False)