from PIL import Image
from pathlib import Path
from collections import Counter

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
print("ANÁLISE DA BASE PROCESSADA - GEOMAP")
print("=" * 60)

print(f"Imagens encontradas: {len(imagens)}")

if not imagens:
    print("Nenhuma imagem encontrada.")
    exit()

formatos = Counter(
    arquivo.suffix.lower()
    for arquivo in imagens
)

print("\nFormatos encontrados:")
for formato, quantidade in formatos.items():
    print(f"  {formato}: {quantidade}")

tamanhos = []
resolucoes = []

for arquivo in imagens:
    tamanho = arquivo.stat().st_size
    tamanhos.append(tamanho)

    with Image.open(arquivo) as imagem:
        resolucoes.append(imagem.size)

print("\nResoluções encontradas:")
resolucoes_unicas = Counter(resolucoes)

for resolucao, quantidade in resolucoes_unicas.items():
    print(
        f"  {resolucao[0]} x {resolucao[1]}: "
        f"{quantidade} imagens"
    )

tamanho_total = sum(tamanhos)
tamanho_medio = tamanho_total / len(tamanhos)
tamanho_minimo = min(tamanhos)
tamanho_maximo = max(tamanhos)

def converter_mb(valor):
    return valor / (1024 * 1024)

print("\nTamanho dos arquivos:")
print(f"  Total:   {converter_mb(tamanho_total):.2f} MB")
print(f"  Médio:   {converter_mb(tamanho_medio):.2f} MB")
print(f"  Mínimo:  {converter_mb(tamanho_minimo):.2f} MB")
print(f"  Máximo:  {converter_mb(tamanho_maximo):.2f} MB")

print("\nVerificação da resolução:")

if len(resolucoes_unicas) == 1:
    print("  Todas as imagens possuem a mesma resolução.")
else:
    print("  Existem imagens com resoluções diferentes.")

print("=" * 60)
print("ANÁLISE CONCLUÍDA")
print("=" * 60)