# Radix_desafio
Desafio de código da radix-engenharia

# Projeto de Coleta de Dados em Tempo Real

Este projeto foi desenvolvido utilizando Docker Compose, em python com flask, visando coletar e armazenar dados de equipamentos que enviam informações em formato JSON para um endpoint. Além disso, o projeto permite o upload de arquivos CSV para preencher lacunas nos dados coletados.

## Requisitos
-- se estiver usando o windows, deve ter o wls instalado:
-- https://learn.microsoft.com/pt-br/windows/wsl/install

## Estrutura do Projeto

- **API**: Endpoint para receber dados em tempo real e processar arquivos CSV.
- **Banco de Dados**: Armazena os dados recebidos.
- **Interface de Visualização**: Exibe gráficos com médias dos sensores.

## Funcionalidades

1. **Recepção de Dados**:
   - Endpoint para receber dados em JSON.
   - Exemplo de payload:
     ```json
     {
       "equipmentId": "EQ-12495",
       "timestamp": "2023-02-15T01:30:00.000-05:00",
       "value": 78.42
     }
     ```

2. **Upload de CSV**:
   - Endpoint para upload de arquivos CSV com dados de sensores.
   - O formato do CSV deve seguir a estrutura:
     ```
     equipmentId;timestamp;value
     EQ-12495;2023-02-12T01:30:00.000-05:00;78.8
     EQ-12492;2023-01-12T01:30:00.000-05:00;8.8
     ```

3. **Média dos Sensores**:
   - Tela para exibir o valor médio dos sensores nas últimas 24 horas, 48 horas, 1 semana e 1 mês.
   - Gráficos para facilitar a análise.

4. **Documentação**:
   - Documentação da API e do sistema como um todo.

## Tecnologias Utilizadas

- **Docker**: Containerização da aplicação.
- **Python**: Backend para criação da API.
- **PostgreSQL**: Banco de dados para armazenamento dos dados coletados.
- **Chart.js**: Biblioteca para gráficos na interface.
- **HTML**: Linguagem de marcação.

## Como Executar o Projeto

**Clone do Repositório e Execução do app**:
   
git clone https://github.com/lukaslamim/Radix_desafio

docker compose -f "docker-compose.yml" up -d --build 

http:/localhost:5000/



