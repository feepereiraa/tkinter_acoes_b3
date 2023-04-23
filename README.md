# Filtro de ações da B3

Este é um simples projeto que busca aplicar, principalmente, as bibliotecas: selenium, tkinter e sqlite3 para criação de uma aplicação que filtra as ações de acordo
com parametros determinados pelo usuário. Nada muito complexo, apenas para monitoramento de ações que se mostrem interessantes para uma estratégia de longo prazo (buy
and hold).

## Como usar

Após o download das bibliotecas do arquivo "requirements.txt", faça o download dos arquivos "application.py", "funcionalidades.py" e "modulos.py", e rode o primeiro 
em qualquer IDE de sua prefêrencia.

### Botão "Limpar Tudo"

Limpa todos os registros da tabela à direita, assim como todos os filtros.

### Botão "Buscar"

Irá buscar pelo ticker referenciado na entry box à esquerda do próprio botão.

### Botão "Atualizar Dados"

Através da biblioteca selenium, irá abrir o Google Chrome para download dos indicadores fundamentalistas no site Status Invest.

### Botão "Magic Formula"

Este botão irá criar um ranking (melhores no topo) com as melhores ações a serem compradas de acordo com os critérios da Fórmula Mágica de Joel Greenblat.

### Checkbox "Remover Ações de Baixa Liquidez"

Este checkbox, quando ativado, irá remover as ações com liquidez abaixo do primeiro quartil da distribuição dos valores de liquidez dos tickers. Esta funcionalidade
pode ser usada tanto para a lista do botão "Gerar Lista com Restrições" quanto para o botão "Magic Formula".

### Filtros

Os filtros recebem apenas valores numéricos (ponto como divisor de casa decimal), e são validos apenas para o botão "Gerar Lista com Restrições".

### Botão "Gerar Lista com Restrições"

Este botão irá gerar uma lista de ações de acordo com os filtros estabelecidos pelo usuário.

## Requisitos

É necessário ter o Google Chrome instalado para rodar a aplicação. Além disso, você precisará instalar os seguintes pacotes:

sqlite3, tkinter, forex_python.converter, selenium, pandas, os, time, yfinance

Para isso, execute o seguinte comando dentro da pasta do arquivo:

pip install -r requirements.txt

Após isso apenas rode o arquivo "application.py"

## Contribuição

O projeto está aberto a qualquer tipo de sugestão e contribuição.
