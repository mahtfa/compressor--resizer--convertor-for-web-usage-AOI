import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
from datetime import datetime

# ================= CONFIG =================
SUPPORTED_FORMATS = ["jpg", "jpeg", "png", "bmp", "webp", "tiff", "gif"]
IMAGE_EXTENSIONS = tuple(f".{f}" for f in SUPPORTED_FORMATS)
LOG_FILE = "log.txt"

# ================= LOG SYSTEM =================
def write_log(message):
    log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def log_start(title):
    line = "=" * 50
    write_log(f"\n{line}")
    write_log(f"{title} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    write_log(f"{line}")

# ================= BROWSE =================
def browse_folder(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)

# ================= RESIZE =================
def resize_images():
    input_folder = resize_input.get()
    output_folder = resize_output.get()
    max_size = resize_size.get()

    if not input_folder or not output_folder or not max_size:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        max_size = int(max_size)
    except:
        messagebox.showerror("Error", "Max side must be a number.")
        return

    os.makedirs(output_folder, exist_ok=True)
    log_start("RESIZE STARTED")

    for file in os.listdir(input_folder):
        if file.lower().endswith(IMAGE_EXTENSIONS):
            try:
                path = os.path.join(input_folder, file)
                save_path = os.path.join(output_folder, file)

                with Image.open(path) as img:
                    w, h = img.size
                    if w > h:
                        new_w = max_size
                        new_h = int(h * (max_size / w))
                    else:
                        new_h = max_size
                        new_w = int(w * (max_size / h))

                    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                    resized.save(save_path, quality=95)

                write_log(f"✅ RESIZED: {file}")

            except Exception as e:
                write_log(f"❌ ERROR RESIZE {file} -> {e}")

    write_log("✅ RESIZE FINISHED\n")

# ================= COMPRESS =================
def compress_images():
    input_folder = compress_input.get()
    output_folder = compress_output.get()
    quality = compress_quality.get()

    if not input_folder or not output_folder or not quality:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        quality = int(quality)
    except:
        messagebox.showerror("Error", "Quality must be a number.")
        return

    os.makedirs(output_folder, exist_ok=True)
    log_start("COMPRESS STARTED")

    for file in os.listdir(input_folder):
        if file.lower().endswith(IMAGE_EXTENSIONS):
            try:
                path = os.path.join(input_folder, file)
                save_path = os.path.join(output_folder, file)

                with Image.open(path) as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    img.save(save_path, optimize=True, quality=quality)

                write_log(f"✅ COMPRESSED: {file}")

            except Exception as e:
                write_log(f"❌ ERROR COMPRESS {file} -> {e}")

    write_log("✅ COMPRESS FINISHED\n")

# ================= CONVERT (FIXED + SAFE) =================
def convert_images():
    input_folder = convert_input.get()
    output_folder = convert_output.get()
    target_format = convert_format.get().lower()

    if not input_folder or not output_folder or not target_format:
        messagebox.showerror("Error", "All fields are required.")
        return

    if target_format not in SUPPORTED_FORMATS:
        messagebox.showerror("Error", "Invalid target format.")
        return

    os.makedirs(output_folder, exist_ok=True)
    log_start("CONVERT STARTED")

    for file in os.listdir(input_folder):
        if file.lower().endswith(IMAGE_EXTENSIONS):
            try:
                path = os.path.join(input_folder, file)
                name, _ = os.path.splitext(file)
                save_path = os.path.join(output_folder, f"{name}.{target_format}")

                with Image.open(path) as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    img.save(save_path, target_format.upper())

                write_log(f"✅ CONVERTED: {file} -> {target_format}")

            except Exception as e:
                write_log(f"❌ ERROR CONVERT {file} -> {e}")

    write_log("✅ CONVERT FINISHED\n")

# ================= GUI =================
app = tk.Tk()
app.title("Image Studio Pro")
app.geometry("900x550")
app.resizable(False, False)

tabs = ttk.Notebook(app)
tabs.pack(fill="both", expand=True)

# ================= RESIZE TAB =================
resize_tab = ttk.Frame(tabs)
tabs.add(resize_tab, text="Resize")

ttk.Label(resize_tab, text="Input Folder").grid(row=0, column=0, padx=10, pady=5)
resize_input = ttk.Entry(resize_tab, width=55)
resize_input.grid(row=0, column=1)
ttk.Button(resize_tab, text="Browse", command=lambda: browse_folder(resize_input)).grid(row=0, column=2)

ttk.Label(resize_tab, text="Output Folder").grid(row=1, column=0, padx=10, pady=5)
resize_output = ttk.Entry(resize_tab, width=55)
resize_output.grid(row=1, column=1)
ttk.Button(resize_tab, text="Browse", command=lambda: browse_folder(resize_output)).grid(row=1, column=2)

ttk.Label(resize_tab, text="Max Side (Longest Edge in px)").grid(row=2, column=0, padx=10, pady=5)
resize_size = ttk.Entry(resize_tab)
resize_size.insert(0, "1000")
resize_size.grid(row=2, column=1, sticky="w")

ttk.Button(resize_tab, text="Start Resize", command=resize_images).grid(row=3, column=1, pady=10)

# ================= COMPRESS TAB =================
compress_tab = ttk.Frame(tabs)
tabs.add(compress_tab, text="Compress")

ttk.Label(compress_tab, text="Input Folder").grid(row=0, column=0, padx=10, pady=5)
compress_input = ttk.Entry(compress_tab, width=55)
compress_input.grid(row=0, column=1)
ttk.Button(compress_tab, text="Browse", command=lambda: browse_folder(compress_input)).grid(row=0, column=2)

ttk.Label(compress_tab, text="Output Folder").grid(row=1, column=0, padx=10, pady=5)
compress_output = ttk.Entry(compress_tab, width=55)
compress_output.grid(row=1, column=1)
ttk.Button(compress_tab, text="Browse", command=lambda: browse_folder(compress_output)).grid(row=1, column=2)

ttk.Label(compress_tab, text="Quality (1 - 100)").grid(row=2, column=0, padx=10, pady=5)
compress_quality = ttk.Entry(compress_tab)
compress_quality.insert(0, "80")
compress_quality.grid(row=2, column=1, sticky="w")

ttk.Button(compress_tab, text="Start Compress", command=compress_images).grid(row=3, column=1, pady=10)

# ================= CONVERT TAB =================
convert_tab = ttk.Frame(tabs)
tabs.add(convert_tab, text="Convert")

ttk.Label(convert_tab, text="Input Folder").grid(row=0, column=0, padx=10, pady=5)
convert_input = ttk.Entry(convert_tab, width=55)
convert_input.grid(row=0, column=1)
ttk.Button(convert_tab, text="Browse", command=lambda: browse_folder(convert_input)).grid(row=0, column=2)

ttk.Label(convert_tab, text="Output Folder").grid(row=1, column=0, padx=10, pady=5)
convert_output = ttk.Entry(convert_tab, width=55)
convert_output.grid(row=1, column=1)
ttk.Button(convert_tab, text="Browse", command=lambda: browse_folder(convert_output)).grid(row=1, column=2)

ttk.Label(convert_tab, text="Target Format").grid(row=2, column=0, padx=10, pady=5)

convert_format = ttk.Combobox(convert_tab, values=SUPPORTED_FORMATS)
convert_format.set("webp")
convert_format.grid(row=2, column=1, sticky="w")

ttk.Button(convert_tab, text="Start Convert", command=convert_images).grid(row=3, column=1, pady=10)

# ================= LOG PANEL =================
log_frame = ttk.LabelFrame(app, text="Process Log")
log_frame.pack(fill="both", expand=True, padx=10, pady=8)

log_box = tk.Text(log_frame, height=10)
log_box.pack(fill="both", expand=True)

write_log("✅ Image Studio Pro Ready...")

app.mainloop()
