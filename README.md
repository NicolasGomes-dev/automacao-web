# Projeto de Automação com Python

Este projeto automatiza o cadastro de produtos em um sistema web utilizando python.

## Funcionalidades 

- Abre o navegador e acessa o sistema de cadastro.
- Realiza o login automaticamente
- Lê uma base de dados de produtos a partir de um arquivo "produtos.csv".
- Preenche e cadastra cada produto no sistema de forma automática.

## Como usar

1. **Pré-requisitos**
    - Python 3 instalado
    - Instale as dependências:
    '''
    pip install pyautogui pandas
    '''

2. **Prepare o arquivo "produtos_csv"**
    O arquivo deve conter as colunas: 'codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo', 'obs'.

3. **Execute o script:**
    '''
    python auto.py
    '''

4. **Atenção**
    - Ajuste as coordenadas dos clicks conforme a posição dos campos do seu navegador.
    - Não mova o mouse nem o teclado durante a execução do script.

## Estrutura dos arquivos

- 'auto.py' - Script principal de automação
- 'produtos.csv' - Base de dados dos produtos a serem cadastrados.
- 'README.md' - Este arquivo de instruções.

## Observações 

- O projeto é para fins educacionais e pode ser adaptado para outros sistemas de cadastro.
- Certifique-se que o nevegador e o sistema estejam acessíveis antes de rodar o script.

 
