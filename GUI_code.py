import os
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image

extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')


def browse_folder(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, END)
        entry.insert(0, folder)


# ------------------ RESIZE ------------------
def resize_images():
    input_folder = resize_input.get()
    output_folder = resize_output.get()
    max_size = int(resize_size.get())

    if not input_folder or not output_folder:
        messagebox.showerror("خطا", "مسیر پوشه‌ها را مشخص کنید")
        return

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith(extensions):
            path = os.path.join(input_folder, file)
            save_path = os.path.join(output_folder, file)

            with Image.open(path) as img:
                w, h = img.size
                if w > h:
                    nw = max_size
                    nh = int(h * (max_size / w))
                else:
                    nh = max_size
                    nw = int(w * (max_size / h))

                resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
                resized.save(save_path, quality=95)

    messagebox.showinfo("انجام شد", "تمام تصاویر تغییر اندازه داده شدند")


# ------------------ COMPRESS ------------------
def compress_images():
    input_folder = compress_input.get()
    output_folder = compress_output.get()
    quality = int(compress_quality.get())

    if not input_folder or not output_folder:
        messagebox.showerror("خطا", "مسیر پوشه‌ها را مشخص کنید")
        return

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith(extensions):
            path = os.path.join(input_folder, file)
            save_path = os.path.join(output_folder, file)

            with Image.open(path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                img.save(save_path, optimize=True, quality=quality)

    messagebox.showinfo("انجام شد", "تمام تصاویر فشرده شدند")


# ------------------ CONVERT ------------------
def convert_images():
    input_folder = convert_input.get()
    output_folder = convert_output.get()
    to_format = convert_format.get().lower()

    if not input_folder or not output_folder:
        messagebox.showerror("خطا", "مسیر پوشه‌ها را مشخص کنید")
        return

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith(extensions):
            path = os.path.join(input_folder, file)
            name, _ = os.path.splitext(file)
            save_path = os.path.join(output_folder, f"{name}.{to_format}")

            with Image.open(path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(save_path)

    messagebox.showinfo("انجام شد", "تمام تصاویر تبدیل شدند")


# ------------------ GUI ------------------
app = Tk()
app.title("Image Tool")
app.geometry("600x350")

tabs = ttk.Notebook(app)
tabs.pack(fill=BOTH, expand=1)

# ----------- Resize Tab -----------
resize_tab = Frame(tabs)
tabs.add(resize_tab, text="Resize")

resize_input = Entry(resize_tab, width=50)
resize_input.pack(pady=5)
Button(resize_tab, text="انتخاب پوشه ورودی", command=lambda: browse_folder(resize_input)).pack()

resize_output = Entry(resize_tab, width=50)
resize_output.pack(pady=5)
Button(resize_tab, text="انتخاب پوشه خروجی", command=lambda: browse_folder(resize_output)).pack()

resize_size = Entry(resize_tab)
resize_size.insert(0, "1000")
resize_size.pack(pady=10)

Button(resize_tab, text="شروع Resize", command=resize_images).pack(pady=10)


# ----------- Compress Tab -----------
compress_tab = Frame(tabs)
tabs.add(compress_tab, text="Compress")

compress_input = Entry(compress_tab, width=50)
compress_input.pack(pady=5)
Button(compress_tab, text="انتخاب پوشه ورودی", command=lambda: browse_folder(compress_input)).pack()

compress_output = Entry(compress_tab, width=50)
compress_output.pack(pady=5)
Button(compress_tab, text="انتخاب پوشه خروجی", command=lambda: browse_folder(compress_output)).pack()

compress_quality = Entry(compress_tab)
compress_quality.insert(0, "80")
compress_quality.pack(pady=10)

Button(compress_tab, text="شروع Compress", command=compress_images).pack(pady=10)


# ----------- Convert Tab -----------
convert_tab = Frame(tabs)
tabs.add(convert_tab, text="Convert")

convert_input = Entry(convert_tab, width=50)
convert_input.pack(pady=5)
Button(convert_tab, text="انتخاب پوشه ورودی", command=lambda: browse_folder(convert_input)).pack()

convert_output = Entry(convert_tab, width=50)
convert_output.pack(pady=5)
Button(convert_tab, text="انتخاب پوشه خروجی", command=lambda: browse_folder(convert_output)).pack()

convert_format = Entry(convert_tab)
convert_format.insert(0, "webp")
convert_format.pack(pady=10)

Button(convert_tab, text="شروع Convert", command=convert_images).pack(pady=10)

app.mainloop()
