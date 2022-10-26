import pandas as pd
import numpy as np
#inputs
time_intervals = [0,5,6,1,2,8,5,2,4,6]
service_time = [3,2,1,5,3,4,2,1,5,3]
arrival_time= [] #arrival time
time_service_begins= []
time_service_ends = []
waiting_time_in_queue = []
time_customer_spends_in_system = [] #cycle time
Idle_time = [] #idle time
customer_counter = time_intervals
# print(customer_counter)
#x is a temporary variable to sum up the time_intervals values
#we assume that first employee will be present in the system
#append method is used in python for adding values to a list
Idle_time.append(0) #to prevent error in pandas
#calculating entry time(adding time_intervals values into one list=> time that system have been running)
#further calculations are based on this instead of time intervals
x = 0 # temp variable
for c in range(len(time_intervals)):
 x = x + time_intervals[c]
 arrival_time.append(x)

#first starting and ending time(we assume first customer receives service in time 0)
time_service_begins.append(time_intervals[0])
#ending time for first customer will be the time he/she starts to get service + his/her service time
time_service_ends.append(time_service_begins[0] + service_time[0])
#calculating all starting, ending time and employee rest
#first employee will not experience queue due to the fact that there is no one before and employee is ready
waiting_time_in_queue.append(0)
#time spent for first employee will be his/her service time only because there is no queue
time_customer_spends_in_system.append(service_time[0])
#this for loop starts from 1 because that we calculated first items by assumptions 
for c in range(1,len(customer_counter)): #{

    #this if loops checks if customer would wait in line or not
    #if time that customer i entered the system was lower than previous customer(i-1)E.g. customer i   -
    #came in min 5 but customer i-1 will finish his/her job in min 6:
    if(arrival_time[c]<= time_service_ends[c-1]): #i-1 throws an error if started from 0
        #starting time of i will be when i-1 finish his/her job(queue for i)
        time_service_begins.append(time_service_ends[c-1])
        #ending time will be starting time + service time
        time_service_ends.append(time_service_begins[c] + service_time[c])
        #queue time can be determined(time he/she enter the sytem - time that previous customer fully served)
        waiting_time_in_queue.append(time_service_ends[c-1] - arrival_time[c])
        #total time spent on system: his/her queue time + service time
        time_customer_spends_in_system.append(time_service_ends[c] - arrival_time[c] ) #waiting_time_in_queue[c] + service_time[c]
        #whenever there is a queue there is no rest for employee
        Idle_time.append(0)
#this if is for customers that will not experience queue
#E.g. he/she enters in min 10 and last customer fully served at min 8
    else: #arrival_time[c]>time_service_ends[c-1]
        # he/she start to get served as soon as he/she enters the system
        time_service_begins.append(arrival_time[c])
        time_service_ends.append(time_service_begins[c] + service_time[c]) #arrival_time[c] + service_time[c] ()
        #our employee waits until next customer enters
        waiting_time_in_queue.append(0)
        #time spent for customer is queue time + service time
        time_customer_spends_in_system.append(waiting_time_in_queue[c] + service_time[c])
        # time that new customer entered - time that previous customer left the system will be rest time for employee 
        Idle_time.append(abs(time_service_begins[c] - time_service_ends[c-1])) ###cal after cal
        #no queue for customer
#} #end of for

#calculating outputs, and problem requirements

average_queue_time = 0
average_idle_time = 0
simulation_time = time_service_ends[-1]
#for 10 customers
for c in range(10):
    #adding values of queue list
    average_queue_time = average_queue_time+waiting_time_in_queue[c]
    #average idle time of server
    average_idle_time = average_idle_time + Idle_time [c]
    #calculating average of above value
average_queue_time= average_queue_time/len(arrival_time) #/number of customers
average_idle_time = average_idle_time/simulation_time 
#creating dataset to visualize data
dataset = {
    'Arrival t' : arrival_time,
    'Service t' : service_time,
    'service begins' : time_service_begins,
    'service ends' : time_service_ends,
    'Idle t' : Idle_time,
    'Waiting t in queue' : waiting_time_in_queue,
    't in system' : time_customer_spends_in_system,
    'avg queue' : average_queue_time,
    'avg idle' : average_idle_time
}

#visualizing data with pandas library
df = pd.DataFrame(dataset)
#changing starting index from 0 to 1
df.index = np.arange(1, len(df) + 1)
df.index.names = ['customer']
print(df)

#based on our calculation we can determine:
#1- do we need more employee?
#2- do we need less employees(if we had 2 or more)
#3- how much our employee have free time in service time
#4- is the queue time reasonable? do we need to buy chairs for customers that wait in line
#5- is time spent on system reasonable? should wa apply changes to our system?




