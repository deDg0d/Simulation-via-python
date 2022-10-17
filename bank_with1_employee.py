from importlib.metadata import entry_points
from smtplib import quotedata
from time import time
from tracemalloc import start
import pandas as pd
import numpy as np
#inputs
time_intervals = [0,5,6,1,2,8,5,2,4,6]
service_time = [3,2,1,5,3,4,2,1,5,3]
entering_time= []
starting_time= []
ending_time = []
queue_time = []
time_spent = []
employee_rest = []
x = 0
#we assume that first employee will be present in system
#append method is used in python for adding values to a list
employee_rest.append(0)
#calculating entry time(adding time_intervals values into one list=> time that system have been running, time customer enters)
#further calculations are based on this instead of time intervals
for i in range(len(time_intervals)):
    #x is a temporary variable to sum up the time_intervals values
 x = x + time_intervals[i]
 entering_time.append(x)
print(entering_time)
#first start and ending time(we assume first customer receive service in time 0)
starting_time.append(0)
#ending time for first customer will be the time he/she start to get service + his/her service time
ending_time.append(starting_time[0] + service_time[0])
#calculating all start, ending time and employee rest
#first employee won't experience queue due to the fact that there is no one before and employee is ready
queue_time.append(0)
#time spent for first employee will be his/her service time only because there is no queue
time_spent.append(service_time[0])
#this for loop starts from 1 due to the fact that we calculate first items by assumptions 
for i in range(1,len(time_intervals)):
    #this if loops checks if customer whould wait in line or not
    #if time that customer i enters the system was lower than previous customer(i-1)E.g. customer i
    #came in min 5 but customer i-1 will finish his/her job in min 6:
    if(entering_time[i]<= ending_time[i-1]):
        #starting time of i will be when i-1 finish his/her job(queue for i)
        starting_time.append(ending_time[i-1])
        #ending time will be starting time + service time
        ending_time.append(starting_time[i] + service_time[i])
        #whenever there is a queue there is no rest for employee
        employee_rest.append(0)
        #queue time can be determined(time he/she enter the sytem - time that previous customer fully served)
        queue_time.append(abs(entering_time[i] - ending_time[i-1]))
        #total time spent on system: his/her queue time + service time
        time_spent.append(queue_time[i] + service_time[i])
#this if is for customers that will not experience queue
#E.g. he/she enters in min 10 and last customer fully served at min 8
    if(entering_time[i]>ending_time[i-1]):
        # he/she start to get served as soon as he/she enters the system
        starting_time.append(entering_time[i])
        ending_time.append(starting_time[i] + service_time[i])
        #our employee waits until next customer enters
        # time that new customer entered - time that previous customer left the system will be rest time for employee 
        employee_rest.append(abs(starting_time[i] - ending_time[i-1]))
        #no queue for customer
        queue_time.append(0)
        #time spent for customer is queue time + service time
        time_spent.append(queue_time[i] + service_time[i])

#calculating outputs, and problem requirements

average_queue_time = 0
#for 10 customers
for i in range(10):
    #adding values of queue list
    average_queue_time = average_queue_time+queue_time[i]
    #calculating average of above value
average_queue_time= average_queue_time/10  
#creating dataset to visualize data
dataset = {
    'entery time' : entering_time,
    'service time' : service_time,
    'starting time' : starting_time,
    'ending time' : ending_time,
    'rest' : employee_rest,
    'queue time' : queue_time,
    'avg' : average_queue_time,
    't spent' : time_spent
}

#visualizing data with pandas library
df = pd.DataFrame(dataset)
print(df)

#based on our calculation we can determine:
#1- do we need more employee?
#2- do we need less employees(if we had 2 or more)
#3- how much our employee have free time in service time
#4- is the queue time reasonable? do we need to buy chairs for customers that wait in line
#5- is time spent on system reasonable? should wa apply changes to our system?




