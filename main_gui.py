import tkinter as tk
from tkinter import filedialog, messagebox
from file_trend_tracker.file_analyzer import FileAnalyzer
from file_trend_tracker.data_plotter import DataPlotter


def add_folder():
    folder_path = filedialog.askdirectory(title="폴더 선택")
    if folder_path:
        folder_listbox.insert(tk.END, folder_path)


def analyze_and_plot():
    folder_paths = list(folder_listbox.get(0, tk.END))

    if not folder_paths:
        messagebox.showwarning("경고", "분석할 폴더를 선택하세요.")
        return

    data_frames = []
    for folder in folder_paths:
        try:
            analyzer = FileAnalyzer(folder)
            analyzer.collect_file_data()
            df = analyzer.aggregate_data()
            data_frames.append(df)
        except Exception as e:
            messagebox.showerror("오류", f"폴더 {folder} 분석 중 오류 발생: {e}")

    if data_frames:
        plotter = DataPlotter(data_frames)
        plotter.plot_count()
        plotter.plot_size()
        messagebox.showinfo("완료", "그래프 생성이 완료되었습니다.")
    else:
        messagebox.showwarning("경고", "분석할 데이터가 없습니다.")


def clear_list():
    folder_listbox.delete(0, tk.END)


# GUI 설정
root = tk.Tk()
root.title("파일 경로 분석 도구")

frame = tk.Frame(root)
frame.pack(pady=10)

folder_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=50, height=10)
folder_listbox.pack(side=tk.LEFT, padx=(0, 10))

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=folder_listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
folder_listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="폴더 추가", command=add_folder)
add_button.grid(row=0, column=0, padx=5)

analyze_button = tk.Button(
    button_frame, text="분석 및 그래프 생성", command=analyze_and_plot
)
analyze_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="초기화", command=clear_list)
clear_button.grid(row=0, column=2, padx=5)

exit_button = tk.Button(button_frame, text="종료", command=root.quit)
exit_button.grid(row=0, column=3, padx=5)

root.mainloop()
