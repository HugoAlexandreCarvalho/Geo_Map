# Processamento Digital de Imagens Aéreas e Análise Topográfica Matricial via Python e WebODM
# Geomap
## Integrantes da equipe

- Gustavo Barros Martins
- Hugo Alexandre Carvalho Coelho Coutinho
- Jeferson Machado dos Santos
- Maicon de Sousa Pontes

## Descrição do problema

O projeto busca solucionar um problema enfrentado por um engenheiro autônomo relacionado ao elevado tempo necessário para realizar algumas atividades técnicas.

Entre os principais problemas estão o mapeamento manual de terrenos e a análise de dados de elevação, atividades que podem consumir bastante tempo e estar sujeitas a erros humanos de interpretação.

Embora os drones tenham facilitado a coleta de dados em campo, o grande volume de informações geradas, especialmente matrizes de elevação, pode tornar o processamento e a análise dos dados um novo gargalo.

Dessa forma, o projeto propõe a utilização de Python, WebODM, processamento de imagens e análise matricial para automatizar parte desse processo, buscando identificar características do terreno, como áreas planas e regiões de interesse para análise.

## Conjunto de dados utilizado

O projeto utilizará um conjunto de dados composto por imagens aéreas obtidas por drones e informações relacionadas ao seu georreferenciamento.

Esses dados serão utilizados para gerar e analisar informações topográficas do terreno, incluindo modelos digitais de elevação e ortomosaicos.

### Base de dados

**Nome:** ODMData

**Descrição:** conjunto de datasets disponibilizados pelo projeto OpenDroneMap para utilização em testes e processamento de imagens aéreas obtidas por drones.

## Fonte dos dados

Os dados são disponibilizados pelo projeto **OpenDroneMap**, uma plataforma de código aberto voltada ao processamento de imagens obtidas por drones e à geração de produtos fotogramétricos.

## Link para a fonte original

- OpenDroneMap – Datasets:
  https://opendronemap.org/odm/datasets/

- Repositório oficial do ODMData:
  https://github.com/OpenDroneMap/ODMdata

## Instruções para obtenção dos dados

Os dados podem ser obtidos diretamente na página oficial do OpenDroneMap:

https://opendronemap.org/odm/datasets/

O conjunto de dados selecionado deverá ser baixado e armazenado na pasta `dataset/` do projeto.

A estrutura poderá ser organizada da seguinte forma:

```text
├── README.md
├── docs/
│   └── TED01.pdf
├── data/
│   └── dataset/
└── src/
    └── main.py