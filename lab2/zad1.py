from scipy import integrate
import numpy as np
from matplotlib import pyplot as plt
km = 0.1
kt = 100
m = 0.005
c =  2
input_duration = 0.01
input_amplitude = 1
sim_dt = 0.0001
sim_time = 0.1
time_vec = np.arange(0,sim_time,sim_dt)

def generate_pulse(time_vector, pulse_duration, amplitude,sim_dt):
  pulse = amplitude * np.sin(np.pi * time_vector / (pulse_duration))
  pulse[int(pulse_duration/sim_dt)::]=0
  return pulse

def solve_dynamics(t,X,km,kt,m,c,active_force,sim_dt):
  ln, dln_dt =  X # lm - enlongation, dlm_dt - enlongation speed
  d2ln_dt = 1/m*(-c*dln_dt-km*ln-kt*ln-active_force[int(t/sim_dt)])
  return [dln_dt,d2ln_dt]

x0 = [0,0] # initial values - ln0, dln_dt0
input = generate_pulse(time_vec,input_duration,input_amplitude,sim_dt) # input pulse

# TODO
ref_solution = integrate.solve_ivp(solve_dynamics, [time_vec[0], time_vec[-1]], x0, args=(km, kt, m, c, input, sim_dt), t_eval=time_vec)
plt.plot(time_vec,abs(ref_solution.y[0,:])) # plot resulting ln
plt.xlabel('Time [s]')
plt.ylabel('Enlongation [m]')
plt.show()