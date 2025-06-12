import argparse
from pathlib import Path

from bgremover.rembg_wrapper import models
from bgremover.runners import COMMANDS


def run_with_args() -> None:
    parser = argparse.ArgumentParser()

    global_parent = argparse.ArgumentParser(add_help=False)
    global_parent.add_argument(
        "-i",
        "--input-path",
        dest="input",
        metavar="INPUT_PATH",
        help="Path to the source image or directory with source images",
        type=str_to_path_or_fail,
        required=True,
    )
    global_parent.add_argument(
        "-o",
        "--output-dir",
        dest="output",
        metavar="OUT_DIR_PATH",
        help="Directory where to save the processed files",
        type=Path,
        required=True,
    )
    global_parent.add_argument(
        "-m",
        "--model",
        metavar="MODEL_NAME",
        dest="model",
        help="rembg compatible model name you want to use",
        default="birefnet-portrait",
        type=str,
        choices=models,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    process_single_parser = subparsers.add_parser(
        "one",
        help="Process a single image. Use -i with an image file path",
        parents=[global_parent],
    )
    process_single_parser.set_defaults(command="process_image")

    process_many_parser = subparsers.add_parser(
        "many",
        help="Process multiple images. Use -i with a directory containing images",
        parents=[global_parent],
    )
    process_many_parser.set_defaults(command="process_images")

    args = parser.parse_args()
    COMMANDS[args.command](args.input, args.output, args.model)


def str_to_path_or_fail(path_txt: str) -> Path:
    path = Path(path_txt).resolve()

    if not path.exists():
        msg = f"🔴 Error: {path} does not exist"
        raise argparse.ArgumentTypeError(msg)

    return path
