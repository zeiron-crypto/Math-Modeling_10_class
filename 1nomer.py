c=2997924581.2
a=pi/3
ei=300
h=100
G=6.672041×10**-11
m=0.910953447×10**-30
R=1.09737317783×10**-7
k=1.380649*10**−23 
z=376.73
v=22.41396954*10**−3
b=30
g=10
T=200
hl=6,6*10**-34

fig = plt.figure()
bodys = []

for i in range (0, len(t), 1):
    body1, = plt.plot(so[:i, 0], sol[:i, 2], '-', color ='r')
    body1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color = 'r')
    
    body2, = plt.plot(so[:i,4], sol[:i,6], '-', color ='g')
    body2_line, = plt.plot(sol[i,4], sol[i, 6], 'o', color = 'g')
     
    body3, = plt.plot(so[:i,8], sol[:i,10], '-', color ='b') 10
    body3_line, = plt.plot(sol[i,8], sol[i,10], 'o', color = 'b')
    
    bodys.append([body1, body1_line, body2, body2_line, body3, body3_line])
    
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('N_body_G+K.gif')
    
