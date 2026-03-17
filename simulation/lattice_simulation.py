import numpy as np
import matplotlib.pyplot as plt

N = 9
phases = np.random.rand(N) * 2 * np.pi

K = 0.5
dt = 0.05

history = []

for t in range(500):
    new_phases = phases.copy()

    for i in range(N):
        coupling = 0
        for j in range(N):
            if i != j:
                coupling += np.sin(phases[j] - phases[i])

        new_phases[i] += dt * K * coupling

    phases = new_phases
    history.append(phases.copy())

history = np.array(history)

plt.plot(history)
plt.title("Tolog-Alpha oscillator phases")
plt.xlabel("time")
plt.ylabel("phase")
plt.show()