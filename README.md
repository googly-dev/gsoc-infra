# gsoc-infra
# 🛰️ GPR Parametric Automation Framework

A collaborative research tool developed by **@pratiktech28** and **@googly-dev** to automate gprMax simulations, perform physics-based analytics, and manage data via SQL.

## 🚀 Overview
This framework automates the entire lifecycle of a Ground Penetrating Radar (GPR) parametric study. It allows users to sweep through various material properties (like permittivity) and automatically captures the signal behavior, arrival times, and peak amplitudes into a relational database.

## ✨ Key Features
- **Automated Execution:** Headless gprMax simulation runs with dynamic `.in` file generation.
- **Physics Analytics:** Real-time extraction of wave velocity shifts and signal attenuation.
- **Data Persistence:** Relational storage of all simulation metadata using SQLite.
- **Visual Synthesis:** Automated generation of comparative A-scan plots with residual analysis.

## 🛠️ Setup & Usage
1. **Prerequisites:** - Python 3.x
   - gprMax installed in your environment.
   - NumPy & Matplotlib.

2. **Run the Pipeline:**
   ```bash
   python main.py

   Check Results:

View the database: sqlite3 parametric_results/simulations.db

View the plot: parametric_results/analysis_plot.png

🤝 Contribution
This project is part of a collaborative effort to build robust GSoC infrastructure.

Co-authored-by: @googly-dev


---

### **2. `schema.sql` (Database Structure)

```sql
-- Database Schema for GPR Simulation Results
-- Created by @pratiktech28 & @googly-dev

CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    permittivity REAL NOT NULL,        -- Relative permittivity of the material
    peak_amplitude REAL NOT NULL,      -- Max amplitude of the Ez component
    arrival_time REAL NOT NULL,        -- Time of flight (seconds)
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Index for faster querying by permittivity
CREATE INDEX IF NOT EXISTS idx_permittivity ON results(permittivity);
