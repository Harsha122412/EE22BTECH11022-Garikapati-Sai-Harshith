from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt
#(a)
A=np.array(np.random.randint(1,7,size=10000))
c=0
for i in range(0,10000):
	if A[i]%2==0:
		c=c+1
print(c/10000)
#(b)
B1=bernoulli.rvs(size=10000,p=0.5)
B2=bernoulli.rvs(size=10000,p=0.5)
c=0
for i in range(0,10000):
	if B1[i]+B2[i]>0:
		c=c+1
print(c/10000)
#(c)
shape=np.array(np.random.randint(1,5,size=10000))
numb=np.array(np.random.randint(1,14,size=10000))
c=0
for i in range(0,10000):
	if numb[i]==13:
		c=c+1
	if shape[i]==3 and numb[i]==9:
		c=c+1
	if shape[i]==4 and numb[i]==3:
		c=c+1
print(c/10000)
#(d)
D1=np.array(np.random.randint(1,7,size=10000))
D2=np.array(np.random.randint(1,7,size=10000))
c=0
for i in range(0,10000):
	if D1[i]+D2[i]==6:
		c=c+1
print(c/10000)
num_sides = 6
outcomes = np.arange(1, num_sides + 1)
sums = outcomes[:, np.newaxis] + outcomes
probabilities = np.bincount(sums.flatten())[2:] / (num_sides ** 2)
x = np.arange(2, 2 * num_sides + 1)
fig, ax = plt.subplots()
ax.stem(x, probabilities, basefmt=' ')
ax.set_xlabel('Sum of Dice')
ax.set_ylabel('Probability')
ax.set_title('PMF of Sum of Two Dice')
ax.set_ylim(0.00, max(probabilities) + 0.05)
plt.xticks(x)
plt.savefig("../figs/figure.png")
plt.show()
