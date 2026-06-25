import requests
import time
def req(base_url):
    try:
        # obter o valor da transação
        response_valor = requests.get(f"{base_url}/value")
        response_valor.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        valor = response_valor.text.strip()

        # obter o ID da transação
        response_id = requests.get(f"{base_url}/id")
        response_id.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        id_transacao = response_id.text.strip()

        if valor.startswith("R$ "):
            valor_formatado = valor[len("R$ "):].replace(',', '.').strip()
        else:
            print("Formato do valor não reconhecido.")
            valor_formatado = None

        return valor_formatado, id_transacao

    except requests.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None, None
