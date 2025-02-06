import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(input_csv):
    df = pd.read_csv(input_csv)
    
    plt.bar(df["Bin"], df["Count"], alpha=0.7, label="Empirical")
    plt.xlabel("Bins")
    plt.ylabel("Ball Count")
    plt.title("Galton Board Simulation Results")
    plt.legend()
    plt.savefig("outputs/histograms/galton_histogram.png")
    plt.show()

if __name__ == "__main__":
    plot_histogram("outputs/galton_simulation_results.csv")