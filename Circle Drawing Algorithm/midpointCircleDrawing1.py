import matplotlib.pyplot as plt

def midpointCircleDrawingAlgo(xc, yc, r):
    
    d = 1 - r
    x = 0
    y = r
    
    points = [(x, y)]
    
    print(f"x = {x}, y = {y}, d = {d}")
    
    while y >= x :
        
        if d < 0 :
            d = d + 2*x + 3
        else :
            d = d + 2*(x - y) + 5
            y = y - 1
            
        x = x + 1
    
        print(f"x = {x}, y = {y}, d = {d}")
            
        points.extend([(xc+x, yc+y), (xc-x, yc+y), (xc+x, yc-y), (xc-x, yc-y), 
                       (xc+y, yc+x), (xc-y, yc+x), (xc+y, yc-x), (xc-y, yc-x)])
        
    return points
        

        
        

if __name__ == '__main__':
    
    xc = int(input("Enter the x-coordinate of center: "))
    yc = int(input("Enter the y-coordinate of center: "))
    r = int(input("Enter the radius of the circle: "))
    
    circle_points = midpointCircleDrawingAlgo(xc, yc, r)
    
    x_values = [point[0] for point in circle_points]
    y_values = [point[1] for point in circle_points]

    plt.scatter(x_values, y_values)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
