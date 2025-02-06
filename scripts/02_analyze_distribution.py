import pandas as pd
import numpy as np
from scipy.stats import binom, chisquare

def analyze_distribution(input_csv):
    df = pd.read_csv(input_csv)
    total_balls = df["Count"].sum()
    rows = df["Bin"].max()
    
    expected_probs = binom.pmf(df["Bin"], rows, 0.5)
    expected_counts = expected_probs * total_balls

    chi2_stat, p_value = chisquare(df["Count"], expected_counts)

    df["Expected"] = expected_counts
    df.to_csv("outputs/summary_statistics.csv", index=False)

    return chi2_stat, p_value

if __name__ == "__main__":
    analyze_distribution("outputs/galton_simulation_results.csv")