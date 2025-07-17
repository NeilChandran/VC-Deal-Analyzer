import numpy as np

def run_simulation(initial_investment, expected_return, std_dev, iterations=10000):
    returns = np.random.normal(expected_return, std_dev, size=iterations)
    simulated_outcomes = initial_investment * (1 + returns)
    return simulated_outcomes

def summarize_simulation(sim):
    print(f"Mean: {np.mean(sim):,.2f}")
    print(f"Median: {np.median(sim):,.2f}")
    print(f"95% Value at Risk: {np.percentile(sim, 5):,.2f}")

if __name__ == "__main__":
    results = run_simulation(100000, 0.3, 0.6)
    summarize_simulation(results)



