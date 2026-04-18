import sqlite3
import numpy as np

def calculate_nrmse(original, simulated):
    """
    Original data aur simulated data ke beech Normalized Root Mean Square Error nikalta hai.
    """
    mse = np.mean((original - simulated) ** 2)
    rmse = np.sqrt(mse)
    nrmse = rmse / (np.max(original) - np.min(original))
    return nrmse

def validate_db_results(db_name='parametric_results/simulations.db', threshold=0.05):
    """
    Database se data uthakar check karta hai ki koi result abnormal toh nahi hai.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT permittivity, peak_amplitude FROM results")
    rows = cursor.fetchall()
    
    print("\n--- ✅ Quality Validation Report ---")
    is_valid = True
    for eps, peak in rows:
        if peak < 0.001: 
            print(f"⚠️ Warning: Low signal strength detected for Eps {eps}")
            is_valid = False
        else:
            print(f"✔️ Eps {eps}: Peak {peak:.4f} is within acceptable range.")
            
    conn.close()
    return is_valid

if __name__ == "__main__":
    # Test validation
    validate_db_results()
