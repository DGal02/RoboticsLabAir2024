from scipy.optimize import minimize
import numpy as np
from scipy import integrate
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

def cost_function(x,ref_solution):
  # x are optimized parameters (km, kt)
  est_solution = integrate.solve_ivp(solve_dynamics,[time_vec[0],time_vec[-1]],[0,0],t_eval=time_vec,args=(x[0],x[1],m,c,input,sim_dt))
  return np.sum((est_solution.y[0,:] - ref_solution.y[0,:])**2)

# initial guess
km1=0.9
kt1=30
init_guess = [km1,kt1]

# TODO
# Use minimize method. Provide cost function, initial guess and args=(ref_solution)
opt_params = minimize(cost_function,init_guess,args = (ref_solution),method='BFGS',options={'gtol': 1e-6, 'disp': True})
print(opt_params.x)

# Generate output with optimal parameters and plot the result
my_solution = integrate.solve_ivp(solve_dynamics,[time_vec[0],time_vec[-1]],[0,0],t_eval=time_vec,args=(opt_params.x[0],opt_params.x[1],m,c,input,sim_dt))
plt.plot(time_vec,abs(my_solution.y[0,:]))
plt.plot(time_vec,abs(ref_solution.y[0,:]))
plt.xlabel('Time [s]')
plt.ylabel('Enlongation [m]')
plt.legend(['Estimated response', 'Reference response'])
plt.show()