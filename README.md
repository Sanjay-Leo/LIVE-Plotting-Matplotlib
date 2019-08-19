# LIVE-Plotting-Matplotlib
User have to add values to the CSV file to see live Plotting working

### Example:
After importing the required libraries and defining `matplotlib.animation` we 
will declared `animation.FuncAnimation` to animate the graph
```
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

```
> **you should observe this in the cell output ( the graph will animate according to
the values added in plot.csv )**

![alt text](https://user-images.githubusercontent.com/51887422/63293935-c0894900-c2e6-11e9-9738-b3761026eda4.JPG)

> **Make sure you addup the values in plot.csv**
