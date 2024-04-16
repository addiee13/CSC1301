from matplotlib import pyplot as plt
x = list(range(24))
y = [45, 44, 43, 43, 42, 42, 41, 41, 42, 45, 48, 50, 52, 53, 54, 55, 55, 54, 52, 50, 49, 48, 47, 46]
plt.plot(x, y, 'r-')
plt.grid(True)
plt.title("Temperature in Atlanta")
plt.xticks(x)
plt.xlabel("Time of the day")
plt.ylabel("Temperature")
plt.show()