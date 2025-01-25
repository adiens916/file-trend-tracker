"""
Written by ChatGPT
"""

import os
from datetime import datetime

import pandas as pd


class FileAnalyzer:
    def __init__(self, folder_path, exclude_folders=None):
        """
        :param folder_path: 탐색할 폴더 경로
        :param exclude_folders: 제외할 폴더 이름 목록 (리스트 형태)
        """
        self.folder_path = folder_path
        self.exclude_folders = exclude_folders if exclude_folders else []
        self.file_data = []

    def collect_file_data(self):
        """
        Collects file data including modified date and size from the folder path.
        Excludes folders matching any of the keywords in exclude_folders.
        """
        for root, dirs, files in os.walk(self.folder_path):
            # 제외할 폴더가 포함된 폴더 이름을 제거
            dirs[:] = self._filter_excluded_dirs(dirs)

            for file in files:
                file_path = os.path.join(root, file)
                try:
                    modified_time = os.path.getmtime(file_path)  # 수정 시간
                    file_size = os.path.getsize(file_path)  # 파일 크기 (바이트)
                    modified_date = datetime.fromtimestamp(modified_time).date()
                    self.file_data.append({"date": modified_date, "size": file_size})
                except Exception as e:
                    print(f"파일 처리 중 오류 발생: {file_path}, {e}")

    def _filter_excluded_dirs(self, dirs):
        """
        제외할 폴더 키워드를 기준으로 dirs 리스트를 필터링합니다.
        """
        filtered_dirs = []
        for d in dirs:
            contains_excluded_keyword = any(
                keyword in d for keyword in self.exclude_folders
            )
            if not contains_excluded_keyword:
                filtered_dirs.append(d)
        return filtered_dirs

    def aggregate_data(self):
        """
        Aggregates file data by date to calculate file count and total size per date.
        Returns a DataFrame with the aggregated data.
        """
        df = pd.DataFrame(self.file_data)
        aggregated_data = (
            df.groupby("date")
            .agg(
                file_count=("size", "size"),  # 파일 개수
                total_size=("size", "sum"),  # 총 파일 크기
            )
            .reset_index()
        )
        return aggregated_data

    def save_to_csv(self, output_path):
        """
        Saves the aggregated data to a CSV file.
        """
        aggregated_data = self.aggregate_data()
        aggregated_data.to_csv(output_path, index=False)
        print(f"결과가 저장되었습니다: {output_path}")
