# GeoMap — Processamento e Segmentação de Imagens Aéreas

## Integrantes da equipe

- Gustavo Barros Martins
- Hugo Alexandre Carvalho Coelho Coutinho
- Jeferson Machado dos Santos
- Maicon de Sousa Pontes

---

## Descrição do problema

O projeto busca solucionar um problema enfrentado por um engenheiro autônomo relacionado ao elevado tempo necessário para realizar atividades de análise e interpretação de terrenos.

Atualmente, parte dessas atividades pode envolver a análise manual de imagens aéreas obtidas por drones, exigindo que o profissional identifique visualmente diferentes elementos presentes no terreno, como solo, vegetação, pedras, áreas pavimentadas e construções.

Esse processo pode consumir bastante tempo e estar sujeito a erros de interpretação, principalmente quando existe uma grande quantidade de imagens para analisar.

Dessa forma, o projeto propõe a utilização de técnicas de Inteligência Artificial e processamento digital de imagens para automatizar parte desse processo.

---

## Solução proposta

O GeoMap tem como objetivo desenvolver uma solução capaz de analisar imagens aéreas obtidas por drones e realizar a **segmentação semântica** dos elementos presentes no terreno.

A partir de uma imagem, o sistema deverá ser capaz de identificar diferentes regiões e classificá-las de acordo com suas características.

Entre os elementos que poderão ser identificados estão:

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

A proposta é utilizar um modelo de Inteligência Artificial treinado com imagens previamente classificadas para aprender a identificar esses diferentes elementos de forma automática.

---

## MVP

O MVP inicial do projeto será concentrado na **segmentação semântica de imagens aéreas**.

O sistema deverá receber uma imagem obtida por drone e produzir uma representação segmentada, na qual diferentes regiões da imagem serão classificadas de acordo com os elementos identificados.

### Fluxo previsto

```text
Imagem aérea
     ↓
Pré-processamento
     ↓
Modelo de Inteligência Artificial
     ↓
Segmentação semântica
     ↓
Classificação dos elementos
     ↓
Imagem segmentada