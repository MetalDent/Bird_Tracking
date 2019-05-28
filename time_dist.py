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

times = birddata.timestamp[birddata.bird_name == "Eric"] 
elapsed_time = [time-times[0] for time in times] 
plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1)) 

times = birddata.timestamp[birddata.bird_name == "Sanne"] 
elapsed_time = [time-times[40916] for time in times] 
plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1)) 

times = birddata.timestamp[birddata.bird_name == "Nico"] 
elapsed_time = [time-times[19795] for time in times] 
plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1)) 

plt.xlabel(" Observation ") 
plt.ylabel(" Elapsed time (days) ") 
plt.legend(('Eric', 'Sanne', 'Nico')) 

plt.show() 
