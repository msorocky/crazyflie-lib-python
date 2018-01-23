import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ScopeAddGyro (object):
    def __init__(self,ax1,ax2,ax3):
        self.ax1 = ax1
        self.ax2 = ax2
        self.ax3 = ax3
        timescale = 0
        gx = 0
        gy = 0
        gz = 0
        self.ax1.plot(timescale,gx)
        self.ax2.plot(timescale,gy)
        self.ax3.plot(timescale,gz)

    def update(self,dummy):
	    graph_data = open('Gyrotest.txt','r').read()
	    lines = graph_data.split('\n')
	    timescale = []
	    gx = []
	    gy = []
	    gz = []
	    j=1

	    print(len(lines))
	    for line in lines:
	    	print(line)
	        if len(lines)-6 > j:
	            print(j)
	            j=j+1
	            continue
	        if len(line) > 3:
	            sensortype, ts, x, y, z = line.split(',')
	            if sensortype == 'Gyroscope':
		            timescale.append(ts)
		            gx.append(x)
		            gy.append(y)
		            gz.append(z)
	        j=j+1
	    self.ax1.clear()
	    self.ax2.clear()
	    self.ax3.clear()
	    self.ax1.plot(timescale,gx)
	    self.ax2.plot(timescale,gy)
	    self.ax3.plot(timescale,gz)


if __name__ == '__main__':
	fig = plt.figure()
	axRow = fig.add_subplot(3,1,1)
	axPitch = fig.add_subplot(3,1,2)
	axYaw = fig.add_subplot(3,1,3)
	animate = ScopeAddGyro(axRow,axPitch,axYaw)
	ani = animation.FuncAnimation(fig, animate.update, interval=100)
	plt.show()