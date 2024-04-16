import matplotlib.pyplot as plt
import random
x_chords = [random.randint(1,100) for i in range(100)]
plt.pie(x_chords)
print(x_chords)
plt.show()