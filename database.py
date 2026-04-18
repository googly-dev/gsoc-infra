import sqlite3
import os

def init_db(db_name='parametric_results/simulations.db'):
    """Database aur Table banata hai agar nahi hai toh."""
    os.makedirs(os.path.dirname(db_name), exist_ok=True)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Table structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            permittivity REAL,
            peak_amplitude REAL,
            arrival_time REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_result(eps, peak, arrival, db_name='parametric_results/simulations.db'):
    """Ek single simulation ka data SQL mein save karta hai."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO results (permittivity, peak_amplitude, arrival_time)
        VALUES (?, ?, ?)
    ''', (eps, peak, arrival))
    conn.commit()
    conn.close()
    print(f"🗄️ Data for Eps {eps} saved to SQLite database.")
