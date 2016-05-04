import math
import matplotlib.pyplot as plt
import numpy as np      
from matplotlib import animation   
 
#calculate the trajectory
def Trajectory(v,theta,B,T0,choice):
    v_x=v * math.cos(theta * math.pi/180)
    v_y=v * math.sin(theta * math.pi/180)
    dt,y0,a,alpha=0.005,10**4,6.5*10**(-3),2.5
    x,y,t=0,0,0
    distance=[[]for i in range(3)]
    distance[0].append(x)
    distance[1].append(y)
    if choice<0:            #negative for isothermal approximation
        def rho(height):
            return math.exp(-height/y0)
    else:                   #non-negative for adiabatic approximation
        def rho(height):
            return (1-a*height/T0)**alpha
    while y>= 0:
        a_x3, a_y3=-B*rho(y)*v*v_x,-9.8-B*rho(y)*v*v_y
        x=x+v_x*dt
        v_x=v_x+a_x3*dt
        y=y+v_y*dt
        v_y=v_y+a_y3*dt
        t=t+dt
        v=(v_x**2+v_y**2)**0.5
        distance[0].append(x/1000)   #divided by 1000 to change the unit from "meter" to "kilometer"
        distance[1].append(y/1000)
    distance[2].append(t)
    return distance

#plot the figure for isothermal case
velocity=700
B=4*10**(-5)
T0=300
plt.subplot(1,2,1)
for i in range(7):
    angle=i*5+30
    d=Trajectory(velocity,angle,B,T0,-1)
    plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label=angle)
    print angle,d[0][-1],d[2][0]    
plt.grid(True,color='k')
plt.title('Cannon Trajectory')
plt.text(30,6,'Isothermal',fontsize=15)
plt.text(30,5,'v0=700m/s')
plt.xlabel('Horizon Distance x(km)')
plt.ylabel('Vertical Distance y(km)')
plt.xlim(0,50)
plt.ylim(0,14)
plt.legend()

#plot for adiabatic case
plt.subplot(1,2,2)
for i in range(7):
    angle=i*5+30
    d=Trajectory(velocity,angle,B,T0,1)
    plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label=angle)
    print angle,d[0][-1],d[2][0]   
plt.grid(True,color='k')
plt.title('Cannon Trajectory')
plt.text(30,6,'Adiabatic',fontsize=15)
plt.text(30,5,'v0=700m/s')
plt.xlabel('Horizon Distance x(km)')
plt.ylabel('Vertical Distance y(km)')
plt.xlim(0,50)
plt.ylim(0,14)
plt.legend()
plt.show()


#动图，Isothermal情况下各个角度的扫描，标记角度和射程，最远距离尚未完成
# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(0, 35), ylim=(0,18))
line, = ax.plot([], [], lw=2)  
plt.title('Cannon Trajectory of Isothermal Approximation')
plt.xlabel('Horizon Distance x(km)')
plt.ylabel('Vertical Distance y(km)')
plt.grid(True,color='k')
note = ax.text(18,12,'',fontsize=15)
# initialization function: plot the background of each frame
def init():  
    line.set_data([], []) 
    note.set_text('')  
    return line,note
# animation function.  this is called sequentially   
def animate(j):
    dis=Trajectory(700,j,4*10**(-5),300,-1) 
    x = dis[0]  
    y = dis[1]
    line.set_data(x, y) 
    note.set_text('initial speed:700m/s \n'+'firing angle: %d'%j + r'$^{\circ}$'+ '\ndistance:%s'%dis[0][-1] + 'km')
    return line,note

anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=91, interval=5, blit=True)  
plt.show()  


