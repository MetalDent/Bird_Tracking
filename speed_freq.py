import pandas as pa
import matplotlib.pyplot as plt 
import numpy as np 
  
birddata = pa.read_csv("bird_tracking.csv") 
bird_names = pa.unique(birddata.bird_name)  

# For Eric 
ix = birddata.bird_name == "Eric" 
speed = birddata.speed_2d[ix] 
  
plt.figure(figsize = (8,4)) 
ind = np.isnan(speed) 
plt.hist(speed[~ind], bins = np.linspace(0,30,20), normed=True) 
plt.xlabel(" 2D speed (m/s) ") 
plt.ylabel(" Frequency ") 
plt.title("Eric")

# For Sanne
ix = birddata.bird_name == "Sanne" 
speed = birddata.speed_2d[ix] 
  
plt.figure(figsize = (8,4)) 
ind = np.isnan(speed) 
plt.hist(speed[~ind], bins = np.linspace(0,30,20), normed=True) 
plt.xlabel(" 2D speed (m/s) ") 
plt.ylabel(" Frequency ") 
plt.title("Sanne")

# For Nico
ix = birddata.bird_name == "Nico" 
speed = birddata.speed_2d[ix] 
  
plt.figure(figsize = (8,4)) 
ind = np.isnan(speed) 
plt.hist(speed[~ind], bins = np.linspace(0,30,20), normed=True) 
plt.xlabel(" 2D speed (m/s) ") 
plt.ylabel(" Frequency ") 
plt.title("Nico")

plt.show() 