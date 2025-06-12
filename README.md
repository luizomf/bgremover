# BGRemover - Remove background from images using rembg (CLI)

**BGRemover** is a command-line tool to remove image backgrounds using [rembg](https://github.com/danielgatis/rembg) and powerful AI models like `u2net`, `birefnet`, and others.

- 🖼️ Process individual images or entire folders
- ⚙️ Choose among multiple rembg-compatible models
- 🧠 Built with Python 3.13+, argparse, and modern packaging
- 💻 Easy to install with [`uv`](https://github.com/astral-sh/uv)
- 🔒 Fully local, no cloud dependencies after downloading the models

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/luizomf/bgremover.git
cd bgremover
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv sync
```

### 2. Manual installation (if needed)

Install dependencies safely using `--no-build-package` to avoid native compilation issues:

```bash
uv add pillow
uv add --no-build-package llvmlite llvmlite
uv add --no-build-package numba numba
uv add "rembg[cpu]" --no-build-package numba
```

> 💡 On Windows, make sure you have [Microsoft Visual C++ Redistributable](https://rb.gy/c4deeu) installed.

---

## 🧪 Verifying Installation

```bash
uv pip show llvmlite
uv pip show numba
uv run python -c "import llvmlite; print(llvmlite.__version__)"
uv run python -c "import numba; print(numba.__version__)"
```

---

## 🧠 Usage

### CLI commands

```bash
bgremover -h
```

```text
usage: bgremover [-h] {one,many} ...

subcommands:
  one       Remove background from a single image
  many      Remove background from all images in a directory
```

### Examples

#### One image:

```bash
bgremover one -i ./images/photo.png -o ./out/
```

#### Multiple images:

```bash
bgremover many -i ./images/ -o ./out/ -m isnet-anime
```

---

## 🎨 Supported Models

You can use any rembg-compatible model:

```text
u2net, u2netp, u2net_human_seg, u2net_cloth_seg, u2net_custom, silueta,
isnet-general-use, isnet-anime, sam, birefnet-general, birefnet-general-lite,
birefnet-portrait, birefnet-dis, birefnet-hrsod, birefnet-cod,
birefnet-massive, ben2-base
```

---

## 🧾 Where are AI models stored?

- **Windows:** `C:\Users\YOUR_USER\.u2net`
- **Linux/macOS:** `~/.u2net`

---

## 🧰 Project structure

```text
src/bgremover/
├── cli.py              # CLI entrypoint with argparse
├── runners.py          # Dispatch map for subcommands
├── rembg_wrapper.py    # Model list, remove_bg(), etc.
├── constants.py        # (optional) allowed_extensions, etc.
```

---

## 🧠 Developer mode

You can run the CLI locally:

```bash
uv run bgremover one -i ./images/photo.jpg -o ./out/
```

---

## 👨‍🏫 Author

Created by [Luiz Otávio Miranda](https://www.otaviomiranda.com.br)
📺 [YouTube @OtavioMiranda](https://www.youtube.com/@OtavioMiranda)
🐙 [GitHub @luizomf](https://github.com/luizomf)

---

## 📄 License

MIT

---
