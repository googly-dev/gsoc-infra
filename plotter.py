import matplotlib.pyplot as plt
import os

def plot_gpr_results(data_dict, output_path='parametric_results/analysis.png'):
    """
    Har permittivity value ke liye compare karke graph banata hai.
    """
    plt.figure(figsize=(12, 6))
    for label, data in data_dict.items():
        plt.plot(data, label=f'Eps: {label}')
    
    plt.title('GPR Signal Analysis - Parametric Sweep')
    plt.xlabel('Time Steps')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Folder check aur save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"📈 Graph successfully saved at: {output_path}")
