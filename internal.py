import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from gprMax.tools.output_stats import get_output_data # gprMax ka built-in tool

# Simulation Settings
base_input_file = 'user_model.in'
permittivity_values = [3.0, 5.0, 8.0]
output_dir = 'parametric_results'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def run_simulation(eps_value):
    new_filename = f"model_eps_{eps_value}.in"
    with open(base_input_file, 'r') as f:
        content = f.read()
    
    updated_content = content.replace('MATERIAL_EPS', str(eps_value))
    
    with open(new_filename, 'w') as f:
        f.write(updated_content)
    
    print(f"🚀 Running simulation for Eps: {eps_value}...")
    subprocess.run(['python', '-m', 'gprMax', new_filename, '-n', '1'], check=True)
    
    output_file = new_filename.replace('.in', '.out')
    rx_data = get_output_data(output_file, 1, 'Ez') 
    
    os.remove(new_filename) 
    
    return rx_data

plt.figure(figsize=(12, 6))

for eps in permittivity_values:
    data = run_simulation(eps)
    plt.plot(data, label=f'Permittivity: {eps}')

plt.title('GPR Signal Comparison: Effect of Soil Permittivity')
plt.xlabel('Time Steps')
plt.ylabel('Amplitude (V/m)')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'comparison_analysis.png'))
print(f"\n📊 Analysis graph saved in {output_dir}/")
plt.show()