**Introduçãp**
Este projeto consiste na ingestão e transformação de dados de pacientes a partir de um ficheiro CSV, com carregamento para uma base de dados PostgreSQL e conversão para o formato FHIR.

**Estrutura do Projeto**
├── .env                    # Configurações de acesso à base de dados
├── patient.csv             # Ficheiro com dados brutos dos pacientes
├── ingestion.py            # Script para carregar e validar os dados no PostgreSQL
├── part3_transform.py      # Script para transformar os dados para o formato FHIR
├── requirements.txt        # Bibliotecas necessárias para executar os scripts
├── data_assets.yaml        # Documentação das tabelas raw_patient e fhir_patient
├── README.md               # Este ficheiro

**Pré-Requisitos**
- Python 3.8+
- PostgreSQL instalado e a correr localmente
- Instalar dependências - Correr comando "pip install -r requirements.txt"

**Passos**
1. Criação de tabelas - Executar os comandos SQL no PostgreSQL
Tabela raw_patient

Tabela fhir_patient

2. Ingestão de Dados 
Executar comando "python Part2_DataIngestion.py"

3. Transformação de Dados
Executar comando "python Part3_DataTransformation.py"