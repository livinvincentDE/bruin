"""@bruin
name: ingestion.trips
type: python
image: python:3.11

connection: duckdb-default

materialization:
  type: table
  strategy: append

columns:
  - name: pickup_datetime
    type: timestamp
    description: "When the meter was engaged"
  - name: dropoff_datetime
    type: timestamp
    description: "When the meter was disengaged"
@bruin"""

import os
os.environ["TZDIR"] = ""
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

import os
import json
import pandas as pd
def materialize():
    start_date = os.environ["BRUIN_START_DATE"]
    end_date = os.environ["BRUIN_END_DATE"]
    taxi_types = json.loads(os.environ["BRUIN_VARS"]).get("taxi_types", ["yellow"])

    # Temporary dummy dataframe for testing
    data = {
        "pickup_datetime": ["2022-01-01 10:00:00"],
        "dropoff_datetime": ["2022-01-01 10:30:00"],
        "payment_type": [1],
        "total_amount": [25.5],
    }

    df = pd.DataFrame(data)
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])

    return df