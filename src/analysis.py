from PIL import Image
from pathlib import Path
import numpy as np

PASTA = Path(
    r"D:\faculdade\archive\semantic_drone_dataset\training_set\images\processed"
)

EXTENSOES = {".jpg", ".jpeg", ".png", ".webp"}

imagens = [
    arquivo
    for arquivo in PASTA.iterdir()
    if arquivo.is_file()
    and arquivo.suffix.lower() in EXTENSOES
]

print("=" * 60)
print("ESTATÍSTICAS DESCRITIVAS - GEOMAP")
print("=" * 60)

print(f"Imagens analisadas: {len(imagens)}")
print("Resolução: 1280 x 853")
print()

# Acumuladores
soma_rgb = np.zeros(3, dtype=np.float64)
soma_quadrados_rgb = np.zeros(3, dtype=np.float64)

min_rgb = np.full(3, 255, dtype=np.uint8)
max_rgb = np.zeros(3, dtype=np.uint8)

total_pixels = 0

for numero, arquivo in enumerate(imagens, start=1):

    with Image.open(arquivo) as imagem:
        imagem = imagem.convert("RGB")
        pixels = np.asarray(imagem, dtype=np.uint8)

    pixels = pixels.reshape(-1, 3)

    total_pixels += len(pixels)

    soma_rgb += pixels.sum(axis=0)
    soma_quadrados_rgb += (pixels.astype(np.float64) ** 2).sum(axis=0)

    min_rgb = np.minimum(min_rgb, pixels.min(axis=0))
    max_rgb = np.maximum(max_rgb, pixels.max(axis=0))

    if numero % 50 == 0:
        print(f"Imagens processadas: {numero}/{len(imagens)}")

# Média
media_rgb = soma_rgb / total_pixels

# Variância e desvio padrão
variancia_rgb = (
    soma_quadrados_rgb / total_pixels
) - (media_rgb ** 2)

desvio_rgb = np.sqrt(variancia_rgb)

# Luminosidade aproximada
luminosidade_media = (
    0.299 * media_rgb[0]
    + 0.587 * media_rgb[1]
    + 0.114 * media_rgb[2]
)

print()
print("=" * 60)
print("RESULTADOS")
print("=" * 60)

print(f"Total de pixels analisados: {total_pixels:,}")

print("\nMÉDIA DOS PIXELS")
print(f"  Vermelho (R): {media_rgb[0]:.2f}")
print(f"  Verde   (G): {media_rgb[1]:.2f}")
print(f"  Azul    (B): {media_rgb[2]:.2f}")

print("\nDESVIO PADRÃO")
print(f"  Vermelho (R): {desvio_rgb[0]:.2f}")
print(f"  Verde   (G): {desvio_rgb[1]:.2f}")
print(f"  Azul    (B): {desvio_rgb[2]:.2f}")

print("\nVALORES MÍNIMOS")
print(f"  Vermelho (R): {min_rgb[0]}")
print(f"  Verde   (G): {min_rgb[1]}")
print(f"  Azul    (B): {min_rgb[2]}")

print("\nVALORES MÁXIMOS")
print(f"  Vermelho (R): {max_rgb[0]}")
print(f"  Verde   (G): {max_rgb[1]}")
print(f"  Azul    (B): {max_rgb[2]}")

print(f"\nLuminosidade média aproximada: {luminosidade_media:.2f}")

print("=" * 60)
print("ANÁLISE ESTATÍSTICA CONCLUÍDA")
print("=" * 60)