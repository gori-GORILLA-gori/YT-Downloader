import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys
import os
import threading
import re
import shutil
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        outdir_var.set(folder)

def browse_cookies():
    file = filedialog.askopenfilename(filetypes=[("Cookies.txt", "*.txt")])
    if file:
        cookie_path_var.set(file)

def toggle_cookie_ui():
    if use_cookie_var.get():
        cookie_frame.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
    else:
        cookie_frame.grid_remove()
        cookie_path_var.set("")

def run_command_with_logging(cmd, on_success=None):
    show_log = show_log_var.get()
    try:
        if not show_log:
            subprocess.run(cmd, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            subprocess.run(cmd, check=True)
        if on_success:
            on_success()
        else:
            messagebox.showinfo("完了", "処理が完了しました！")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("エラー", f"処理中にエラーが発生しました\n\n{e}")

def sanitize_filename(filename):
    name, ext = os.path.splitext(filename)
    name = re.sub(r'[^A-Za-z0-9_\-]', '_', name)
    return name + ext

def get_new_file(outdir, before_files, timeout=30):
    """ダウンロード完了後の新しいファイルを検出する関数"""
    for _ in range(timeout):
        after_files = set(os.listdir(outdir))
        new_files = after_files - before_files
        if new_files:
            return new_files.pop()
        time.sleep(1)
    return None

def download_video():
    url = url_var.get().strip()
    outdir = outdir_var.get().strip()
    use_cookie = use_cookie_var.get()
    cookie_path = cookie_path_var.get()

    if not url:
        messagebox.showerror("エラー", "動画のURLを入力してください")
        return
    if not outdir:
        messagebox.showerror("エラー", "保存先フォルダを指定してください")
        return
    if use_cookie and not cookie_path:
        messagebox.showerror("エラー", "cookies.txt を指定してください")
        return

    ytdlp_path = resource_path("yt-dlp.exe")

    # ダウンロード前のファイル一覧取得
    before_files = set(os.listdir(outdir))

    # yt-dlpでファイル名取得（mp4固定）
    filename_cmd = [
        ytdlp_path,
        "-o", "%(title)s.mp4",
        "--get-filename",
        url
    ]
    result = subprocess.run(filename_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        messagebox.showerror("エラー", "ファイル名の取得に失敗しました。\n" + result.stderr)
        return
    expected_filename = result.stdout.strip()

    # yt-dlpでダウンロード
    download_cmd = [
        ytdlp_path,
        "--no-mtime",
        "-f", "bv*+ba/b",
        "--merge-output-format", "mp4",
        "-o", os.path.join(outdir, "%(title)s.%(ext)s"),
    ]
    if use_cookie:
        download_cmd += ["--cookies", cookie_path]
    download_cmd.append(url)

    def after_download():
        # ダウンロード完了を待って新ファイル名検出
        new_file = get_new_file(outdir, before_files)
        if not new_file:
            messagebox.showerror("エラー", "ダウンロードファイルの検出に失敗しました。")
            return

        # 安全ファイル名生成
        safe_name = sanitize_filename(new_file)
        src_path = os.path.join(outdir, new_file)
        dst_path = os.path.join(outdir, safe_name)

        try:
            if os.path.exists(dst_path):
                os.remove(dst_path)
            shutil.move(src_path, dst_path)
            messagebox.showinfo("完了", f"ダウンロード完了: {safe_name}")
        except Exception as e:
            messagebox.showerror("エラー", f"ファイル移動に失敗しました:\n{e}")

    threading.Thread(target=lambda: run_command_with_logging(download_cmd, on_success=after_download)).start()

# GUI初期化
root = tk.Tk()
root.title("yt-dlp GUIダウンローダー")

url_var = tk.StringVar()
outdir_var = tk.StringVar()
cookie_path_var = tk.StringVar()
use_cookie_var = tk.BooleanVar()
show_log_var = tk.BooleanVar(value=True)

tk.Label(root, text="動画のURL").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=url_var, width=50).grid(row=0, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="保存先フォルダ").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=outdir_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="参照", command=browse_folder).grid(row=1, column=2, padx=5, pady=5)

tk.Checkbutton(root, text="ログを表示する", variable=show_log_var).grid(row=2, column=1, sticky="w", padx=5)
tk.Checkbutton(root, text="cookies.txt を使う", variable=use_cookie_var, command=toggle_cookie_ui).grid(row=4, column=1, sticky="w", padx=5)

cookie_frame = tk.Frame(root)
tk.Label(cookie_frame, text="cookies.txt パス:").grid(row=0, column=0, padx=4)
tk.Entry(cookie_frame, textvariable=cookie_path_var, width=40, state="readonly").grid(row=0, column=1, padx=5)
tk.Button(cookie_frame, text="参照", command=browse_cookies).grid(row=0, column=2, padx=5)
cookie_frame.grid_remove()

tk.Button(root, text="ダウンロード開始", command=download_video).grid(row=6, column=1, pady=10)

root.mainloop()
