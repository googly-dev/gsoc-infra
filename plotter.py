import matplotlib.pyplot as plt
import os
import numpy as np

def plot_gpr_results(data_dict, output_path='parametric_results/analysis.png'):
    """
    Comparison aur Residual (Difference) analysis ke saath graph banata hai.
    """
    keys = list(data_dict.keys())
    base_eps = keys[0]
    base_signal = data_dict[base_eps]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    for label, data in data_dict.items():
        ax1.plot(data, label=f'Eps: {label}')
    
    ax1.set_title('GPR Signal Analysis - Parametric Sweep', fontsize=14)
    ax1.set_ylabel('Amplitude (V/m)')
    ax1.legend(loc='upper right')
    ax1.grid(True, linestyle='--', alpha=0.5)

    for label in keys[1:]: 
        residual = data_dict[label] - base_signal
        ax2.plot(residual, label=f'Diff (Eps {label} - {base_eps})', alpha=0.7)
    
    ax2.set_title('Signal Residuals (Deviation from Base Case)', fontsize=12)
    ax2.set_xlabel('Time Steps')
    ax2.set_ylabel('Delta Amplitude')
    ax2.legend(loc='upper right')
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"📈 Advanced Analysis Graph saved at: {output_path}")
