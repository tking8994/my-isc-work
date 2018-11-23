import matplotlib.pyplot as plt
time=[0,1,2,3,4,5,6]
c02=[250,265,272,260,300,320,389]
temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]
plt.plot(time,c02, '--b')
ax1=ax1.set_ylabel(C02)
ax2=ax1.twinx()
ax2.se
plt.plot(time,temp,'r')
plt.title("Figure 1")
plt.xlabel("time")
plt.ylabel("C02")
plt.legend()
#plt.show()
