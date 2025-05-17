import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x_points = []
    y_points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    p = 2 * dy - dx
    y = y1
    y_step = 1 if y1 < y2 else -1
    
    for x in range(x1, x2 + 1):
        if steep:
            x_points.append(y)
            y_points.append(x)
        else:
            x_points.append(x)
            y_points.append(y)
        
        if p >= 0:
            y += y_step
            p -= 2 * dx
        p += 2 * dy
    
    return x_points, y_points

# Taking input from user
xstart = int(input("Enter x1: "))
ystart = int(input("Enter y1: "))
xend = int(input("Enter x2: "))
yend = int(input("Enter y2: "))

# Get points of the line
x_coords, y_coords = bresenham_line(xstart, ystart, xend, yend)

# Plot the line
plt.figure(figsize=(6, 4))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='green')
plt.title("Bresenham's Line Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

print(x_coords)
print(y_coords)
plt.show()
