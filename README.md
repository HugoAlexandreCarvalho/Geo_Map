# GeoMap — Processamento e Segmentação de Imagens Aéreas

## Sobre o projeto

O GeoMap é um projeto acadêmico voltado ao processamento digital e à segmentação semântica de imagens aéreas obtidas por drones, utilizando técnicas de Inteligência Artificial e Ciência de Dados.

A proposta busca auxiliar engenheiros na interpretação de terrenos por meio da identificação automatizada de diferentes elementos presentes nas imagens, contribuindo para tornar esse processo mais ágil e organizado.

O projeto está sendo desenvolvido de forma incremental, passando pelas etapas de planejamento, seleção e preparação de dados, implementação de modelos de Inteligência Artificial e avaliação experimental dos resultados.

## Integrantes da equipe

- Gustavo Barros Martins
- Hugo Alexandre Carvalho Coelho Coutinho
- Jeferson Machado dos Santos
- Maicon de Sousa Pontes

## Descrição do problema

A análise de imagens aéreas obtidas por drones pode exigir tempo e conhecimento técnico, principalmente quando envolve a identificação de diferentes elementos presentes em uma determinada área.

A identificação manual de características como solo, vegetação, pedras, áreas pavimentadas e construções pode demandar bastante tempo e estar sujeita a erros de interpretação.

Diante desse cenário, o GeoMap propõe a utilização de Inteligência Artificial e processamento digital de imagens para automatizar parte dessa análise, utilizando a segmentação semântica para identificar e delimitar elementos presentes nas imagens aéreas.

## Objetivo do projeto

Desenvolver uma solução computacional capaz de processar imagens aéreas obtidas por drones e utilizar modelos de Inteligência Artificial para identificar diferentes elementos presentes nas cenas.

A implementação inicial concentra-se na segmentação semântica, estabelecendo uma base tecnológica para futuras funcionalidades relacionadas à interpretação territorial e à análise de terrenos.

## Conjunto de dados utilizado

### Semantic Drone Dataset

O Semantic Drone Dataset é um conjunto de imagens aéreas obtidas por drones, acompanhado de informações de segmentação semântica.

O conjunto apresenta imagens de alta resolução e diferentes classes de elementos presentes nas cenas, sendo utilizado como referência para o desenvolvimento e a experimentação de modelos de segmentação de imagens.

## Fonte dos dados

**Graz University of Technology (TU Graz)**

O conjunto de dados foi desenvolvido para pesquisas relacionadas à compreensão semântica de imagens aéreas obtidas por drones.

### Links para as fontes originais

