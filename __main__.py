import json
import requests
from src.chave import URL, URL_File, Bot
from src.Selecionar_Ham import selecionar_Hamburguer
from src import mapa_frete
from src.funcoes import bot


while True:
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
                
                message = data['message']
                                    
                if 'text' in message:
                    text= message['text']

                    if text:
                        bot.send_cardapio(data)

                        continuar = True
                        while continuar:
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
                                        
                                        message = data['message']
                                        
                                        if 'text' in message:
                                            text= message['text']
                                            
                                            if text == "Cardapio":
                                                bot.cardapio(data)

                                            elif text == "Mac":
                                                bot.get_file(data, 'img/hamburguer.jpg')
                                                reply_markup = {
                                                    'keyboard': [
                                                        [{'text': 'Mais detalhe do Mac'}],
                                                        [{'text': 'Cardapio'}],
                                                        [{'text': 'Adicionar Mac'}],
                                                    ],
                                                    'one_time_keyboard': True,
                                                    'resize_keyboard': True,
                                                }

                                                requests.get(URL['url'] + 'SendMessage',
                                                            {'chat_id': data['message']['chat']['id'],
                                                            'text': 'Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.',
                                                            'reply_markup': json.dumps(reply_markup),
                                                            'disable_web_page_preview': 'true'})
                                                
                                                selecionar_Hamburguer()
                                            elif text == 'Big':
                                                bot.get_file(data, 'img/hamburguer.jpg')
                                                reply_markup = {
                                                    'keyboard': [
                                                        [{'text': 'Mais detalhe do Big'}],
                                                        [{'text': 'Cardapio'}],
                                                        [{'text': 'Adicionar Big'}],
                                                    ],
                                                    'one_time_keyboard': True,
                                                    'resize_keyboard': True,
                                                }

                                                requests.get(URL['url'] + 'SendMessage',
                                                            {'chat_id': data['message']['chat']['id'],
                                                            'text': 'Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.',
                                                            'reply_markup': json.dumps(reply_markup),
                                                            'disable_web_page_preview': 'true'})
                                                
                                                selecionar_Hamburguer()

                                            elif text == 'Piz':
                                                bot.get_file(data, 'img/hamburguer.jpg')
                                                reply_markup = {
                                                    'keyboard': [
                                                        [{'text': 'Mais detalhe do Piz'}],
                                                        [{'text': 'Cardapio'}],
                                                        [{'text': 'Adicionar Piz'}],
                                                    ],
                                                    'one_time_keyboard': True,
                                                    'resize_keyboard': True,
                                                }

                                                requests.get(URL['url'] + 'SendMessage',
                                                            {'chat_id': data['message']['chat']['id'],
                                                            'text': 'Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.',
                                                            'reply_markup': json.dumps(reply_markup),
                                                            'disable_web_page_preview': 'true'})
                                                selecionar_Hamburguer()

                                            elif text == 'Piz2':
                                                bot.get_file(data, 'img/hamburguer.jpg')
                                                reply_markup = {
                                                    'keyboard': [
                                                        [{'text': 'Mais detalhe do Piz2'}],
                                                        [{'text': 'Cardapio'}],
                                                        [{'text': 'Adicionar Piz2'}],
                                                    ],
                                                    'one_time_keyboard': True,
                                                    'resize_keyboard': True,
                                                }

                                                requests.get(URL['url'] + 'SendMessage',
                                                            {'chat_id': data['message']['chat']['id'],
                                                            'text': 'Um suculento hambúrguer com ingredientes frescos e saborosos, uma explosão de sabores em cada mordida.',
                                                            'reply_markup': json.dumps(reply_markup),
                                                            'disable_web_page_preview': 'true'})
                                                selecionar_Hamburguer()

                                            elif text == 'tip1':
                                                bot.get_file(data, 'img/refri.png')
                                                reply_markup = {
                                                    'keyboard': [
                                                        [{'text': 'Mais detalhe do Piz2'}],
                                                        [{'text': 'Cardapio'}],
                                                        [{'text': 'Adicionar Piz2'}],
                                                    ],
                                                    'one_time_keyboard': True,
                                                    'resize_keyboard': True,
                                                }

                                                requests.get(URL['url'] + 'SendMessage',
                                                            {'chat_id': data['message']['chat']['id'],
                                                            'text': 'Bebida de laranja: Uma deliciosa bebida refrescante com sabor cítrico e suculento de laranja, perfeita para saciar sua sede e despertar seus sentidos.',
                                                            'reply_markup': json.dumps(reply_markup),
                                                            'disable_web_page_preview': 'true'})
                                                selecionar_Hamburguer()

                                            elif text == 'tip2':
                                                bot.get_file(data, 'img/refri.png')
                                                reply_markup = {
                                                    'keyboard': [
                                                        [{'text': 'Mais detalhe do tip2'}],
                                                        [{'text': 'Cardapio'}],
                                                        [{'text': 'Adicionar tip2'}],
                                                    ],
                                                    'one_time_keyboard': True,
                                                    'resize_keyboard': True,
                                                }

                                                requests.get(URL['url'] + 'SendMessage',
                                                            {'chat_id': data['message']['chat']['id'],
                                                            'text': 'Coca-Cola: Um clássico irresistível, a Coca-Cola é uma bebida gaseificada que combina o sabor único de uma mistura secreta de ingredientes, resultando em uma experiência de sabor refrescante e incomparável.',
                                                            'reply_markup': json.dumps(reply_markup),
                                                            'disable_web_page_preview': 'true'})
                                                selecionar_Hamburguer()

                                            elif text == 'Finalizar compra':                                 
                                                mapa_frete.frete_get()
                                                
                                            elif text.lower() == "voltar":
                                                frete_true = False
                                                bot.send_cardapio(data)
                                                continue
                                            
                                        elif 'location' in data['message']:
                                            location = data['message']['location']
                                            latitude = location['latitude']
                                            longitude = location['longitude']
                                            
                                            print(latitude, longitude)