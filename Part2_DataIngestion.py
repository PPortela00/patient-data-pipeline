# Importa bibliotecas necessárias

import pandas as pd
import psycopg2
import re
from dotenv import load_dotenv
import os


# Carrega variáveis de ambiente do ficheiro .env
load_dotenv()

#Função para validar o formato de e-mails usando regex
def validate_email(email):
    """
    Valida o formato de um e-mail. Se estiver vazio ou nulo, retorna None.
    Lógica: usa expressão regular básica para verificar se contém "@" e domínio.
    """
    if pd.isnull(email) or str(email).strip() == "":
        return None
    
    email = str(email).strip()
    if re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        return email
    else:
        raise ValueError(f"E-mail inválido detectado: '{email}'")

def parse_date_safe(value):
    """
    Converte a string de data para datetime. Retorna None se falhar.
    """
    return pd.to_datetime(value, errors='coerce') if pd.notna(value) else None

# Função para limpar os dados do DataFrame
def clean_data(df):
    """
    Aplica validações e substituições nos dados:
    - Converte datas
    - Remove 'Unknown' de address e blood_type
    - Valida e-mails
    """
    df['birth_date'] = df['birth_date'].apply(parse_date_safe)
    df['address'] = df['address'].replace("Unknown", None)
    df['email'] = df['email'].apply(validate_email)

    # Substitui "Unknown" por None no tipo sanguíneo - para resolver problema character varying(5)
    df['blood_type'] = df['blood_type'].replace("Unknown", None)

    return df

# Função para inserir os dados limpos na BD
def insert_data(df):
    """
    Insere os dados limpos na BD.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()

        for _, row in df.iterrows():
            values = tuple(None if pd.isna(x) or x == "" else x for x in row)
            cur.execute("""
                INSERT INTO raw_patient (
                    first_name, last_name, birth_date, gender, address,
                    city, state, zip_code, phone_number, email,
                    emergency_contact_name, emergency_contact_phone,
                    blood_type, insurance_provider, insurance_number,
                    marital_status, preferred_language, nationality,
                    allergies, last_visit_date
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, values)

        conn.commit()
        print("✅ Dados inseridos com sucesso.")
    
    except Exception as e:
        print(f"❌ Erro ao inserir dados: {e}")
    
    finally:
        cur.close()
        conn.close()

df = pd.read_csv("patient.csv")      # Lê o ficheiro CSV com os dados dos pacientes         
df = clean_data(df)                  # Aplica as limpezas e validações necessárias
insert_data(df)                      # Insere os dados limpos na base de dados
