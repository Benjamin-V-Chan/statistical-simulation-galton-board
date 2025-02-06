import json
import numpy as np
import pandas as pd

def run_monte_carlo_simulation(n_simulations, rows, balls):
    results = []
    
    for _ in range(n_simulations):
        bin_counts = np.zeros(rows + 1, dtype=int)
        for _ in range(balls):
            final_position = sum(np.random.choice([0, 1], size=rows))
            bin_counts[final_position] += 1
        
        results.append({
            "mean": np.mean(bin_counts),
            "variance": np.var(bin_counts),
            "skewness": pd.Series(bin_counts).skew(),
            "kurtosis": pd.Series(bin_counts).kurt()
        })
    
    with open("outputs/monte_carlo_results.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
    run_monte_carlo_simulation(config["n_simulations"], config["rows"], config["balls"])