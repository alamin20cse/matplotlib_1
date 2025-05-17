import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            x_points.append(x)
            y_points.append(y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            x_points.append(x)
            y_points.append(y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    # Add final point
    x_points.append(x)
    y_points.append(y)

    return x_points, y_points

# ✅ Input from user
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# ✅ Call algorithm
x_vals, y_vals = bresenham_line(x1, y1, x2, y2)

# ✅ Plot using matplotlib
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='o', color='green')
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.show()
