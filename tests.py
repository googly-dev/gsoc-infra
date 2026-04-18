import unittest
import os
import sqlite3
import numpy as np
import database
import analytics

class TestGPRFramework(unittest.TestCase):
    
    def setUp(self):
        self.test_db = 'test_sims.db'
        database.init_db(self.test_db)

    def test_database_insertion(self):
        database.save_result(3.0, 0.5, 1.2e-11, db_name=self.test_db)
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT permittivity FROM results WHERE permittivity=3.0")
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], 3.0)
        conn.close()

    def test_analytics_logic(self):
        dummy_data = {3.0: np.array([0, 0, 1.0, 0])} # Peak at index 2
        dt = 1.0
        report = analytics.analyze_signal_propagation(dummy_data, dt)
        self.assertEqual(report[3.0]['arrival'], 2.0)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

if __name__ == '__main__':
    unittest.main()
