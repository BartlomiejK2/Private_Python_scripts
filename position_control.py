import asyncio
import math
import moteus
import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
import time
frequency = 200
t = 10
n = t*frequency
time_s = np.empty(3)
position_vector = np.empty(n)
velocity_vector = np.empty(n)
torque_vector = np.empty(n)
Q_current_vector = np.empty(n)
D_current_vector = np.empty(n)
temperature_vector = np.empty(n)
x = np.linspace(0,n,n)
async def main():
    time_s[0] = time.perf_counter()
    c1 = moteus.Controller(id=1)
    await c1.set_stop()
    i = 0
    state = await c1.set_position(position=math.nan, query=True)
    startPos = state.values[moteus.Register.POSITION]
    time_s[1] = time.perf_counter() - time_s[0]
    while i < n:
        current_time = time.perf_counter()
        state = await c1.set_position(position = 15*math.sin(i/500*math.pi)+startPos, query=True)
        position_vector[i] = state.values[moteus.Register.POSITION]
        velocity_vector[i] = state.values[moteus.Register.VELOCITY]EWS`
        torque_vector[i] = state.values[moteus.Register.TORQUE]
        while(time.perf_counter()-current_time <(1/frequency)):
            pass
        #await asyncio.sleep(0.00001)
        i += 1
asyncio.run(main())
print("Koniec")
time_s[2] = time.perf_counter()
time_elapsed = time_s[2] - time_s[1]
print()
print("Czas działania: "+time_elapsed)
file = open("Pomiary z moteusa.txt","w")
file.write("Pozycja:\tPrędkość\tMoment:\tQ_natezenie:\t"
           "D_natezenie:\tTemperatura:\n")
i = 0
while i < n:
    file.write(position_vector[i]+ "\t" +velocity_vector[i]+ "\t" +torque_vector[i]+ "\t"+Q_current_vector[i] +"\t"
               + D_current_vector[i] + "\t" + temperature_vector[i] +"\n")
    i += 1
file.close()
plt.plot(x, position_vector)
plt.show()




