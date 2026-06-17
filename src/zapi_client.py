import logging
import requests

def send_message(phone, message, instance_id, token):
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    payload = {"phone": phone, "message": message}
    try:
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        logging.info(f"Mensagem enviada para {phone}")
        return True
    except Exception as e:
        logging.error(f"Erro ao enviar para {phone}: {e}")
        return False