import requests
import json
import __main__
from chave import URL, URL_File, Bot
from Lista_de_lanche import opcoes, pedido
from descricao import bigmac, bignut
from funcoes import bot
import mapa_frete 

@staticmethod
def selecionar_Hamburguer():
    continuar_ham = True
    while continuar_ham:
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
                for data in x['result']:
                    bot.delete_updates(data,1)

                    print(json.dumps(data, indent=1))

                    if data['message']['text'] == "Mais detalhe do Mac":
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bigmac})
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bignut})
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Adicionar Mac'}],
                                [{'text': 'Voltar ao menu'}],
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': "Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                        
                    elif data['message']['text'] == "Mais detalhe do Big":
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bigmac})
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bignut})
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Adicionar Big'}],
                                [{'text': 'Voltar ao menu'}],
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': "Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                    
                    elif data['message']['text'] == "Mais detalhe do Piz":
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bigmac})
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bignut})
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Adicionar Piz'}],
                                [{'text': 'Voltar ao menu'}],
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': "Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                        
                    elif data['message']['text'] == "Mais detalhe do Piz2":
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bigmac})
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bignut})
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Adicionar Piz2'}],
                                [{'text': 'Voltar ao menu'}],
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': "Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                    
                    elif data['message']['text'] == "Mais detalhe do tip1":
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bigmac})
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bignut})
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Adicionar tip1'}],
                                [{'text': 'Voltar ao menu'}],
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': 'Bebida de laranja: Uma deliciosa bebida refrescante com sabor cítrico e suculento de laranja, perfeita para saciar sua sede e despertar seus sentidos.',
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                    
                    elif data['message']['text'] == "Mais detalhe do tip2":
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bigmac})
                        requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': bignut})
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Adicionar tip2'}],
                                [{'text': 'Voltar ao menu'}],
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': 'Coca-Cola: Um clássico irresistível, a Coca-Cola é uma bebida gaseificada que combina o sabor único de uma mistura secreta de ingredientes, resultando em uma experiência de sabor refrescante e incomparável.',
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                    
                        
                    if data['message']['text'] == "Adicionar Mac":
                        pedido.append('Mac')

                        pedido_p = ''
                        for item in pedido:
                            pedido_p += f"{item}\n"

                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Cardapio'}],
                                [{'text': 'Finalizar compra'}]
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': f"Seu pedido adicionado: \n{pedido_p}",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                    
                    elif data['message']['text'] == "Adicionar Big":
                        pedido.append('Big')

                        pedido_p = ''
                        for item in pedido:
                            pedido_p += f"{item}\n"

                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Cardapio'}],
                                [{'text': 'Finalizar compra'}]
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': f"Seu pedido adicionado: \n{pedido_p}",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})

                    elif data['message']['text'] == "Adicionar Piz":
                        pedido.append('Piz')

                        pedido_p = ''
                        for item in pedido:
                            pedido_p += f"{item}\n"

                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Cardapio'}],
                                [{'text': 'Finalizar compra'}]
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': f"Seu pedido adicionado: \n{pedido_p}",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                    
                    elif data['message']['text'] == "Adicionar Piz2":
                        pedido.append('Piz2')

                        pedido_p = ''
                        for item in pedido:
                            pedido_p += f"{item}\n"

                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Cardapio'}],
                                [{'text': 'Finalizar compra'}]
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': f"Seu pedido adicionado: \n{pedido_p}",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                    
                    elif data['message']['text'] == "Adicionar tip2":
                        pedido.append('tip2')

                        pedido_p = ''
                        for item in pedido:
                            pedido_p += f"{item}\n"

                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Cardapio'}],
                                [{'text': 'Finalizar compra'}]
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': f"Seu pedido adicionado: \n{pedido_p}",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                        
                    elif data['message']['text'] == "Adicionar tip1":
                        pedido.append('tip1')

                        pedido_p = ''
                        for item in pedido:
                            pedido_p += f"{item}\n"

                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Cardapio'}],
                                [{'text': 'Finalizar compra'}]
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': f"Seu pedido adicionado: \n{pedido_p}",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                        
                    elif data['message']['text'] == "Cardapio":
                        bot.cardapio(data)
                        
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'Finalizar compra'}]
                            ],
                            'one_time_keyboard': True,
                            'resize_keyboard': True,
                        }
                        requests.get(URL['url'] + 'SendMessage',
                                        {'chat_id': data['message']['chat']['id'],
                                        'text': "",
                                        'reply_markup': json.dumps(reply_markup),
                                        'disable_web_page_preview': 'true'})
                        continuar_ham = False
                        
                    elif data['message']['text'] == "Finalizar compra":
                        requests.get(URL['url'] + "SendMessage", {'chat_id': data['message']['chat']['id'], 'text':"Por favor digite seu CEP (Apenas Numero) ou nos mande sua localização"})
                        mapa_frete.frete_get()
                    elif data['message']['text'] == "Voltar ao menu":
                        bot.cardapio(data)
                        continuar_ham = False
            pass                  
    return
