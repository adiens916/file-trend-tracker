"""
Written by ChatGPT
"""

from file_trend_tracker.file_analyzer import FileAnalyzer
from file_trend_tracker.data_plotter import DataPlotter


def main():
    folder_paths = []

    print("\n[파일 경로 분석 도구]")
    print("폴더 경로를 입력하세요. 빈 입력을 하면 분석을 종료합니다.\n")

    while True:
        folder_path = input("폴더 경로 입력: ")

        if not folder_path.strip():  # 빈 입력 시 종료
            break

        folder_paths.append(folder_path)

    if not folder_paths:  # 경로가 하나도 입력되지 않은 경우 종료
        print("\n분석할 폴더가 없습니다. 프로그램을 종료합니다.")
        return

    data_frames = []

    for folder in folder_paths:
        print(f"\n[분석 중] {folder}")
        try:
            analyzer = FileAnalyzer(folder)
            analyzer.collect_file_data()
            df = analyzer.aggregate_data()
            data_frames.append(df)
        except Exception as e:
            print(f"오류 발생: {e}")

    if data_frames:
        print("\n[그래프 생성]")
        plotter = DataPlotter(data_frames)
        plotter.plot_count()
        plotter.plot_size()
    else:
        print("\n분석할 데이터가 없습니다.")

    print("\n프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
