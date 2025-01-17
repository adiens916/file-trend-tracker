"""
Written by ChatGPT
"""

import matplotlib.pyplot as plt


class DataPlotter:
    def __init__(self, dataframes):
        self.dataframes = dataframes if isinstance(dataframes, list) else [dataframes]

    def plot(self):
        """
        Plots the data. If multiple DataFrames are provided, they are combined for comparison.
        """
        combined_data = self._combine_dataframes()

        # Create subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

        # Plot file counts
        for label, data in combined_data.items():
            ax1.plot(
                data["date"],
                data["file_count"],
                marker="o",
                label=f"{label} - File Count",
            )
        ax1.set_ylabel("파일 개수")
        ax1.set_title("날짜별 파일 개수 비교")
        ax1.legend()
        ax1.grid(True)

        # Plot total sizes
        for label, data in combined_data.items():
            ax2.plot(
                data["date"],
                data["total_size"],
                marker="x",
                label=f"{label} - Total Size",
            )
        ax2.set_ylabel("파일 크기 (bytes)")
        ax2.set_title("날짜별 파일 크기 비교")
        ax2.legend()
        ax2.grid(True)

        plt.xlabel("날짜")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def _combine_dataframes(self):
        """
        Combines multiple dataframes for plotting. Ensures consistent date range for comparison.
        Returns a dictionary of DataFrames keyed by label.
        """
        combined_data = {}
        for i, df in enumerate(self.dataframes):
            label = f"Dataset {i + 1}"
            combined_data[label] = df
        return combined_data
