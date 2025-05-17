import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, x_points, y_points):
    # Circle এর সব অষ্টাংশে পয়েন্ট যোগ করি
    x_points.extend([ xc+x, xc-x, xc+x, xc-x, xc+y, xc-y, xc+y, xc-y ])
    y_points.extend([ yc+y, yc+y, yc-y, yc-y, yc+x, yc+x, yc-x, yc-x ])

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r

    x_points = []
    y_points = []

    plot_circle_points(xc, yc, x, y, x_points, y_points)

    while x <= y:
        x += 1
        if p < 0:
            p = p + 4*x + 6
        else:
            y -= 1
            p = p + 4*(x - y) + 10

        plot_circle_points(xc, yc, x, y, x_points, y_points)

    return x_points, y_points

# Taking input from user
xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
r = int(input("Enter radius: "))

# Drawing the circle
x_coords, y_coords = bresenham_circle(xc, yc, r)

# Plotting the circle
plt.figure(figsize=(6,6))
plt.scatter(x_coords, y_coords, color='blue')
plt.title("Bresenham's Circle Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
# plt.gca().set_aspect('equal', adjustable='box')
plt.gca()
plt.show()
