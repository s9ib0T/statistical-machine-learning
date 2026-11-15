import numpy as np
import pandas as pd

# This preprocessing is meant to be shared between the models
#  so we do not add scaling here, do that for the models as needed.

def load(path):
    df = pd.read_csv(path)
    y = (df.increase_stock == "high_bike_demand") * 1
    x = df.drop(columns=["increase_stock", "snow"]) # snow always 0
    return x, y

def add_features(x):
    x = x.copy()
    x["daytime"] = x.hour_of_day.between(7, 20) * 1
    # can add more features here
    return x