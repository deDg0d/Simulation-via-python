import numpy as np
import matplotlib.pyplot as plt

#rand uniform
rand_uni = []
for _ in range(100):
    rand_uni.append(np.random.choice([0,1])) #uniform
print(rand_uni)

#exp distribution

rand_exp = []
for i in range(500):
    rand_exp.append (np.random.exponential(scale = 1/3)) #The scale parameter = rate = 10
    # rand_exp[i] = round(rand_exp[i]) #to save integer numbers


#normalize between 0 and 1
# for i in range(len(rand_exp)) :
#     rand_exp[i] = rand_exp[i] / max(rand_exp)
# print(rand_exp)

#calculating the prob
def exp(x,lam): #probability distribution function
    return lam* np.exp(-lam * x)
def exp_cdf(x,lam): #cumulative distribution function
    return (np.exp(-lam *x)) # = p(X>x)
# print(exp_cdf(15,0.1))  #rate = 10 , p(X>15)?
# print(exp(np.array(rand_exp),1/10))
# print(exp(np.array([1,2,3]),2))

#to see the distribution shape 

rand_exp.sort()
rand_exp.reverse()
print(rand_exp)
plt.hist(rand_exp)
plt.show()
