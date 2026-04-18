import database
import analytics
def main():
    # 1. Database setup karo
    database.init_db()
    
    sample_data = {3.0: [0.1, 0.5, 0.2], 5.0: [0.08, 0.4, 0.15]} 
    dt = 1.0e-11 
    
    report = analytics.analyze_signal_propagation(sample_data, dt)
    
    for eps, stats in report.items():
        database.save_result(eps, stats['peak'], stats['arrival'])
    
    print("\n✅ Full Pipeline Executed: Simulation -> Analytics -> Database")

if __name__ == "__main__":
    main()
