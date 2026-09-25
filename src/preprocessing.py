from PIL import Image
from pathlib import Path

# ============================================================
# CONFIGURAÇÕES
# ============================================================

PASTA_ORIGINAL = Path(
    r"D:\faculdade\archive\semantic_drone_dataset\training_set\images"
)

PASTA_PROCESSADA = PASTA_ORIGINAL / "processed"

LARGURA = 1280
ALTURA = 853

# Qualidade da compressão JPEG
QUALIDADE = 90

# Formatos aceitos
EXTENSOES = {".jpg", ".jpeg", ".png", ".webp"}

# ============================================================
# CRIAÇÃO DA PASTA DE SAÍDA
# ============================================================

PASTA_PROCESSADA.mkdir(exist_ok=True)

# Procura somente as imagens diretamente dentro da pasta original
imagens = [
    arquivo
    for arquivo in PASTA_ORIGINAL.iterdir()
    if arquivo.is_file()
    and arquivo.suffix.lower() in EXTENSOES
]

print("=" * 60)
print("REDIMENSIONAMENTO DO DATASET - GEOMAP")
print("=" * 60)

print(f"Imagens encontradas: {len(imagens)}")
print("Resolução original: 6000 x 4000")
print(f"Resolução nova:     {LARGURA} x {ALTURA}")
print(f"Pasta de saída:     {PASTA_PROCESSADA}")

print("=" * 60)

# ============================================================
# PROCESSAMENTO
# ============================================================

tamanho_original_total = 0
tamanho_processado_total = 0

processadas = 0
erros = 0

for numero, arquivo in enumerate(imagens, start=1):

    try:

        # Tamanho original
        tamanho_original = arquivo.stat().st_size
        tamanho_original_total += tamanho_original

        # Abre a imagem
        with Image.open(arquivo) as imagem:

            # Converte para RGB
            imagem = imagem.convert("RGB")

            # Redimensionamento
            imagem_redimensionada = imagem.resize(
                (LARGURA, ALTURA),
                Image.Resampling.LANCZOS
            )

            # Nome do arquivo processado
            nome_saida = arquivo.stem + ".jpg"

            caminho_saida = (
                PASTA_PROCESSADA / nome_saida
            )

            # Salva a imagem
            imagem_redimensionada.save(
                caminho_saida,
                "JPEG",
                quality=QUALIDADE,
                optimize=True
            )

        # Tamanho processado
        tamanho_processado = caminho_saida.stat().st_size
        tamanho_processado_total += tamanho_processado

        processadas += 1

        print(
            f"[{numero}/{len(imagens)}] "
            f"{arquivo.name} -> {nome_saida}"
        )

    except Exception as erro:

        erros += 1

        print(f"ERRO: {arquivo.name}")
        print(f"      {erro}")


# ============================================================
# RESULTADOS
# ============================================================

def converter_mb(tamanho):
    return tamanho / (1024 * 1024)


print()
print("=" * 60)
print("RESULTADO DO PROCESSAMENTO")
print("=" * 60)

print(f"Total encontrado:          {len(imagens)}")
print(f"Processadas:               {processadas}")
print(f"Erros:                     {erros}")

print(
    f"\nTamanho original:          "
    f"{converter_mb(tamanho_original_total):.2f} MB"
)

print(
    f"Tamanho processado:        "
    f"{converter_mb(tamanho_processado_total):.2f} MB"
)

if tamanho_original_total > 0:

    reducao = (
        1 -
        tamanho_processado_total /
        tamanho_original_total
    ) * 100

    print(
        f"Redução de armazenamento:  "
        f"{reducao:.2f}%"
    )

print()
print("Resolução original:   6000 x 4000")
print("Resolução processada: 1280 x 853")

print("=" * 60)
print("PROCESSAMENTO CONCLUÍDO")
print("=" * 60)