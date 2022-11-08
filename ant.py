import numpy as np
import pandas as pd
seed = []
storage = 0
consumed_seed1 = 0 #ant that consume all seeds
consumed_seed_2 = 0 #ant that store half of the seeds
consumed_seed_2_list = [] #just for demonstration
storage_list = []#just for demonstration
days = 100
for i in range(days):
     seed.append(np.random.exponential(scale = 2)) #random between 0 to 10
     seed[i] = round(seed[i])


for i in range(days): #simulation for ant 2
    if seed[i] >4: #if it find more that 4 seeds in a day
        
        consumed_seed_2 = consumed_seed_2 + 2
        consumed_seed_2_list.append(2) #TO SHOW THE PROCESS
        storage = storage + (seed[i] - 2)  
        storage_list.append(seed[i] - 2) #TO SHOW THE PROCESS

    else:
        storage = storage + (seed[i] /2 )
        storage_list.append(seed[i] / 2) #TO SHOW THE PROCESS
        consumed_seed_2 = consumed_seed_2 + (seed[i]/2)
        consumed_seed_2_list.append(seed[i]/2) #TO SHOW THE PROCESS
for i in range(days): #simulation for ant 1
    if seed[i]<3:
        consumed_seed1 = consumed_seed1 + seed[i]
    else :
        consumed_seed1 = consumed_seed1 + 2
    


dataset = {
    'seed found' : seed,
    'storage' : storage_list,
    'ant 2 consumption' : consumed_seed_2_list
}

df = pd.DataFrame(dataset)

print(df)
print(f'total storage is{storage}')
print(f'total consumption of ant2 is {consumed_seed_2}')
print(f'consumtion of ant 1 is {consumed_seed1}')