# b2bflow Challenge

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Supabase](https://img.shields.io/badge/Supabase-Integração-green)](https://supabase.com/)
[![Z-API](https://img.shields.io/badge/Z--API-WhatsApp-orange)](https://z-api.io/)

Solução para o desafio técnico da b2bflow. O sistema lê contatos da tabela `contacts` no Supabase e envia mensagens personalizadas via Z-API (WhatsApp), com tratamento básico de erros e logs.

## Funcionalidades

- Leitura de até 3 contatos da tabela `contacts` no Supabase.
- Envio de mensagem no formato `"Olá, <nome> tudo bem com você?"` para cada contato.
- Logs estruturados no console (nível INFO).
- Validação de variáveis de ambiente no início da execução.
- Tratamento de erros em operações de rede e banco.

## Estrutura do Projeto

```
.
├── .env                 # Variáveis de ambiente (não versionado)
├── .gitignore
├── requirements.txt
├── main.py              # Ponto de entrada
└── src/
    ├── __init__.py
    ├── config.py        # Carregamento e validação do .env
    ├── supabase_client.py
    └── zapi_client.py
```

## Pré-requisitos

- Python 3.8+
- Conta no Supabase (plano gratuito)
- Conta na Z-API (plano gratuito)
- WhatsApp instalado no celular

## Configuração

1. Clone o repositório:

```bash
git clone https://github.com/iz-brum/b2bflow-challenge.git
cd b2bflow-challenge
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate          # Linux/Mac
# ou .\venv\Scripts\activate      # Windows (cmd)
# ou source venv/Scripts/activate # Windows (Git Bash)
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` na raiz com as seguintes variáveis:

```env
SUPABASE_URL=https://seuprojeto.supabase.co
SUPABASE_KEY=sua_chave_service_role_ou_anon
ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_INSTANCE_TOKEN=seu_instance_token
```

5. Crie a tabela `contacts` no Supabase (via SQL Editor):

```sql
CREATE TABLE contacts (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);

-- Insira dados de exemplo (opcional)
INSERT INTO contacts (name, phone) VALUES 
('João Silva', '5511999999999'),
('Maria Oliveira', '5511988888888');
```

6. Configure a instância na Z-API:
   - Crie uma instância no painel da Z-API.
   - Conecte escaneando o QR Code com o WhatsApp.
   - Copie o `Instance ID` e `Instance Token` para o `.env`.

## Uso

Execute o script principal:

```bash
python main.py
```

O programa irá:
- Buscar até 3 contatos no Supabase.
- Para cada contato, enviar a mensagem personalizada via Z-API.
- Registrar logs de sucesso ou falha.

## Exemplo de saída

```
2026-06-16 16:12:03,861 - INFO - Buscando contatos no Supabase...
2026-06-16 16:12:04,412 - INFO - Encontrados 1 contato(s). Iniciando envios...
2026-06-16 16:12:04,816 - INFO - Mensagem enviada para 5565999999999
2026-06-16 16:12:04,817 - INFO - Enviado para João Silva (5565999999999)
2026-06-16 16:12:05,818 - INFO - Processo finalizado.
```

## Observações

- O projeto foi desenvolvido para atender aos requisitos do desafio.
- A Z-API em modo trial adiciona um aviso às mensagens enviadas, o que é esperado.
- Para uso em produção, considere adicionar retry, logs persistentes e monitoramento.

## Licença

MIT
