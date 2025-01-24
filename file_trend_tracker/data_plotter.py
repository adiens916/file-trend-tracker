"""
Written by ChatGPT & Claude.ai
"""

from pandas import DataFrame
import matplotlib.pyplot as plt


class DataPlotter:
    def __init__(self, dataframes: list[DataFrame]):
        self.dataframes = dataframes if isinstance(dataframes, list) else [dataframes]
        self.combined_data = self._combine_dataframes()
        self.colors = [
            "#1f77b4",
            "#ff7f0e",
            "#2ca02c",
            "#d62728",
            "#9467bd",
            "#8c564b",
            "#e377c2",
            "#7f7f7f",
            "#bcbd22",
            "#17becf",
        ]

    def plot_count(self):
        """
        Plots the file counts from the combined data.
        """
        self._plot_data(column="file_count", title="File Count", ylabel="file count")

    def plot_size(self):
        """
        Plots the total sizes from the combined data.
        """
        self._plot_data(
            column="total_size", title="File Size", ylabel="file size (bytes)"
        )

    def _plot_data(self, column: str, title: str, ylabel: str):
        """
        Generic plotting method to reduce code duplication
        """
        plt.figure(figsize=(12, 4))

        for i, (label, data) in enumerate(self.combined_data.items()):
            plt.plot(
                data["date"],
                data[column],
                color=self.colors[i % len(self.colors)],
                label=f"{label}",
                linestyle="--",
                linewidth=2,
            )

            # 점 표시 추가
            plt.scatter(
                data["date"],
                data[column],
                color=self.colors[i % len(self.colors)],
                marker="o",  # 원형 마커
                s=50,  # 마커 크기
            )

        plt.ylabel(ylabel)
        plt.title(f"{title} By Date")
        plt.legend()
        plt.grid(True)
        plt.xlabel("date")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def _combine_dataframes(self):
        """
        Combines multiple dataframes for plotting.
        """
        combined_data = {}
        for i, df in enumerate(self.dataframes):
            label = f"Dataset {i + 1}"
            combined_data[label] = df
        return combined_data
