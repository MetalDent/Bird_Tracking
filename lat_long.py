import pandas as pa
import matplotlib.pyplot as plt 
import numpy as np 
  
  
birddata = pa.read_csv("bird_tracking.csv") 
bird_names = pa.unique(birddata.bird_name)  

ix = birddata.bird_name == "Nico" 
x,y = birddata.longitude[ix], birddata.latitude[ix] 
plt.figure(figsize = (7,7)) 
plt.title("Nico")
plt.plot(x,y,"b.") 

ix = birddata.bird_name == "Eric" 
x,y = birddata.longitude[ix], birddata.latitude[ix] 
plt.figure(figsize = (7,7)) 
plt.title("Eric")
plt.plot(x,y,"b.") 

ix = birddata.bird_name == "Sanne" 
x,y = birddata.longitude[ix], birddata.latitude[ix] 
plt.figure(figsize = (7,7)) 
plt.title("Sanne")
plt.plot(x,y,"b.") 
  
plt.figure(figsize = (7,7)) 
for bird_name in bird_names: 
    ix = birddata.bird_name == bird_name   
    x,y = birddata.longitude[ix], birddata.latitude[ix] 
    plt.plot(x,y,".", label=bird_name) 
plt.xlabel("Longitude") 
plt.ylabel("Latitude") 
plt.legend(loc="lower right") 
plt.title("Trajectories of all three birds")
plt.show() 