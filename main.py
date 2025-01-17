from file_trend_tracker.file_analyzer import FileAnalyzer
from file_trend_tracker.data_plotter import DataPlotter


# 사용 예시
if __name__ == "__main__":
    # A 폴더 분석
    folder_a = r"C:\분석할\폴더A"
    analyzer_a = FileAnalyzer(folder_a)
    analyzer_a.collect_file_data()
    df_a = analyzer_a.aggregate_data()

    # B 폴더 분석
    folder_b = r"C:\분석할\폴더B"
    analyzer_b = FileAnalyzer(folder_b)
    analyzer_b.collect_file_data()
    df_b = analyzer_b.aggregate_data()

    # 데이터플로터 초기화 및 그래프 표시
    plotter = DataPlotter([df_a, df_b])
    plotter.plot()
