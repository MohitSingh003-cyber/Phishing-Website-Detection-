import pandas as pd
from eda import run_eda
from model import train_model
X, y = run_eda()
print("EDA DONE")
dt_model , rf_model = train_model(X,y)