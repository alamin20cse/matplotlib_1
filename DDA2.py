import matplotlib.pyplot as plt
import numpy as np

def dda_line(x1, y1, x2, y2):
    """DDA Line Drawing Algorithm"""
    points = []
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate steps needed for generating pixels
    steps = max(abs(dx), abs(dy))
    
    # Calculate increment in x & y for each step
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Start with the first point
    x = x1
    y = y1
    points.append((round(x), round(y)))
    
    # For every step, find the next pixel position
    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))
    
    return points

def plot_line(points, x1, y1, x2, y2):
    """Plot the line using matplotlib"""
    # Unzip the points into x and y coordinates
    x_coords, y_coords = zip(*points)
    
    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, 'bo-', linewidth=2, markersize=8)
    plt.title(f"DDA Line Drawing Algorithm: ({x1},{y1}) to ({x2},{y2})")
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # Set equal scaling for both axes
    plt.axis('equal')
    plt.show()

def main():
    print("DDA Line Drawing Algorithm")
    
    # Get user input
    try:
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
    except ValueError:
        print("Please enter integer values only.")
        return
    
    # Generate points using DDA algorithm
    points = dda_line(x1, y1, x2, y2)
    
    # Print the points
    print("\nPoints on the line:")
    for point in points:
        print(point)
    
    # Plot the line
    plot_line(points, x1, y1, x2, y2)

if __name__ == "__main__":
    main()