import math

z_1_a = 1.645 #z_{0.95} - significance level
z_1_b = 1.282 #z_{0.90} - risk willing to take

p0=0.1 #p denoting the proportion of defectives already assumed

delta = 0.10 #change in the proportion defective that we are interested in detecting 

p1 = 0.20 # delta = abs(p1-p0)

N = ((z_1_a*math.sqrt(p0*(1-p0))+z_1_b*math.sqrt(p1*(1-p1)))/delta)**2

print(round(N,3))