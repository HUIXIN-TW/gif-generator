# 📸 GIF Generator

This Python script automatically generates a timestamped GIF from a folder of numbered PNG screenshots (like `1.png`, `2.png`, etc). It's useful for showcasing UI flows or demos — especially for apps like [NotionSyncGCal](https://notionsyncgcal.huixinyang.com/).

## ✨ Features

- Converts numbered PNGs to a smooth GIF
- Automatically sorts files like `1.png`, `2.png`, ..., `10.png`
- Adds timestamp and folder name to the output filename
- Saves the GIF in the same folder

## 🛠️ Requirements

- Python 3.7+
- Pillow

Install dependencies:

```bash
conda create -n gif-demo python=3.11 pillow
conda activate gif-demo
````

## 🚀 Usage

Place your numbered screenshots (e.g. `1.png`, `2.png`, etc.) into a folder.

Then run the script:

```python
from generate_gif import create_gif_from_folder

create_gif_from_folder("your-folder-name/")
```

The output will be saved as:

```text
your-folder-name/your-folder-name_demo-YYYYMMDD_HHMMSS.gif
```

## 📁 Folder Structure Example

```bash
project-root/
├── your-folder-name/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   └── ...
├── generate_gif.py
└── README.md
```

## 🤖 License

MIT License. Feel free to use or modify.

---

Created with ❤️ by [Huixin Yang](https://huixinyang.com)