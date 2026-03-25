import fastf1
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

fastf1.Cache.enable_check("f1_cache")

# load the f1 dataset (Qutar , 2024)
session_2024= fastf1.get_session(2024,24,"R")
session_2024.load()
laps_2024=session_2024.laps[['Driver','LapTime','Sector1Time','Sector2Time','Sector3Time']].copy()
laps_2024.dropna(inplace=True)

#coverting the lap and sector time to seconds
for col in ["LapTime","Sector1Time","Sector2Time","Sector3Time"]:
    laps_2024[f"{col} (s)" ]= laps_2024[col].dt.total_seconds()
