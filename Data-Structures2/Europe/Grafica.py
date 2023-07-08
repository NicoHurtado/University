import matplotlib.pyplot as plt

algorithms = []
times = []

with open('output.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[:4]:
        times.append(float(line))
    for line in lines[4:]:
        algorithms.append(line.strip())

print(times)
print(algorithms)

plt.plot(algorithms, times)
plt.title('Algorithms vs Times')
plt.xlabel('Algorithms')
plt.ylabel('Times (ms)')
plt.savefig('AlgorithmsPlot.png')
