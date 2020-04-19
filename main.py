import numpy as np
import matplotlib.pyplot as plt
from qutip import *
import imageio



def animate_bloch(states, duration=0.1):

    b = Bloch()
    b.zlabel=['z', '-z'] 
    images=[] 
    for i in range(len(states)):
        b.clear()
        b.add_states(states[i])
        b.save('temp_file.png')
        images.append(imageio.imread('temp_file.png'))
    imageio.mimsave('bloch_anim.gif', images, duration=duration)
    

def Vector_States(xy_comp , z_comp):
        
    states = []
    
    for i in range (0,len(Mxy)-5):
        states.append((xy_comp[i]*basis(2,1) + z_comp[i+5]*basis(2,0)).unit())
    
    animate_bloch(states, duration=0.1)
    
    
#plotting vectors
t = np.linspace(0, 1000, 50)

#Assume we are dealling with gray matter so
#T1 = 925ms , T2= 100ms , M0=1mT
Mxy = np.exp(-t/100)

plt.figure()
plt.plot(t, Mxy)
plt.xlabel('t (ms)')
plt.ylabel('Mxy (mT)')

Mz = np.sqrt(1-Mxy**2)
plt.figure()
plt.plot(t, Mz)
plt.xlabel('t (ms)')
plt.ylabel('Mz (mT)')

plt.show()


Vector_States(Mxy , Mz)    
    