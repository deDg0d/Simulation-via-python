import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
#inputs

#time interval exp with lambda = 3 and service time is exp with lambda of 4
#lambda for time interval is 3 and for service time is 4
numberofcustomers=100
number_of_replications=2
warmp_up_period = 10


time_intervals = []
service_time = []
total_average_idle_time = [] #average of each replication
total_average_queue_time = [] #average of each replication
total_average_time_spent = [] #average of each replication
lambda_for_arrival= 3
lambda_for_service = 4
for _ in range(number_of_replications):
    for c in range(numberofcustomers):
        random_for_arrival=np.random.random_sample() #save random number between 0 and  1
        time_intervals.append ((1/-lambda_for_arrival)*(math.log(random_for_arrival))) #-ln(r)/lambda
        random_for_service_time = np.random.random_sample()
        service_time.append((1/-lambda_for_service)*(math.log(random_for_service_time)))

    time_service_begins= []
    arrival_time= [] #arrival time
    time_service_ends = []
    waiting_time_in_queue = []
    time_customer_spends_in_system = [] #cycle time
    Idle_time = [] #idle time
    customer_counter = time_intervals
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
    #warm up period for simulation
    
    for c in range(warmp_up_period,len(customer_counter)):
    #adding values of queue list
        average_queue_time = average_queue_time+waiting_time_in_queue[c]
    #average idle time of server
        average_idle_time = average_idle_time + Idle_time [c]
    #calculating average of above value
    average_queue_time= average_queue_time/len(arrival_time) #/number of customers
    average_idle_time = average_idle_time/simulation_time 
    #calculating Ls
    #arrival = 1 departure = 0
    arr_arrival = [[1,arrival_time[c]]]*len(arrival_time+time_service_ends) #array created to save arrival values for the length of all events(arrival-departure)
    data = np.array(arr_arrival) 
    for c in range(len(arrival_time)):
        
        data[c,1] = arrival_time[c]
        data[len(arrival_time)+c,1] = time_service_ends[c]
        data[len(arrival_time)+c,0] = 0

    sorted_data = data[data[:, -1].argsort()] #sort 2d array based on its last element
    ls = 0
    lsa = [] #type of ls, created for representing in dataframe
    for c in range(len(data)):
        if sorted_data[c,0] == 1: # if an event were arrival
            ls+=1 
            lsa.append(ls)
        else: #event is departure
            ls-=1
            lsa.append(ls)
    presenting_data = []
    presenting_event = []
    #codes for representing dataframe based on clock,Ls, and type of event
    for c in range(len(arrival_time + time_service_ends)):
        presenting_data.append(sorted_data[c,1])
        presenting_event.append(sorted_data[c,0])

    dataset2 = {
        'type of event' : presenting_event ,
        'ls' : lsa
    }
    clock = presenting_data
    df2 = pd.DataFrame(dataset2)
    df2 = df2.set_index([pd.Index(clock)])
    df2.index.names = ['clock']
    print(df2)
    # plt.plot(lsa)
    # plt.show()
    # print(ls)



    
    
    


    

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
    # print(df)
    #saving average data for each replication
    total_average_idle_time.append(average_idle_time)
    total_average_queue_time.append(average_queue_time)
    dataset_for_average = {
        'average idle time' : total_average_idle_time,
        'average queue time' : total_average_queue_time
    }
    df_for_replications = pd.DataFrame(dataset_for_average)
    df_for_replications.index = np.arange(1, len(df_for_replications) + 1)
    df_for_replications.index.names = ['customer']
    # print(df_for_replications)
    print(f'average idle time is: {sum(total_average_idle_time)/number_of_replications},\naverage queue time is: {sum(total_average_queue_time)/number_of_replications}')
total_average_idle_time.append(sum(total_average_idle_time)/number_of_replications)
total_average_queue_time.append(sum(total_average_queue_time)/number_of_replications)
#adding average to the end of the dataframe

dataset_for_average = {
        'average idle time per replication' : total_average_idle_time,
        'average queue time per replication' : total_average_queue_time
    }
df_for_replications = pd.DataFrame(dataset_for_average)
df_for_replications.index = np.arange(1, len(df_for_replications) + 1)
df_for_replications.index.names = ['customer']

# print(df_for_replications)
#calculating the chance of finding 10 customers in system


# p = lambda_for_arrival/ lambda_for_service
# n = 10
# pn = (p**(n))*(1-p)


            




#visualazing the data
# time_intervals.sort()
# time_intervals.reverse()
# service_time.sort()
# service_time.reverse()
# plt.hist(service_time, bins = 10)
# plt.hist(time_intervals)
# plt.plot(time_intervals, "b-", label="t intervals(3)")
# plt.plot(service_time, 'r',label="t service(4)")
# plt.legend(loc="upper right")
# plt.show()


