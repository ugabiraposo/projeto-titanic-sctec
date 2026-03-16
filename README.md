# Projeto Final | Análise Exploratória de Dados do Titanic 🚢

<p align="center">
  <img src="imagens/logo_sctec.png" alt="Logo SCTEC" width="300">
</p>

Este repositório foi criado para documentar o desenvolvimento do meu **projeto final de Análise Exploratória de Dados**, construído em Python a partir do dataset **Titanic**. O projeto foi desenvolvido com fins estudantis como parte da atividade prática extra do curso **Introdução ao Data Science**, pertencente à trilha rápida de **Análise de Dados**.

Ao longo deste projeto, apliquei na prática conteúdos estudados durante a formação, como leitura de arquivos CSV, exploração inicial dos dados, tratamento de valores nulos, identificação de duplicidades, filtros, ordenações, agrupamentos com `groupby` e geração de visualizações. A proposta central foi transformar dados brutos em informações mais claras, organizadas e visuais, buscando identificar padrões relevantes relacionados à sobrevivência dos passageiros.

## Objetivo

O principal objetivo deste projeto foi desenvolver uma análise exploratória clara, organizada e coerente a partir de uma base de dados real, colocando em prática conceitos fundamentais da área de dados. Além de explorar o comportamento do dataset Titanic, a intenção também foi demonstrar minha evolução técnica durante a trilha e minha capacidade de estruturar um projeto analítico com documentação, tratamento de dados e visualizações.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib

## O que foi desenvolvido

Durante a análise, foram realizadas etapas importantes para a compreensão e organização do dataset. Entre elas:

- leitura do arquivo CSV
- visualização das primeiras linhas da base
- análise das informações gerais das colunas
- verificação dos tipos de dados
- estatísticas descritivas
- identificação de valores nulos
- verificação e remoção de duplicidades
- tratamento de dados ausentes
- aplicação de filtros e ordenações
- agrupamentos com `groupby`
- geração de gráficos para apoiar a interpretação dos resultados

## Tratamento dos dados

Antes de iniciar a parte visual e interpretativa, foi necessário fazer uma preparação básica da base. Alguns campos apresentavam valores ausentes, então foram aplicadas soluções simples e coerentes para manter a consistência da análise.

As principais decisões foram:

- preenchimento da coluna de idade com a mediana
- preenchimento da coluna de embarque com a moda
- substituição dos valores ausentes da cabine por `Não informado`
- remoção de linhas duplicadas

Além disso, foi criada uma nova coluna chamada **Faixa_Etaria**, classificando os passageiros em:

- Criança
- Jovem
- Adulto
- Idoso

Essa etapa ajudou a enriquecer a análise e tornou mais fácil visualizar a distribuição etária da base.

## Análises realizadas

As análises desenvolvidas neste projeto buscaram explorar relações importantes entre as variáveis do dataset. Entre os pontos analisados, estão:

- distribuição geral de sobrevivência
- taxa de sobrevivência por sexo
- tarifa média por classe
- distribuição dos passageiros por faixa etária
- quantidade de pessoas em cada classe
- quantidade de sobreviventes de acordo com a classe

## Visualizações geradas

Para complementar a análise e tornar os resultados mais fáceis de interpretar, foram gerados gráficos com foco em leitura rápida e comparação visual.

Os gráficos produzidos foram:

- gráfico de barras da sobrevivência geral
- gráfico de barras da taxa de sobrevivência por sexo
- gráfico de barras da tarifa média por classe
- gráfico de pizza da distribuição por faixa etária
- gráfico de barras da quantidade de pessoas por classe
- gráfico de barras da quantidade de sobreviventes por classe

## Principais insights

A análise mostrou que algumas variáveis possuem forte relação com a sobrevivência dos passageiros.

Entre as percepções mais relevantes, destaco:

- mulheres apresentaram taxa de sobrevivência maior do que homens
- a classe dos passageiros influenciou tanto o valor da tarifa quanto os índices de sobrevivência
- a distribuição por faixa etária ajudou a compreender melhor o perfil dos passageiros
- o tratamento dos valores nulos foi importante para evitar distorções na análise
- filtros, agrupamentos e gráficos foram essenciais para transformar os dados em informações mais claras

Mesmo sendo um projeto introdutório, foi possível perceber como uma base de dados real pode gerar análises interessantes quando passa por etapas mínimas de organização, limpeza e visualização.

## Certificação

Este projeto também representa a aplicação prática dos conhecimentos desenvolvidos durante o curso **Introdução ao Data Science**, realizado no **SENAI/SC - LAB 365 Florianópolis**, com **20 horas** de duração.

Ao longo da formação, foram trabalhados conteúdos essenciais para a construção deste projeto, como:

- introdução a Python para dados
- coleta e tratamento de dados
- visualização de dados
- prática com SQL, APIs e noções de nuvem

<p align="center">
  <img src="imagens/certificado.png" alt="Certificado do curso Introdução ao Data Science - SENAI" width="500">
</p>

## Conclusão

Este projeto foi uma oportunidade importante para aplicar, de forma prática, conteúdos fundamentais estudados ao longo da trilha rápida de **Análise de Dados**. Mais do que apenas executar comandos em Python, o desenvolvimento deste trabalho me permitiu exercitar raciocínio analítico, organização de projeto, interpretação de dados e documentação técnica.

Por ter sido desenvolvido com fins educacionais e também como parte de um processo seletivo, este projeto representa um passo importante na minha trajetória de aprendizado na área de dados e reforça meu interesse em continuar evoluindo tecnicamente por meio do **SCTEC**.

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/SEU-USUARIO/projeto-titanic-sctec.git
