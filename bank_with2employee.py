from tracemalloc import start
import numpy as np
import pandas as pd
entry_interval =[]
service_time = []
entry_time = []
starting = []
ending = []
queue = []
employee1_ready = 0
employee2_ready = 0

#inputs
for i in range(40):
    entry_interval.append(np.random.choice([1,2,3,4,5], p=[0.5,0.3,0.1,0.05,0.05]))
    service_time.append(np.random.choice(np.arange(1,6)))
#assumptions
entry_time.append(0)
queue.append(0)
x = 0
for i in range(39):
 x = x + entry_interval[i]
 entry_time.append(x)

starting.append(0)
ending.append(starting[0]  + service_time[0])
employee1_ready = ending[0]
for i in range(1,40):
 print(employee1_ready)

#  print(employee1_ready,employee2_ready)
    #both employees are free, emp1 will serve
 if(entry_time[i] >= employee1_ready and entry_time[i]>= employee2_ready ):

   starting.append(entry_time[i])
   ending.append(starting[i] + service_time[i])
   employee1_ready = ending[i]
   queue.append(0)
   #both free emp2 will serv

    #both busy
 elif(entry_time[i] < employee1_ready and entry_time[i]< employee2_ready):
    print('both busy')
    if(employee1_ready <= employee2_ready):
     starting.append(employee1_ready)
     ending.append(starting[i] + service_time[i])
     employee1_ready = ending[i]
    elif(employee2_ready<employee1_ready):
    #  employee2_ready = entry_time[i]
     starting.append(employee2_ready)
     ending.append(employee2_ready + service_time[i])
     employee2_ready = ending[i]
    queue.append(abs(entry_time[i] - ending[i]))
    #one is free
 elif(entry_time[i]>=employee1_ready ):
   starting.append(entry_time[i])
   ending.append(starting[i]+ service_time[i])
   employee1_ready = ending[i]
   queue.append(0)

    #two is free
 elif(entry_time[i]<employee1_ready ):
    if(employee2_ready==0):
      employee2_ready = entry_time[i]
    starting.append(entry_time[i])
    ending.append(starting[i]+ service_time[i])
    employee2_ready = ending[i]
    queue.append(0)
    




   
dataset = {
    'entry' : entry_time,
    'service' : service_time,
    'start' : starting,
    'end' : ending,
    'queue' : queue
}
df = pd.DataFrame(dataset)
print(df)




