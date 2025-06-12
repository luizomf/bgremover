from pathlib import Path

from bgremover.rembg_wrapper import Models, allowed_extensions, remove_bg


def process_image(
    input_path: Path, output_dir: Path, model: Models = "birefnet-portrait"
) -> None | Path:
    output_dir.mkdir(exist_ok=True)

    if input_path.suffix.lower() not in allowed_extensions:
        print(f"🚫 File not allowed: {input_path}")
        return None

    try:
        print(f"🔄 Removing background: {input_path.name}")
        output_image = remove_bg(input_path, output_dir, model)
    except (ValueError, TypeError, KeyError) as e:
        print(f"🔴 Error with {input_path.name}: {e}")
    else:
        print(f"✅ Success: {output_image}")
        return output_image


def process_images(
    input_dir: Path, output_dir: Path, model: Models = "birefnet-portrait"
) -> None:
    if not input_dir.is_dir():
        print(f"🔴 Not a directory: {input_dir}")
        return

    files = input_dir.rglob("*.*")
    if not files:
        print(f"⚠️ No images found: {input_dir}")
        return

    for img_path in files:
        process_image(img_path, output_dir, model)


runners = {"process_image": process_image, "process_images": process_images}
