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
    @classmethod
    def setUpClass(self):
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

        # 제외할 폴더 및 하위 파일 생성
        self.exclude_dir = os.path.join(self.test_dir, ".venv")
        os.makedirs(self.exclude_dir, exist_ok=True)
        exclude_file_path = os.path.join(self.exclude_dir, "excluded_file.txt")
        with open(exclude_file_path, "w") as f:
            f.write("This file should be excluded.")

    @classmethod
    def tearDownClass(self):
        """
        테스트 후 디렉토리 삭제
        """
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_collect_file_data_exclude_folders(self):
        """
        FileAnalyzer가 제외할 폴더를 올바르게 처리하는지 테스트
        """
        analyzer = FileAnalyzer(self.test_dir, exclude_folders=[".venv"])
        analyzer.collect_file_data()

        # 제외 폴더를 제외한 파일만 수집되었는지 확인
        self.assertEqual(len(analyzer.file_data), 3)  # 제외되지 않은 3개의 파일

    def test_collect_file_data_include_excluded(self):
        """
        제외 폴더를 지정하지 않을 경우 모든 파일이 포함되는지 테스트
        """
        analyzer = FileAnalyzer(self.test_dir)
        analyzer.collect_file_data()

        # 모든 파일이 수집되어야 함
        self.assertEqual(len(analyzer.file_data), 4)  # 포함된 파일: 3개 + 제외 파일 1개

    def test_collect_file_data_partial_match_exclude(self):
        """
        FileAnalyzer가 제외할 폴더 키워드를 올바르게 처리하는지 테스트
        """
        analyzer = FileAnalyzer(self.test_dir, exclude_folders=["venv"])
        analyzer.collect_file_data()

        # 제외되지 않은 파일만 포함되었는지 확인
        self.assertEqual(len(analyzer.file_data), 3)  # 제외되지 않은 3개의 파일

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
