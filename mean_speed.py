import pandas as pa
import matplotlib.pyplot as plt 
import datetime 
import numpy as np 

birddata = pa.read_csv("bird_tracking.csv") 
bird_names = pa.unique(birddata.bird_name) 

timestamps = [] 
for k in range(len(birddata)): 
	timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S")) 
birddata["timestamp"] = pa.Series(timestamps, index = birddata.index) 

data = birddata[birddata.bird_name == "Eric"] 
times = data.timestamp 
elapsed_time = [time-times[0] for time in times] 
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1) 

next_day = 1
inds = [] 
daily_mean_speed = [] 
for (i,t) in enumerate(elapsed_days): 
	if t < next_day: 
		inds.append(i) 
	else: 
		daily_mean_speed.append(np.mean(data.speed_2d[inds])) 
		next_day += 1
		inds = [] 

'''data = birddata[birddata.bird_name == "Sanne"] 
times = data.timestamp 
elapsed_time = [time-times[40916] for time in times] 
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1) 

next_day = 1
inds = [] 
daily_mean_speed = [] 
for (i,t) in enumerate(elapsed_days): 
	if t < next_day: 
		inds.append(i) 
	else: 
		daily_mean_speed.append(np.mean(data.speed_2d[inds])) 
		next_day += 1
		inds = [] 

data = birddata[birddata.bird_name == "Nico"] 
times = data.timestamp 
elapsed_time = [time-times[19795] for time in times] 
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1) 

next_day = 1
inds = [] 
daily_mean_speed = [] 
for (i,t) in enumerate(elapsed_days): 
	if t < next_day: 
		inds.append(i) 
	else: 
		daily_mean_speed.append(np.mean(data.speed_2d[inds])) 
		next_day += 1
		inds = []''' 

plt.figure(figsize = (8,6)) 
plt.plot(daily_mean_speed, "rs-") 
plt.xlabel(" Day ") 
plt.ylabel(" Mean Speed (m/s) "); 
plt.show() 
