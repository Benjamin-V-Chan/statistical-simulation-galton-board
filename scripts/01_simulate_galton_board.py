import numpy as np
import pandas as pd
import json

def simulate_galton_board(rows, balls):
    bin_counts = np.zeros(rows + 1, dtype=int)

    for _ in range(balls):
        final_position = sum(np.random.choice([0, 1], size=rows))
        bin_counts[final_position] += 1

    df = pd.DataFrame({"Bin": np.arange(len(bin_counts)), "Count": bin_counts})
    df.to_csv("outputs/galton_simulation_results.csv", index=False)

if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
    simulate_galton_board(config["rows"], config["balls"])