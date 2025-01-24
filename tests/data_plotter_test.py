"""
Written by ChatGPT
"""

import unittest
from datetime import datetime, timedelta

import pandas as pd
from file_trend_tracker.data_plotter import DataPlotter


class TestDataPlotter(unittest.TestCase):
    def setUp(self):
        """
        샘플 데이터프레임 생성
        """
        self.df_a = pd.DataFrame(
            {
                "date": [
                    datetime.now().date() - timedelta(days=i) for i in range(2, -1, -1)
                ],
                "file_count": [5, 10, 15],
                "total_size": [500, 1000, 1500],
            }
        )
        self.df_b = pd.DataFrame(
            {
                "date": [
                    datetime.now().date() - timedelta(days=i) for i in range(2, -1, -1)
                ],
                "file_count": [2, 4, 6],
                "total_size": [200, 400, 600],
            }
        )

    def test_single_dataframe_plot(self):
        """
        단일 데이터프레임을 입력받아 플롯을 생성할 수 있는지 테스트
        """
        plotter = DataPlotter(self.df_a)
        try:
            plotter.plot_count()
            plotter.plot_size()
        except Exception as e:
            self.fail(f"plot() raised an exception: {e}")

    def test_multiple_dataframes_plot(self):
        """
        여러 데이터프레임을 입력받아 플롯을 생성할 수 있는지 테스트
        """
        plotter = DataPlotter([self.df_a, self.df_b])
        try:
            plotter.plot_count()
            plotter.plot_size()
        except Exception as e:
            self.fail(f"plot() raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