- [Página oficial do Semantic Drone Dataset – TU Graz](https://ivc.tugraz.at/research-project/semantic-drone-dataset/)
- [Semantic Drone Dataset – Kaggle](https://www.kaggle.com/datasets/awsaf49/semantic-drone-dataset)

## Preparação e tratamento dos dados

Durante a etapa de preparação dos dados, foram processadas **400 imagens** do conjunto de treinamento.

As imagens originais apresentavam resolução de **6000 × 4000 pixels** e foram redimensionadas para **1280 × 853 pixels**, mantendo aproximadamente a proporção original.

O tratamento foi realizado utilizando **Python** e a biblioteca **Pillow**, por meio do script:

```text
src/preprocessing.py
```

Essa etapa teve como objetivo adequar as imagens às necessidades do processamento computacional e preparar os dados para as etapas posteriores de desenvolvimento do modelo.

## Implementação da Inteligência Artificial

Após a preparação dos dados, o projeto avançou para a implementação experimental de um modelo de segmentação semântica.

Foi utilizada a arquitetura **YOLO11s-seg**, voltada à identificação e delimitação de objetos e regiões presentes nas imagens.

O modelo foi configurado para trabalhar inicialmente com três classes:

| Classe | Elemento identificado |
|---|---|
| Construção | Estruturas e edificações |
| Vegetação | Áreas com cobertura vegetal |
| Via | Vias e superfícies destinadas à circulação |

O treinamento documentado foi realizado ao longo de **100 épocas**, utilizando imagens com resolução de entrada de 640 × 640 pixels e tamanho de lote (batch size) igual a 8.

Essa implementação representa uma etapa experimental do GeoMap, permitindo verificar a aplicação da segmentação semântica em imagens aéreas.

## Avaliação experimental

Além do treinamento, foi realizada uma avaliação experimental em **29 de outubro de 2026**, utilizando dez imagens próprias obtidas por drone.

Para essa análise, foram utilizados pesos de um modelo previamente treinado, com o objetivo de verificar seu comportamento diante de imagens aéreas diferentes daquelas utilizadas como referência durante o desenvolvimento.

Os resultados gerais obtidos foram:

| Métrica | Resultado |
|---|---:|
| Mean Intersection over Union (mIoU) | 51,77% |
| Mean Dice Coefficient (mDice) | 67,59% |

### Resultados por classe

| Classe | IoU | Dice |
|---|---:|---:|
| Construção | 52,56% | 68,90% |
| Vegetação | 64,15% | 78,16% |
| Via | 38,60% | 55,70% |

Os resultados demonstraram diferenças de desempenho entre as categorias avaliadas. A classe vegetação apresentou os melhores índices, enquanto a classe via apresentou maior dificuldade de identificação e delimitação.

É importante destacar que esses valores correspondem à avaliação experimental realizada com dez imagens próprias e não representam uma avaliação definitiva da capacidade de generalização do modelo.

## Tecnologias e ferramentas utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento e processamento dos dados |
| Pillow | Redimensionamento e tratamento de imagens |
| YOLO11s-seg | Modelo de segmentação semântica |
| Ultralytics | Utilização e execução do modelo |
| OpenCV | Manipulação e processamento de imagens |
| Git e GitHub | Controle de versão e armazenamento do projeto |

## Estrutura do projeto

```text
GeoMap/
│
├── data/
│   └── README.md
│
├── docs/
│   ├── TED IA-1.pdf
│   ├── TED 02 BIGDATA.pdf
│   └── TED 03.pdf
│
├── src/
│   ├── main.py
│   └── preprocessing.py
│
├── .gitignore
└── README.md
```

A estrutura apresenta a organização geral da documentação, dos dados e dos códigos-fonte. Outros scripts e arquivos de resultados podem ser incorporados conforme a evolução da implementação.

## Documentação acadêmica

Os documentos produzidos durante o desenvolvimento acadêmico do projeto estão organizados na pasta `docs/`.

- **TED 01 – Inteligência Artificial:** planejamento inicial, definição do problema e proposta de solução.
- **TED 02 – Big Data:** pesquisa, seleção e caracterização do conjunto de dados.
- **TED 03 – Desenvolvimento e avaliação:** implementação experimental do modelo de segmentação e análise dos resultados obtidos.

## Limitações e trabalhos futuros

A implementação atual concentra-se na identificação de três classes: construção, vegetação e via.

Embora a proposta inicial contemple outros elementos, como solo e pedras, essas categorias ainda não fazem parte da configuração experimental documentada.

Como possibilidades de evolução, destacam-se:

- Ampliação da quantidade de classes identificadas.
- Melhoria da precisão da segmentação.
- Realização de avaliações com conjuntos maiores de imagens próprias.
- Incorporação de recursos de análise topográfica.
- Desenvolvimento de funcionalidades para auxiliar na interpretação de terrenos.

## Considerações finais

O GeoMap encontra-se em desenvolvimento experimental, tendo avançado desde a definição do problema e a preparação dos dados até a implementação e avaliação de um modelo de segmentação semântica.

Os resultados obtidos demonstram a viabilidade inicial da utilização de Inteligência Artificial no processamento de imagens aéreas, estabelecendo uma base para o desenvolvimento de novas funcionalidades e aprimoramentos futuros.


## Codigos do projeto
Os códigos-fonte utilizados na preparação dos dados, treinamento e experimentação do modelo de segmentação estão organizados no repositório desenvolvido para a disciplina de Inteligência Artificial. O presente repositório concentra a documentação geral do GeoMap, a descrição do conjunto de dados, os resultados experimentais e a evolução do projeto.

A separação entre os repositórios permite manter a organização dos materiais acadêmicos e evitar a duplicação desnecessária de arquivos.

Link do repositório: https://github.com/ggstv-dl/Analise-Matricial