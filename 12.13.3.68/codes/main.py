from scipy.stats import bernoulli
import numpy as np
import random

A=bernoulli.rvs(size=10000,p=random.random())
B=bernoulli.rvs(size=10000,p=random.random())

c1=0
c2=0
#P(A'|B')
for i in range(0,10000):
	if 1-B[i]==1:
		c2=c2+1;
		if 1-A[i]==1:
			c1=c1+1
p1=c1/c2

#[1-P(A+B)]/P(B')
c1=0
c2=0
for i in range(0,10000):
	if A[i]==1 or B[i]==1:
		c1=c1+1
	if 1-B[i]==1:
		c2=c2+1
p2=(10000-c1)/c2
print("P(A'/B')=",p1)
print("[1-P(A+B)]/P(B')=",p2)
if p1==p2:
	print("Proved that P(A'/B')=[1-P(A+B)]/P(B')")
