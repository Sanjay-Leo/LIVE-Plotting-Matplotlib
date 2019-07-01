
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')  #  styling sheet that tries to replicate the styles from 'FiveThrityEight.com'
fig1 = plt.figure()   # to create a figure object to pull out size of frame

ax1 = fig1.add_subplot(1,1,1)   # it means 1x1 grid and last 1 is (first subplot) 

def animate(p):
    plot_data = open('test.csv', 'r').read()
    line_data = plot_data.split('\n')

    x1 = []
    y1 = []

    for line in line_data:
        if len(line) > 1:
            x,y = line.split(',')
            x1.append(x)
            y1.append(y)

        ax1.clear()
        ax1.plot(x1,y1)

anime_data = animation.FuncAnimation(fig1, animate, interval= 500)
plt.show()


