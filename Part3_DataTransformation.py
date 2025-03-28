import psycopg2
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

def transform_to_fhir():
    try:
        # Conexão com o PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()

        # Transforma e insere os dados
        cur.execute("""
            INSERT INTO fhir_patient (
                id, full_name, birth_date, gender, address,
                telecom, marital_status, insurance_number, nationality
            )
                    SELECT
                        (COALESCE(first_name, '') || COALESCE(last_name, '') || COALESCE(email, '') || COALESCE(phone_number, '')),
                        /* md5(
                             COALESCE(first_name, '') || 
                             COALESCE(last_name, '') || 
                             COALESCE(email, '') || 
                             COALESCE(phone_number, '')
                             ),*/
                        first_name || ' ' || last_name,
                        birth_date,
                        gender,
                        address,
                        jsonb_build_object('phone', phone_number, 'email', email),
                        marital_status,
                        insurance_number,
                        nationality
                    FROM raw_patient;
                """)

        conn.commit()
        print("✅ Dados transformados e inseridos com sucesso na tabela fhir_patient.")
    
    except Exception as e:
        print(f"❌ Erro durante transformação: {e}")
    
    finally:
        cur.close()
        conn.close()

transform_to_fhir()
