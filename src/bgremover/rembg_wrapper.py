from pathlib import Path
from typing import Literal, cast

from PIL import Image
from rembg import new_session, remove  # pyright: ignore

# Comparativo dos modelos testados:
# "u2net_human_seg" → bom equilíbrio, rápido, mas erra detalhes finos (3º lugar)
# "birefnet-general" → acerta mais que o u2net, mas ainda deixa passar erros (2º lugar)
# "birefnet-portrait" → mais preciso até agora, ótimo para fotos de pessoas (1º lugar)
# Os nomes dos models estão em
# -> from rembg.bg import sessions
# -> print(sessions.keys())

# Duplicating the model list for runtime (values) and static typing (Literal)
# because:
# 1. Literal[*models] breaks static analysis (Pyright hates it)
# 2. Runtime introspection is needed elsewhere (e.g., CLI choices)
# 3. This strikes the balance between performance, type safety, and readability
#
# Yes, it's duplicated. No, it's not a mistake. I really tried
type Models = Literal[
    "u2net",
    "u2netp",
    "u2net_human_seg",
    "u2net_cloth_seg",
    "u2net_custom",
    "bria-rmbg",
    "silueta",
    "isnet-general-use",
    "isnet-anime",
    "sam",
    "birefnet-general",
    "birefnet-general-lite",
    "birefnet-portrait",
    "birefnet-dis",
    "birefnet-hrsod",
    "birefnet-cod",
    "birefnet-massive",
    "ben2-base",
]

models = (
    "u2net",
    "u2netp",
    "u2net_human_seg",
    "u2net_cloth_seg",
    "u2net_custom",
    "bria-rmbg",
    "silueta",
    "isnet-general-use",
    "isnet-anime",
    "sam",
    "birefnet-general",
    "birefnet-general-lite",
    "birefnet-portrait",
    "birefnet-dis",
    "birefnet-hrsod",
    "birefnet-cod",
    "birefnet-massive",
    "ben2-base",
)


def remove_bg(
    in_img_path: Path, out_dir: Path, model: Models = "birefnet-portrait"
) -> Path:
    session = new_session(model)
    input_img: Image.Image = Image.open(in_img_path)

    pil_out_img = cast(
        "Image.Image",
        remove(
            input_img,
            session=session,
            # Ativa um acabamento extra na imagem para tentar refinar a
            # borda. Pode usar mais recursos e ser mais lento, mas também
            # pode gerar um resultado melhor.
            # Geralmente é bom para partes complexas, como cabelos por exemplo.
            alpha_matting=False,
            # Todas as opções abaixo precisam que alpha_matting seja True
            #
            # Diz ao alpha matting o quão
            # "claro" um pixel deve ser para ser considerado definitivamente
            # parte do objeto (primeiro plano). Quanto maior o valor, mais
            # estrito ele é para considerar algo como objeto.
            alpha_matting_foreground_threshold=240,
            # Diz ao alpha matting o quão "escuro" um pixel deve ser para ser
            # considerado definitivamente parte do fundo. Quanto menor o valor,
            # mais estrito ele é para considerar algo como fundo.
            alpha_matting_background_threshold=10,
            # Tamanho do recuo da borda. Quando maior o valor, maior e mais
            # suave o recuo. Valores muito altos podem fazer demorar várias
            # vezes mais. Isso não quer dizer que terá um resultado melher.
            # Dependerá exclusivamente do tipo de imagem e de testes
            alpha_matting_erode_size=10,
        ),
    )

    new_img_suffix = f"_{model}.png"
    new_img_name = f"{in_img_path.stem}{new_img_suffix}"
    out_img_path = out_dir / new_img_name
    pil_out_img.save(out_img_path)
    return out_img_path


allowed_extensions = [
    ".blp",
    ".bmp",
    ".bufr",
    ".cur",
    ".dcx",
    ".dds",
    ".dib",
    ".eps",
    ".ps",
    ".fit",
    ".fits",
    ".flc",
    ".fli",
    ".ftc",
    ".ftu",
    ".gbr",
    ".gif",
    ".grib",
    ".h5",
    ".hdf",
    ".icns",
    ".ico",
    ".im",
    ".iim",
    ".jfif",
    ".jpe",
    ".jpeg",
    ".jpg",
    ".j2c",
    ".j2k",
    ".jp2",
    ".jpc",
    ".jpf",
    ".jpx",
    ".mpeg",
    ".mpg",
    ".msp",
    ".pcd",
    ".pcx",
    ".pxr",
    ".apng",
    ".png",
    ".pbm",
    ".pfm",
    ".pgm",
    ".pnm",
    ".ppm",
    ".psd",
    ".qoi",
    ".bw",
    ".rgb",
    ".rgba",
    ".sgi",
    ".ras",
    ".icb",
    ".tga",
    ".vda",
    ".vst",
    ".tif",
    ".tiff",
    ".webp",
    ".emf",
    ".wmf",
    ".xbm",
    ".xpm",
]
