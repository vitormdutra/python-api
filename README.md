# Weather App

## Descrição

O Weather App é uma aplicação simples que utiliza FastAPI para fornecer informações sobre o clima com base no nome da cidade e no código do país fornecidos pelo usuário. A aplicação frontend é uma interface HTML que permite ao usuário consultar dados meteorológicos de uma API.

## Estrutura do Projeto

- **Backend (API)**: Implementado com FastAPI.
- **Frontend**: HTML e JavaScript para interagir com a API e exibir os dados meteorológicos.

## Funcionalidades

- **Obter Previsão do Tempo**: Fornece informações como temperatura, umidade, descrição do clima e velocidade do vento para uma cidade e país específicos.
- **Interface Simples**: Permite ao usuário inserir o nome da cidade e o código do país e exibe os dados meteorológicos.

## Requisitos

- Python 3.7 ou superior
- FastAPI
- Uvicorn
- Requests
- Cachetools

## Configuração

### Backend

1. **Instale as dependências**:

    ```bash
    pip install fastapi uvicorn requests cachetools
    ```

2. **Configuração da Chave da API**:

    Defina a variável de ambiente `OPENWEATHERMAP_API_KEY` com sua chave de API do OpenWeatherMap. No Linux ou macOS, você pode adicionar a seguinte linha ao seu arquivo `.bashrc` ou `.zshrc`:

    ```bash
    export OPENWEATHERMAP_API_KEY='sua-chave-aqui'
    ```

    No Windows, você pode definir a variável de ambiente nas configurações do sistema ou usar o comando `set` no prompt de comando.

3. **Execute o Servidor**:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

    Substitua `main` pelo nome do arquivo Python onde está definido o aplicativo FastAPI.

### Frontend

1. **HTML e CSS**: O frontend está em um arquivo HTML que inclui CSS básico para estilização e JavaScript para interagir com a API.

2. **Abrir a Interface**:

    Abra o arquivo HTML em um navegador para usar a aplicação. A interface permitirá que você insira o nome da cidade e o código do país, e mostrará os dados meteorológicos na tela.

## Uso

1. **Acesse a Interface**:

    Abra o arquivo HTML em um navegador. Você verá um formulário para inserir a cidade e o código do país.

2. **Consulta de Dados**:

    Insira o nome da cidade e o código do país e clique no botão "Get Weather". Os dados meteorológicos serão exibidos na seção abaixo do formulário.

## Exemplos

- **Consulta**: 
    - Cidade: `London`
    - Código do País: `GB`

    Resultará na exibição de informações como a temperatura atual, umidade e descrição do clima para Londres.

## Mensagens de Erro

- **Invalid API Key**: Se a chave da API for inválida.
- **Failed to fetch weather data**: Se ocorrer um problema ao buscar os dados meteorológicos.
- **An unknown error occurred**: Para qualquer outro erro desconhecido.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
