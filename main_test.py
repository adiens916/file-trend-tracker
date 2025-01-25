from file_trend_tracker.file_analyzer import FileAnalyzer
from file_trend_tracker.data_plotter import DataPlotter


# 사용 예시
if __name__ == "__main__":
    folder_path = "."  # 탐색할 폴더 경로
    exclude_folders = ["git", "venv", "build", "egg"]  # 제외할 폴더 목록

    analyzer = FileAnalyzer(folder_path, exclude_folders)
    analyzer.collect_file_data()
    df = analyzer.aggregate_data()

    dp = DataPlotter([df])
    dp.plot_count()
