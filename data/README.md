# Dataset

## Conjunto de dados selecionado

**Semantic Drone Dataset**

O Semantic Drone Dataset é um conjunto de imagens aéreas obtidas por drones, desenvolvido para tarefas de segmentação semântica de imagens.

O dataset é utilizado no projeto GeoMap como base para o desenvolvimento de um sistema capaz de identificar e classificar diferentes elementos presentes em imagens aéreas, como solo, vegetação, pedras, construções, áreas pavimentadas, entre outros.

## Fonte dos dados

**Instituição:** Graz University of Technology (TU Graz)

**Projeto:** Semantic Drone Dataset

**Página oficial:**  
https://ivc.tugraz.at/research-project/semantic-drone-dataset/

**Disponível também em:**  
https://www.kaggle.com/datasets/awsaf49/semantic-drone-dataset

## Características

- Imagens obtidas por veículos aéreos não tripulados (drones);
- Imagens de alta resolução;
- Aproximadamente 400 imagens públicas para treinamento;
- Imagens acompanhadas de informações de segmentação semântica;
- Diversas classes relacionadas ao ambiente e aos elementos presentes no terreno;
- Voltado principalmente para tarefas de visão computacional e segmentação semântica.

## Principais informações

As imagens apresentam diferentes elementos do ambiente, permitindo que um modelo de Inteligência Artificial aprenda a distinguir regiões e objetos presentes nas imagens aéreas.

Entre as classes representadas estão elementos como:

- Solo;
- Vegetação;
- Grama;
- Pedras;
- Cascalho;
- Árvores;
- Água;
- Áreas pavimentadas;
- Telhados;
- Muros;
- Cercas;
- Obstáculos.

## Formato

O dataset é disponibilizado em formato digital contendo imagens aéreas e suas respectivas informações de segmentação.

Para esta etapa do projeto, foram utilizadas as imagens aéreas do conjunto de treinamento. As imagens originais apresentam resolução de **6000 × 4000 pixels**.

Após o processo de preparação realizado no projeto, as imagens foram redimensionadas para **1280 × 853 pixels** e convertidas para o formato **JPEG (.jpg)**.

## Utilização no projeto

O dataset é utilizado como base para estudar, desenvolver e avaliar o sistema de segmentação de imagens aéreas proposto no projeto.

A utilização dessas imagens permite investigar técnicas capazes de reduzir a necessidade de identificação manual dos elementos presentes no terreno, auxiliando posteriormente profissionais que trabalham com análise de áreas e projetos relacionados ao terreno.

## Dados tratados

Como parte da etapa de preparação dos dados, foram processadas **400 imagens**, mantendo a proporção original das imagens e reduzindo sua resolução de **6000 × 4000 para 1280 × 853 pixels**.

O conjunto tratado possui aproximadamente **148,04 MB** e está disponível em um arquivo compactado no Google Drive.

**Download do dataset tratado:**  
[GeoMap – Dataset Tratado](https://drive.google.com/file/d/1kHErjA4FRB0QiFomNd9Aqv_ErCu9eEb2/view?usp=drive_link)

As imagens tratadas foram geradas utilizando o script `src/preprocessing.py`, desenvolvido em Python com a biblioteca Pillow.

O processo reduziu o espaço ocupado pelo conjunto de aproximadamente **3.892,20 MB para 148,04 MB**, representando uma redução de **96,20% no armazenamento**.

## Reprodução do processamento

O tratamento aplicado às imagens pode ser reproduzido por meio do script:

```text
src/preprocessing.py