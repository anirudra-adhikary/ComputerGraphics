from matplotlib import pyplot as plt

def DDA(x0, y0, x1, y1):
    
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    
    steps = max(dx, dy)
    
    xinc = dx/steps
    yinc = dy/steps
    
    x = x0
    y = y0
    
    x_corrdinates = []
    y_corrdinates = []
    
    for i in range(steps):
        
        print("({}, {})".format(x, y))
        x_corrdinates.append(x)
        y_corrdinates.append(y)
        
        x = round(x + xinc)
        y = round(y + yinc)
        
        
    plt.plot(x_corrdinates, y_corrdinates, marker='o', markersize=1, markerfacecolor="green")
    plt.show()
    
if __name__ == '__main__':
    
    x0, y0 = 5, 10
    x1, y1 = 20, 30
    
    DDA(x0, y0, x1, y1)