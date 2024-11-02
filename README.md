# Kalvad-Test
This is Lina Mohammed Osman Solutions.

## Getting Started

 db connection credentials:

```
DB_HOST=localhost
DB_PORT=5432
DB_USER=lina
DB_PASS=1234
```

Make sure Postgress is installed 
Then,creat Database (taxi_trips) and Table (yellow_taxi_trips):
```bash
CREATE TABLE yellow_taxi_trips (
    vendor_id VARCHAR,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count INT,
    trip_distance FLOAT,
    pickup_location_id INT,
    dropoff_location_id INT,
    fare_amount FLOAT,
    extra FLOAT,
    mta_tax FLOAT,
    tip_amount FLOAT,
    tolls_amount FLOAT,
    total_amount FLOAT,
    payment_type INT,
    trip_id SERIAL PRIMARY KEY
);

```
Import python libraries:
```bash
import os
import pandas as pd
from sqlalchemy import create_engine
import requests
```

## Part 1: SQL Challenge
[Solution](https://docs.google.com/document/d/1ZJNhUOOalDM79pMP-OQOhnTjDEtpcTSHO4GD6g619Iw/edit?usp=sharing)

## Part 2: Data Pipeline Design
[Solution](https://docs.google.com/document/d/1oQ3OwZyixcyDm_98nECwiFow_xygLziE5717kOccQgw/edit?usp=sharing)

## Part 3: Data Processing with Python 
[Solution](https://docs.google.com/document/d/1jsoi-S02nGbXwZgNjZziBTtEvwo6685dbNG2mDVW11k/edit?usp=sharing)

## Part 4: Data Visualization
[Solution](https://docs.google.com/document/d/16YONK9Mgvy2cagWmZFHC-zcmfpbvNP72bOZQZTjVSh0/edit?usp=sharing)
