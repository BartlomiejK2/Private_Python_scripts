import asyncio
import math
import moteus
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
n = 1000
velocity_vector = np.empty(n)
x = np.linspace(0,n,n)
async def main():
    c1 = moteus.Controller(id=1)
    await c1.set_stop()
    i = 0
    while i < 1000:
        state = await c1.set_position(position = math.nan,velocity = 15*math.sin(i/500*math.pi) , query=True)
        print("Velocity:", state.values[moteus.Register.VELOCITY])
        velocity_vector[i] = state.values[moteus.Register.VELOCITY]
        print()
        await asyncio.sleep(0.001)
        i += 1
asyncio.run(main())
plt.plot(x,velocity_vector)
plt.show()