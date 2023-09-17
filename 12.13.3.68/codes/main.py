from scipy.stats import bernoulli
import numpy as np
import random

A=bernoulli.rvs(size=10000,p=random.random())
B=bernoulli.rvs(size=10000,p=random.random())

#P(A'|B')
c1=np.sum(1-B)
c2=np.sum((1-A) & (1-B))
p1=c2/c1

#[1-P(A+B)]/P(B')
c1=np.sum(A|B)
c2=np.sum(1-B)
p2=(10000-c1)/c2
print("P(A'/B')=",p1)
print("[1-P(A+B)]/P(B')=",p2)
if p1==p2:
	print("Proved that P(A'/B')=[1-P(A+B)]/P(B')")
