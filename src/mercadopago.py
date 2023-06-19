import requests
import json
from chave import URL
from funcoes import bot
from mapa_frete import calcular_distancia2,valor_total

x, y, Produto = valor_total

def delete_updates(data, x):
    requests.get(URL['url'] + 'getUpdates', params={'offset': data['update_id'] + x})

valor = 0
access_token = "TEST-5996788941634309-090922-8b2c6528e962f604e7b8cf33213ccb45-219918384"
token_conf = "895632123456789-aaaab"

def criar_preferencia(x):
    url = 'https://api.mercadopago.com/checkout/preferences'
    notification_url = f"{URL['url']}sendMessage?chat_id=5659082940&text=Pagamento+confirmado.+Token:+{token_conf},+valor:+{valor}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    payload = {
        "items": [
            {
                "title": "Meu Produto",
                "quantity": 1,
                "unit_price": 75.76
            }
        ],
        
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    payment_link = data['init_point']
    print(json.dumps(data, indent=1))
    print(payment_link)

    return payment_link, data['id']


def check_payment_status(payment_id):
    url = f"https://api.mercadopago.com/v1/payments/{payment_id}"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    status = data['status']

    return status


continuar_pag = True

while continuar_pag:
    x = ''
    while 'result' not in x:
        try:
            x = json.loads(requests.get(URL['url'] + 'getUpdates').text)
        except Exception as e:
            x = ''
            if 'Failed to establish a new connection' in str(e):
                print('Perda de conexão')
            else:
                print('Erro desconhecido: ' + str(e))

        if len(x['result']) > 0:
            for datas in x['result']:
                delete_updates(datas, 1)

                print(json.dumps(datas, indent=1))

            if datas['message']['text'] == 'O':
                payment_link, payment_id = criar_preferencia()
                print(f"Realize o pagamento através deste link: {payment_link}")

                status = check_payment_status(payment_id)
                if status == 'approved':
                    print("Pagamento aprovado.")
                    requests.post(URL['url'] + 'sendmessage', {'chat_id': datas['message']['chat']['id'], 'text': 'Seu pagamento foi aprovado!'})
                elif status == 'rejected':
                    print("Pagamento recusado.")
                    requests.post(URL['url'] + 'sendmessage', {'chat_id': datas['message']['chat']['id'], 'text': 'Seu pagamento foi recusado!'})
                else:
                    print("Status do pagamento desconhecido.")

                continuar_pag = False  # Exit the loop after processing the payment



