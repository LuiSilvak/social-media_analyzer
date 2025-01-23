# Analisador de Dados de Redes Sociais

## Descrição

Este projeto é um analisador de dados de redes sociais que permite extrair, processar e visualizar informações como engajamento (curtidas, compartilhamentos, comentários) e crescimento de seguidores. É ideal para auxiliar na análise de métricas de performance e na tomada de decisões estratégicas em campanhas digitais.

## Funcionalidades

- Importação de dados de redes sociais a partir de arquivos CSV.
- Processamento de métricas como curtidas, comentários e compartilhamentos.
- Visualização de tendências de crescimento de seguidores.
- Geração de gráficos interativos para facilitar a análise.
- Estatísticas sumarizadas para cada rede social.

## Pré-requisitos

Certifique-se de que você tenha os seguintes requisitos instalados no seu ambiente:

1. Python 3.7 ou superior.
2. Bibliotecas necessárias:
    - pandas
    - matplotlib
    - seaborn

Você pode instalar as dependências utilizando o comando:

```bash
    pip install pandas matplotlib seaborn
```

## Como Usar

1. Clone este repositório:

```bash
    git clone https://github.com/LuiSilvak/social-media_analyzer.git
    cd social-media_analyzer
```

2. Certifique-se de ter um arquivo CSV contendo os dados das redes sociais. O arquivo deve conter, no mínimo, as seguintes colunas:

    - Data
    - Curtidas
    - Compartilhamentos
    - Comentarios
    - Seguidores

3. Exemplo de formato do arquivo:

```bash
    Data,Curtidas,Compartilhamentos,Comentarios,Seguidores
    2025-01-01,120,15,10,1000
    2025-01-02,130,20,15,1020
```

4. Execute o script principal:

```bash
    python social-media_analyzer.py
```

5. Visualize as saídas no console e nos gráficos gerados.

## Exemplo de Saída

### Estatísticas Sumarizadas:

```bash
    Métricas Gerais:
    Curtidas Totais: 2345
    Compartilhamentos Totais: 320
    Comentários Totais: 210
    Crescimento Total de Seguidores: 500
```

### Gráficos Gerados:
    - Gráfico de linhas mostrando o crescimento dos seguidores ao longo do tempo.
    - Gráfico de barras comparando as curtidas, comentários e compartilhamentos por dia.

## Estrutura do Projeto

```bash
    social-media_analyzer/
    │
    ├── social-media_analyzer.py   # Script principal         # Exemplo de arquivo de dados
    ├── README.md                  # Documentação do projeto
    └── LICENSE                    # Licença do projeto
```

## Expansões Futuras

- Integração com APIs de redes sociais para coleta automática de dados (ex.: Facebook Graph API, Twitter API).
- Adicionar análises de sentimentos com base nos comentários dos usuários.
- Implementação de relatórios PDF para exportar insights gerados.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.


## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.