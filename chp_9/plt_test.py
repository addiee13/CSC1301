import matplotlib.pyplot as plt
x_axis =[0,1,2,3]
y_axis = [3,4,5,8]
plt.title("Test Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.xticks(x_axis)
plt.grid(True)
plt.plot(x_axis, y_axis)
plt.show()