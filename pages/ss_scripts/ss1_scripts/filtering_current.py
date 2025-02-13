import pandas as pd
import os
from pages.ss_scripts.ss1_scripts.calculations import mf_returns_calculations

def get_top_funds(min_days, top_n_alpha):
    
    df_mf = pd.read_csv(os.path.join("Data", "Input", "mf_eom.csv"))
    df_index = pd.read_csv(os.path.join("Data", "Input", "nifty_eom.csv"))
    df = mf_returns_calculations(df_mf, df_index)
    
    # Filter based on minimum days
    df_filtered = df[df["Duration (Days)"] >= min_days]

    # Sort by Excess Return (%) in descending order
    df_sorted = df_filtered.sort_values(by="Excess Return (%)", ascending=False)

    # Select top N funds
    return df_sorted.head(top_n_alpha)