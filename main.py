import logging
import time
from src.config import get_env_vars, validate_env
from src.supabase_client import get_contacts
from src.zapi_client import send_message

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        env = get_env_vars()
        validate_env(env)
    except EnvironmentError as e:
        logging.error(e)
        return

    try:
        logging.info("Buscando contatos no Supabase...")
        contacts = get_contacts(env["SUPABASE_URL"], env["SUPABASE_KEY"], limit=3)
    except Exception:
        logging.error("Falha ao buscar contatos. Encerrando.")
        return

    if not contacts:
        logging.warning("Nenhum contato encontrado.")
        return

    logging.info(f"Encontrados {len(contacts)} contato(s). Iniciando envios...")

    for contact in contacts:
        name = contact.get("name", "Cliente")
        phone = contact.get("phone")
        if not phone:
            logging.warning(f"Contato '{name}' sem telefone. Ignorando.")
            continue

        message = f"Olá, {name} tudo bem com você?"
        success = send_message(phone, message, env["ZAPI_INSTANCE_ID"], env["ZAPI_INSTANCE_TOKEN"])
        if success:
            logging.info(f"Enviado para {name} ({phone})")
        else:
            logging.warning(f"Falha no envio para {name} ({phone})")
        time.sleep(1)

    logging.info("Processo finalizado.")

if __name__ == "__main__":
    main()