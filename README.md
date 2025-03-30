**Introdução**

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

CREATE TABLE raw_patient (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    birth_date DATE,
    gender VARCHAR(20),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    phone_number VARCHAR(20),
    email VARCHAR(100),
    emergency_contact_name VARCHAR(200),
    emergency_contact_phone VARCHAR(20),
    blood_type VARCHAR(5),
    insurance_provider VARCHAR(100),
    insurance_number VARCHAR(50),
    marital_status VARCHAR(20),
    preferred_language VARCHAR(50),
    nationality VARCHAR(100),
    allergies TEXT,
    last_visit_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TI
MESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TI
MESTAMP
 )

Tabela fhir_patient

CREATE TABLE fhir_patient (
    id VARCHAR(255) PRIMARY KEY, -- Unique ID generated fr
om patient attributes
    full_name VARCHAR(200), 
    birth_date DATE,
    gender VARCHAR(20),
    address VARCHAR(255),
    telecom JSONB, -- JSON object with two fields, phone a
nd email
    marital_status VARCHAR(20),
    insurance_number VARCHAR(255),
    nationality VARCHAR(20)
);

2. Ingestão de Dados
   
Executar comando "python Part2_DataIngestion.py"

3. Transformação de Dados
   
Executar comando "python Part3_DataTransformation.py"
