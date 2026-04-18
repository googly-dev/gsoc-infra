import numpy as np

def analyze_signal_propagation(data_dict, time_step):
    """
    Har permittivity value ke liye signal ki 'Health' aur 'Speed' calculate karta hai.
    """
    report = {}
    
    print("\n--- 📊 Physics Analytics Report ---")
    for eps, signal in data_dict.items():
        peak_val = np.max(np.abs(signal))
        
        arrival_index = np.argmax(np.abs(signal))
        arrival_time = arrival_index * time_step
        
        report[eps] = {
            "peak": peak_val,
            "arrival": arrival_time
        }
        
        print(f"Eps {eps}: Peak = {peak_val:.4f} V/m | Arrival Time = {arrival_time:.2e} s")
    
    return report

def log_summary(report, file_path='parametric_results/summary.txt'):
    """
    Results ko ek text file mein save karta hai taaki PR mein chipka sako.
    """
    with open(file_path, 'w') as f:
        f.write("Simulation Summary Report\n")
        f.write("=========================\n")
        for eps, stats in report.items():
            f.write(f"Permittivity {eps}: Peak Amp: {stats['peak']:.4f}, Arrival: {stats['arrival']:.2e}\n")
    print(f"\n📝 Summary saved to {file_path}")
