# 🖼️ Image Toolbox GUI

**All-in-One Image Converter, Compressor & Resizer**

A modern desktop application for **batch image conversion, compression, and resizing** with a clean multi-tab GUI, live progress logs, and full user control over output settings.

Built with **Python**, using **Tkinter** for the interface and **Pillow** for image processing.

---

## 🚀 Features

✅ Multi-tab graphical interface

✅ Batch image processing

✅ Smart format converter with **searchable dropdown**

✅ High-quality **image compression (same format → smaller size)**

✅ Flexible **image resizing by largest side**

✅ Separate output folders for each tool

✅ Real-time **log panel inside the app**

✅ Automatic **log file saving to disk**

✅ **Stop button** to safely interrupt processing

✅ No overwriting — original filenames are preserved

✅ Crash-safe design with proper exception handling

---

## 📂 Tools Included (Tabs)

### 🔁 1. Image Converter Tab

Convert any supported image format into another with full control.

**User Inputs:**

* Source folder (input images)
* Destination folder
* Output format (searchable dropdown)
* Output quality (1–100)

**How it works:**

* Reads all images from the selected folder
* Converts them into the selected format
* Saves results to your chosen output directory
* Logs success & failures in real time

---

### 📉 2. Image Compressor Tab

Reduces file size **without changing the format**:

✅ JPG → JPG

✅ PNG → PNG

✅ WEBP → WEBP

✅ and more…

**User Inputs:**

* Input folder
* Output folder (`/compressed`)
* Compression quality level

**Best use case:**

* Website optimization
* Telegram / WhatsApp image size reduction
* Faster upload performance

---

### 📐 3. Image Resizer Tab

Resize images by defining the **largest side length**, while keeping aspect ratio.

**User Inputs:**

* Source folder
* Output folder (`/resized`)
* Max width/height value (example: 1024)

**How it works:**

* Automatically detects portrait / landscape
* Scales the image so the **largest edge equals your value**
* Keeps original filenames

---

## 🧾 Logging System

### ✅ Inside the Program

* Live status updates
* Shows:

  * Which images succeeded
  * Which failed
  * Current progress
* Color-coded messages (info, success, error)

### ✅ External Log File

* Automatically saved as:

```
log.txt
```

* Includes:

  * Timestamp
  * File name
  * Operation type
  * Result (SUCCESS / FAILED)
  * Error details (if any)

---

## ⛔ Stop Button

At any time during processing, you can press **STOP** to:

* Immediately halt processing
* Safely exit the current task
* Prevent system freezes
* Avoid forced closing (no data corruption)

---

## 🧠 Supported Formats

The format supports:

* JPG / JPEG
* PNG
* WEBP
* BMP
* TIFF
* ICO
* PPM
* TGA
* PDF (image export)

You can type directly inside the dropdown to auto-filter formats.

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mahtfa/compressor--resizer--convertor-for-web-usage-AOI
cd image-toolbox-gui
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
python main.py
```

---

## 📦 requirements.txt

```txt
Pillow
tk
ttkbootstrap
customtkinter
```

*(You can remove `ttkbootstrap` or `customtkinter` if you only use standard Tk widgets.)*

---

## ⚠️ Common Causes of Crashes (And Fixes)

| Issue                            | Solution                       |
| -------------------------------- | ------------------------------ |
| App crashes on Convert button    | Make sure output folder exists |
| Program freezes with many images | Use the STOP button            |
| Some WEBP images fail            | Update Pillow                  |
| PNG too large after compression  | Lower quality value            |

---

## 🗺️ Roadmap (Future Plans)

* [ ] Watermark tool
* [ ] Auto-naming templates

---

## 🧑‍💻 Developer Notes

* Fully threaded background processing (UI never freezes)
* All operations wrapped in try/except
* Logs written using safe file handlers
* OS independent (Windows / Linux / Mac)

---

## 📜 License

This project is licensed under the **MIT License**
You are free to use, modify, distribute, and sell it.

---

## ⭐ If You Like This Project

Please consider:

* Giving it a ⭐ on GitHub
* Sharing it with your team
* Using it in production projects

