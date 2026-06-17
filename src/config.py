import os
from dotenv import load_dotenv

load_dotenv()

def get_env_vars():
    return {
        "SUPABASE_URL": os.getenv("SUPABASE_URL"),
        "SUPABASE_KEY": os.getenv("SUPABASE_KEY"),
        "ZAPI_INSTANCE_ID": os.getenv("ZAPI_INSTANCE_ID"),
        "ZAPI_INSTANCE_TOKEN": os.getenv("ZAPI_INSTANCE_TOKEN"),
    }

def validate_env(env):
    missing = [k for k, v in env.items() if not v]
    if missing:
        raise EnvironmentError(f"Variáveis faltando: {', '.join(missing)}")