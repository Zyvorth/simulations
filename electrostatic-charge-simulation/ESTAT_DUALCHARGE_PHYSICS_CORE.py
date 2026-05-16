import secrets#to randomly place the particle in the plane
import math
radius=6 
window_len_x=1400
window_len_y=780
mass=10
ESTAT_const=1000000#not the actual constant , but a value chosen for visual appeal of the simulation
charge_inst=[]
def charge_initial(a,b):
  for i in range(max([a,b])):
    if i<a:
     x=secrets.randbelow(window_len_x-radius+1)+radius
     y=secrets.randbelow(window_len_y-radius+1)+radius
     charge_inst.append([x,y,0,0,1])
    if i<b:
     x=secrets.randbelow(window_len_x-radius+1)+radius
     y=secrets.randbelow(window_len_y-radius+1)+radius
     charge_inst.append([x,y,0,0,-1])
def charge_pos_inst():
  charge_inst_copy=charge_inst.copy()
  for i in range(len(charge_inst)):
    x_new=0
    y_new=0
    vx_new=0
    vy_new=0
    a_eff_x=0
    a_eff_y=0
    a_eff=0
    for j in range(len(charge_inst)):
      if i==j:
        continue # to prevent huge spike in effective acceleration(still i have not neglected such scenarios)
      else:
        inst_dist=((charge_inst_copy[j][0]-charge_inst_copy[i][0])**2)+((charge_inst_copy[j][1]-charge_inst_copy[i][1])**2)
        inst_slope_x=(charge_inst_copy[j][0]-charge_inst_copy[i][0])
        inst_slope_y=(charge_inst_copy[j][1]-charge_inst_copy[i][1])
        inst_theta=math.atan2(inst_slope_y,inst_slope_x)
        cos_theta=math.cos(inst_theta)
        sin_theta=math.sin(inst_theta) 
        if inst_dist==0:
          continue
        else:
          a_eff=abs(((ESTAT_const*charge_inst_copy[j][4]*charge_inst_copy[i][4])/inst_dist)/mass)
          if charge_inst_copy[j][4]*charge_inst_copy[i][4]>0: 
            a_eff_x-=(a_eff*cos_theta)# Resolve acceleration into x and y components
            a_eff_y-=(a_eff*sin_theta)
          else:
            a_eff_x+=(a_eff*cos_theta)# Resolve acceleration into x and y components
            a_eff_y+=(a_eff*sin_theta)
            
    x_new=charge_inst_copy[i][0]+((charge_inst_copy[i][2]*(1/250))+((1/2)*a_eff_x*((1/250)**2)))
    vx_new=(charge_inst_copy[i][2]+a_eff_x*(1/250))
    if x_new<radius:
      x_new=radius
      vx_new *= -1#this reverses the direction of velocity when in contact with the boundary
    elif x_new>(window_len_x-radius):
      x_new=window_len_x-radius
      vx_new *= -1
    y_new=charge_inst_copy[i][1]+((charge_inst[i][3]*(1/250))+((1/2)*a_eff_y*((1/250)**2)))
    vy_new=(charge_inst[i][3]+a_eff_y*(1/250))
    if y_new<radius:
      y_new=radius
      vy_new *= -1
    elif y_new>(window_len_y-radius):
      y_new=window_len_y-radius
      vy_new *= -1
    charge_inst[i][0]=x_new
    charge_inst[i][1]=y_new
    charge_inst[i][2]=vx_new
    charge_inst[i][3]=vy_new

