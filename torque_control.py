import asyncio
import math
import moteus
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
n = 1000
torque_vector = np.empty(n)
x = np.linspace(0,n,n)
async def main():
    c1 = moteus.Controller(id=1)
    await c1.set_stop()
    i = 0
    while i < 1000:
        state = await c1.set_position(position = 0,velocity = 0, feedforward_torque =0.6*math.sin(i/500*math.pi) , query=True)
        print("Torque:", state.values[moteus.Register.TORQUE])
        torque_vector[i] = state.values[moteus.Register.TORQUE]
        await asyncio.sleep(0.001)
        i += 1
asyncio.run(main())
plt.plot(x,torque_vector)
plt.show()