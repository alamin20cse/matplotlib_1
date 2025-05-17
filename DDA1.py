import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    # dx, dy হিসাব
    dx = x2 - x1
    dy = y2 - y1

    # স্টেপ নির্ধারণ
    steps = int(max(abs(dx), abs(dy)))

    # প্রতি স্টেপে ইনক্রিমেন্ট
    Xinc = dx / steps
    Yinc = dy / steps

    # প্রথম পয়েন্ট
    x = x1
    y = y1

    # পয়েন্টগুলো স্টোর করবো
    x_points = []
    y_points = []

    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += Xinc
        y += Yinc

    return x_points, y_points

# ✅ ইউজার ইনপুট নেওয়া
x_start = int(input("Enter x1: "))
y_start = int(input("Enter y1: "))
x_end = int(input("Enter x2: "))
y_end = int(input("Enter y2: "))

# DDA কল
x_vals, y_vals = dda_line(x_start, y_start, x_end, y_end)

# ✅ চিত্র আঁকা
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='o', color='blue')
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.show()
