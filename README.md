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

## Instruções para obtenção dos dados

O dataset não será armazenado neste repositório devido ao seu tamanho e às condições de uso e distribuição estabelecidas pelos responsáveis.

O download deverá ser realizado diretamente através das fontes disponibilizadas acima, quando a etapa de desenvolvimento e testes do modelo for iniciada.

O conjunto de dados possui aproximadamente 4 GB na versão disponibilizada no Kaggle.

Após o download, os dados poderão passar por etapas de preparação e pré-processamento, incluindo a redução da resolução das imagens, caso seja necessário para adequar o volume de dados à capacidade computacional disponível e ao treinamento do modelo.

O dataset original deverá ser preservado, sendo utilizadas versões processadas para as etapas de desenvolvimento e treinamento quando necessário.

As informações complementares sobre o dataset também estão disponíveis em:

```text
data/README.md