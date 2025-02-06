import pandas as pd

def compute_statistics(input_csv):
    df = pd.read_csv(input_csv)

    stats = {
        "mean": df["Count"].mean(),
        "variance": df["Count"].var(),
        "std_dev": df["Count"].std(),
        "skewness": df["Count"].skew(),
        "kurtosis": df["Count"].kurt()
    }

    stats_df = pd.DataFrame([stats])
    stats_df.to_csv("outputs/summary_statistics.csv", index=False)

if __name__ == "__main__":
    compute_statistics("outputs/galton_simulation_results.csv")