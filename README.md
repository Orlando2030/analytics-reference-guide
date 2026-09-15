# Analytics Reference Guide

![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Guia prático de estudos e revisão sobre Ciência de Dados, Análise Exploratória de Dados, Estatística, Visualização, Aprendizado de Máquina e Séries Temporais.

Os exemplos combinam explicações conceituais, bases de dados locais e notebooks executáveis em Python.

## Conteúdo

### 1. Fundamentos

Local: `1_fundamentos/`

- `01_fundamentos_programacao_python.ipynb`: lógica e manipulação de dados em Python.
- `02_analise_exploratoria_de_dados.ipynb`: limpeza, transformação e estatística descritiva.
- `03_visualizacao_de_dados.ipynb`: gráficos com Matplotlib e Seaborn.
- `04_estatistica_ciencia_dados.ipynb`: fundamentos estatísticos e probabilidade.

Arquivos de apoio:

- `alunos.csv` e `alunos_final.csv`: exemplos tabulares.
- `dados.json` e `nomes.txt`: exemplos de leitura e processamento de dados.

### 2. Machine Learning e Modelagem

Local: `2_machine_learning_e_modelagem/`

#### Aprendizado não supervisionado

Local: `2_1_Unsupervised/`

- `05_clustering.ipynb`: agrupamento, inércia, método do cotovelo e silhueta.
- `06_PCA.ipynb`: redução de dimensionalidade com PCA.
- `07_Analise_Fatorial_Exploratoria.ipynb`: análise fatorial exploratória.

#### Aprendizado supervisionado

Local: `2_2__Supervised/`

- Regressão linear simples, múltipla, não linear e com variável explicativa temporal.
- Modelos logísticos e modelagem multinível.
- Visualizações interativas em HTML com Plotly.
- Bases de apoio: `bebes.csv`, `paises.csv`, `tempo_vars.csv` e `tempodist.csv`.

### 3. Análise Especializada

Local: `3_analise_especializada/`

- `09_series_temporais.ipynb`: fundamentos de séries temporais.
- `09_series_temporais_exemplos.ipynb`: exemplos práticos.
- `Series_Temporais.py`: implementação complementar.
- `airpassengers.xlsx`: base utilizada nos exemplos.

### Ferramentas auxiliares

- `generate_diagrams.py`: geração de diagramas de apoio.
- `requirements.txt`: dependências Python do projeto.

## Pré-requisitos

- Python 3.13 ou versão compatível.
- pip disponível no ambiente Python.

## Instalação

Execute os comandos no diretório raiz do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Executar os notebooks

Com o ambiente virtual ativado:

```bash
jupyter lab
```

Também é possível iniciar o Jupyter Notebook clássico:

```bash
jupyter notebook
```

Para encerrar o ambiente virtual:

```bash
deactivate
```

## Fluxo recomendado de estudos

1. Fundamentos de Python e análise exploratória.
2. Visualização e estatística.
3. Modelos supervisionados e não supervisionados.
4. PCA e análise fatorial.
5. Séries temporais.

Execute os notebooks na ordem apresentada dentro de cada seção. Alguns exemplos dependem de arquivos locais; mantenha as bases na mesma estrutura de diretórios do repositório. O pacote `yfinance` também pode realizar consultas externas quando utilizado.

## Dependências principais

- Análise de dados: pandas, NumPy e SciPy.
- Modelagem: scikit-learn, statsmodels, Pingouin e factor-analyzer.
- Visualização: Matplotlib, Seaborn, Plotly, Pillow, imageio e NetworkX.
- Finanças: yfinance.
- Notebooks: JupyterLab, Jupyter Notebook e ipykernel.

## Licença

Este projeto está disponível sob a [Licença MIT](LICENSE).

**Autor:** Orlando Santos de Oliveira

