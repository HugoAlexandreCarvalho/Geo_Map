# GeoMap — Processamento e Segmentação de Imagens Aéreas

## Integrantes da equipe

- Gustavo Barros Martins
- Hugo Alexandre Carvalho Coelho Coutinho
- Jeferson Machado dos Santos
- Maicon de Sousa Pontes

## Descrição do problema

O projeto busca auxiliar um engenheiro autônomo na análise de imagens aéreas obtidas por drones.

Atualmente, a identificação manual de diferentes elementos presentes no terreno, como solo, vegetação, pedras, áreas pavimentadas e construções, pode demandar bastante tempo e estar sujeita a erros de interpretação.

O GeoMap propõe o uso de Inteligência Artificial e processamento digital de imagens para automatizar parte dessa análise, realizando a segmentação semântica das imagens aéreas e identificando diferentes elementos presentes no terreno.

## Conjunto de dados utilizado

**Semantic Drone Dataset**

O Semantic Drone Dataset é um conjunto de imagens aéreas obtidas por drones, acompanhado de informações de segmentação semântica.

O dataset contém imagens de alta resolução e diferentes classes de elementos presentes nas cenas, sendo adequado para o desenvolvimento e avaliação de modelos de segmentação de imagens.

## Fonte dos dados

**Graz University of Technology (TU Graz)**

O conjunto de dados foi desenvolvido para pesquisas relacionadas à compreensão semântica de imagens aéreas obtidas por drones.

## Link para a fonte original

Página oficial do dataset:

https://ivc.tugraz.at/research-project/semantic-drone-dataset/

Dataset disponibilizado no Kaggle:

https://www.kaggle.com/datasets/awsaf49/semantic-drone-dataset

## Dados tratados

Durante a etapa de preparação dos dados, foram processadas **400 imagens** do conjunto de treinamento.

As imagens originais apresentavam resolução de **6000 × 4000 pixels** e foram redimensionadas para **1280 × 853 pixels**, mantendo aproximadamente a mesma proporção das imagens originais.

O tratamento foi realizado utilizando **Python** e a biblioteca **Pillow**, por meio do script:

```text
src/preprocessing.py