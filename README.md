# Test_result_analysis

### Sample calculation

The script for sample calculation use the material from [Nist](https://www.itl.nist.gov/div898/handbook/prc/section2/prc242.htm).
This was used to evaluate if the sample size is suficient for taking conclusions about the data.

```python
import math

z_1_a = 1.645 #z_{0.95} - significance level
z_1_b = 1.282 #z_{0.90} - risk willing to take

p0=0.1 #p denoting the proportion of defectives already assumed

delta = 0.10 #change in the proportion defective that we are interested in detecting 

p1 = 0.20 # delta = abs(p1-p0)

N = ((z_1_a*math.sqrt(p0*(1-p0))+z_1_b*math.sqrt(p1*(1-p1)))/delta)**2

print(round(N,3))
```

For this analysis, the ideal sample size would be 102.

### Data separation

Reading the csv file, the data was separated and stored in diferent vectors, which one for a test condition.

```python
    cond_1=[]
    for i in range(1, len(data)):
            if len(data[i]) >= 5 and int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==0:
                cond_1.append(data[i])
    cond_2=[]
    for i in range(1, len(data)):
            if len(data[i]) >= 5 and int(data[i][1])==433 and int(data[i][2])==14 and int(data[i][3])==7 and int(data[i][4])==2:
                cond_2.append(data[i])

```

### Parameters Calculation

In this script, the mean, variance, std deviation and confidence interval were calculated.
```python
for condition_num in range(1, num_conditions + 1):
    # Assuming TX_data.cond_1, TX_data.cond_2, ..., TX_data.cond_40 exist
    condition_data = getattr(TX_LoRa_data_filtering, f"cond_{condition_num}")

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
```
The script also stores the mean and the confidence intervals for each condition, so we can analyse the samples condensed in each condition.


