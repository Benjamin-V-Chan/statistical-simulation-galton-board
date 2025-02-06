# statistical-simulation-galton-board

## Project Overview

The Galton Board, also known as the **Quincunx**, is a classic probability experiment that demonstrates the **central limit theorem** and the **binomial-to-normal distribution transition**. This project simulates the behavior of balls dropping through a triangular array of pegs, where each ball has an equal probability of moving left or right at each peg. Over a sufficiently large number of trials, the final distribution of balls across bins approximates a **normal distribution**.

### **Mathematical Foundation**

#### **Binomial Probability Model**
Each ball undergoes a sequence of independent Bernoulli trials with success probability **p = 0.5** (right movement) and failure probability **q = 1 - p = 0.5** (left movement). The probability that a ball lands in bin $\( k \)$ after $\( n \)$ rows follows a **binomial distribution**:

$$P(X = k) = \binom{n}{k} p^k q^{n-k}$$

where:
- $\( n \)$ is the number of rows (trials)
- $\( k \)$ is the number of right movements
- $\( p = 0.5 \)$ is the probability of moving right
- $\( q = 0.5 \)$ is the probability of moving left
- $\( \binom{n}{k} = \frac{n!}{k!(n-k)!} \)$ is the binomial coefficient

#### **Normal Approximation (Central Limit Theorem)**
By the **De Moivre-Laplace Theorem**, for large $\( n \)$, the binomial distribution can be approximated by a normal distribution with:

- Mean: $$\mu = np$$
- Variance: $$\sigma^2 = np(1 - p)$$

Using the **normal approximation**, the probability of landing in bin \( k \) is:

$$P(X = k) \approx \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(k - \mu)^2}{2 \sigma^2}}$$

where:
- $\( \sigma = \sqrt{np(1 - p)} \)$ is the standard deviation

#### **Skewness and Kurtosis**
For a binomial distribution, the skewness and kurtosis are:

- **Skewness:** $$\gamma_1 = \frac{1 - 2p}{\sqrt{np(1 - p)}}$$
- **Excess Kurtosis:** $$\gamma_2 = \frac{1 - 6p(1 - p)}{np(1 - p)}$$

As $\( n \to \infty \)$, skewness approaches $0$, and kurtosis approaches $3$ (Gaussian distribution), confirming the **normal convergence**.

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_simulate_galton_board.py  # Runs the simulation
│   ├── 02_analyze_distribution.py   # Compares results to binomial & normal distributions
│   ├── 03_monte_carlo_simulation.py # Runs Monte Carlo experiments
│   ├── 04_visualize_results.py      # Generates plots and histograms
│   ├── 05_generate_statistics.py    # Computes statistics like mean & variance
├── outputs/
│   ├── histograms/
│   ├── summary_statistics.csv
│   ├── monte_carlo_results.json
│   ├── galton_simulation_results.csv
├── config.json                       # Stores simulation parameters
├── requirements.txt                  # Required Python packages
└── README.md                         # Project documentation
```

## Usage

### **1. Setup the Project:**
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### **2. Run the Galton Board Simulation**
Fill out the config.json. Then run this script that simulates the Galton Board experiment with the specified number of rows and balls.
```bash
python scripts/01_simulate_galton_board.py
```

### **3. Analyze Distribution Fit**
Compares empirical data to expected binomial and normal distributions.
```bash
python scripts/02_analyze_distribution.py
```

### **4. Monte Carlo Simulation**
Runs multiple simulations to assess statistical properties.
```bash
python scripts/03_monte_carlo_simulation.py
```

### **5. Generate Histograms & Visualizations**
Plots the final ball distribution and overlays a normal curve.
```bash
python scripts/04_visualize_results.py
```

### **6. Compute Summary Statistics**
Computes mean, variance, standard deviation, skewness, and kurtosis.
```bash
python scripts/05_generate_statistics.py
```

## Requirements
- **Python 3.8+**
- **Required Libraries:**
  ```
  numpy
  pandas
  matplotlib
  ```
  Install all dependencies using:
  ```bash
  pip install -r requirements.txt
  ```