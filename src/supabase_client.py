import logging
from supabase import create_client

def get_contacts(supabase_url, supabase_key, limit=3):
    try:
        supabase = create_client(supabase_url, supabase_key)
        response = supabase.table("contacts").select("name, phone").limit(limit).execute()
        return response.data
    except Exception as e:
        logging.error(f"Erro ao buscar contatos: {e}")
        raise