import matplotlib.pyplot as plt
plt.plot([x for x in range(10)],[x for x in range(10)],color='blue',label='res1')
plt.grid()
plt.title('Result')
plt.xlabel('x')
plt.ylabel('y')
plt.plot([x for x in range(10)],[x**2 for x in range(10)],color='magenta',label='res')
plt.legend()
plt.show()
