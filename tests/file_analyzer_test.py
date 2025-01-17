"""
Written by ChatGPT
"""

import unittest
import os
import shutil
from datetime import datetime, timedelta

import pandas as pd
from file_trend_tracker.file_analyzer import FileAnalyzer


class TestFileAnalyzer(unittest.TestCase):
    def setUp(self):
        """
        테스트용 디렉토리와 파일 생성
        """
        self.test_dir = "test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

        # 3일 전, 2일 전, 1일 전 파일 생성
        for i in range(3):
            file_path = os.path.join(self.test_dir, f"file_{i}.txt")
            with open(file_path, "w") as f:
                f.write(f"Test content {i}")
            modified_time = (datetime.now() - timedelta(days=i)).timestamp()
            os.utime(file_path, (modified_time, modified_time))

    def tearDown(self):
        """
        테스트 후 디렉토리 삭제
        """
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_collect_file_data(self):
        """
        FileAnalyzer가 파일 데이터를 올바르게 수집하는지 테스트
        """
        analyzer = FileAnalyzer(self.test_dir)
        analyzer.collect_file_data()
        self.assertEqual(len(analyzer.file_data), 3)  # 3개의 파일이 생성되었는지 확인

    def test_aggregate_data(self):
        """
        파일 데이터를 날짜별로 정확히 집계하는지 테스트
        """
        analyzer = FileAnalyzer(self.test_dir)
        analyzer.collect_file_data()
        df = analyzer.aggregate_data()
        self.assertEqual(len(df), 3)  # 3개의 날짜 데이터가 포함되어야 함
        self.assertTrue("file_count" in df.columns and "total_size" in df.columns)

    def test_save_to_csv(self):
        """
        집계 데이터를 올바르게 CSV로 저장하는지 테스트
        """
        output_csv = "test_output.csv"
        analyzer = FileAnalyzer(self.test_dir)
        analyzer.collect_file_data()
        analyzer.save_to_csv(output_csv)

        self.assertTrue(os.path.exists(output_csv))
        saved_df = pd.read_csv(output_csv)
        self.assertEqual(len(saved_df), 3)  # CSV에 3개의 데이터가 저장되어야 함

        os.remove(output_csv)


if __name__ == "__main__":
    unittest.main()
