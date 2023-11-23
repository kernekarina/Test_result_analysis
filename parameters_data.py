import TX_data
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import math

# Number of conditions
num_conditions = 40
# Data storage for means and confidence intervals
means = []
conf_intervals = []

for condition_num in range(1, num_conditions + 1):
    # Assuming TX_data.cond_1, TX_data.cond_2, ..., TX_data.cond_40 exist
    condition_data = getattr(TX_data, f"cond_{condition_num}")

    # Extract power values for the current condition
    power_values = [float(row[5]) for row in condition_data[1:]]

    # Calculate parameters for the current condition
    x_barra = round(np.mean(power_values), 4)
    variancia = round(np.var(power_values), 4)
    std_dev = round(np.std(power_values), 4)

    # Calculate t-statistic and confidence interval
    n = len(power_values)
    gl = n - 1
    # Nível de confiança
    p = 0.90
    # Complementar
    alpha = 1 - p
    ts = stats.t.ppf(alpha, gl)
    tol = round(ts * std_dev / (math.sqrt(n)), 4)

    # Store means and confidence intervals
    means.append(x_barra)
    conf_intervals.append(tol)

    # Print the results for the current condition
    print(f'Parameters for Condition {condition_num}:')
    print(f'Mean: {x_barra}')
    print(f'Variance: {variancia}')
    print(f'Standard Deviation: {std_dev}')
    print(f'Confidence Interval: {x_barra} +- {tol}\n')

# Plotting
conditions = range(1, num_conditions + 1)
plt.bar(conditions, means)
plt.xlabel('Conditions')
plt.ylabel('Mean')
plt.title('Means for Conditions')
plt.show()