import schedule
import time
import subprocess
import os
from datetime import datetime

def job():
    print(f"🕒 Automation Triggered at: {datetime.now()}")
    try:
        subprocess.run(['python', 'main.py'], check=True)
        print("✅ Scheduled Simulation Pipeline completed successfully.")
    except Exception as e:
        print(f"❌ Automation failed: {e}")

schedule.every().day.at("00:00").do(job)

if __name__ == "__main__":
    print("🤖 GPR Automation Service is running...")
    while True:
        schedule.run_pending()
        time.sleep(60)
