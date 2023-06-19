import requests
import json
from chave import URL, URL_File
from Lista_de_lanche import opcoes
import __main__ 

def __init__(self, x, y):
        self._x = x
        self._y = y
        print('Inside DB init')

class bot():
    

    @staticmethod
    def delete_updates(data,x):
        requests.get(URL['url'] + 'getUpdates', params={'offset': data['update_id'] + x})

    @staticmethod
    def get_message(data, command, msg):
        if data['message']['text'] == command:
            requests.post(URL['url'] + 'SendMessage', data={'chat_id': data['message']['chat']['id'], 'text': str(msg)})

    @staticmethod
    def get_file(data, file):
        aqv = {'png': {'metodo': 'sendPhoto', 'send': 'photo'},
                'jpg': {'metodo': 'sendPhoto', 'send': 'photo'}}
        file_format = 'jpg' if '.jpg' in file else 'png' if '.png' in file else None
        if file_format:
            return requests.get(URL['url'] + aqv[file_format]['metodo'], params={'chat_id': data['message']['chat']['id']},
                                files={aqv[file_format]['send']: open(file, 'rb')}).text
        else:
            return "Formato de arquivo inválido."



    @staticmethod
    def send_markup(data, command, keyboard, msg):
        reply_markup = keyboard
        if data['message']['text'] == command:
            requests.post(URL['url'] + 'sendMessage', data={'text': msg,
                                                             'chat_id': data['message']['chat']['id'],
                                                             'reply_markup': json.dumps(reply_markup),
                                                             'disable_web_page_preview': 'true'})

    @staticmethod
    def calculo_item(itens):
        preco_total = sum(item['preco'] for item in itens)
        return preco_total

    @staticmethod
    def calculo_preco(pedido,preco_frete):
        p_hamburguer = 20
        p_big = 10
        p_pizza = 25
        p_Piz2 = 42
        p_refri = 2
        p_refri2 = 5
        frete = preco_frete
        valor_total = 0

        for item in pedido:
            if item == "Mac":
                valor_total += p_hamburguer
            if item == "Big":
                valor_total += p_big
            if item == "Piz":
                valor_total += p_pizza
            if item == "Piz2":
                valor_total += p_Piz2
            if item == "tip1":
                valor_total += p_refri
            if item == "tip2":
                valor_total += p_refri2
            if item == "frete":
                valor_total += frete

        return valor_total,frete

    @staticmethod
    def send_cardapio(data):
        reply_markup = {
        'keyboard': [[{'text':'Cardapio'}],
                    [{'text':'Falar com atendente'}],
        ],           
        'one_time_keyboard': True,
        'resize_keyboard': True,
    }


        requests.get(URL['url'] + 'SendMessage',
                        {'chat_id': data['message']['chat']['id'],
                        'text': "seja bem vindo! é um projeto em andamento", 
                        'reply_markup': json.dumps(reply_markup),
                        'disable_web_page_preview': 'true'})

    @staticmethod
    def cardapio(data):
        Car = "Cardapio: \n"
        for item in opcoes:
            Car += f"{item['nome']} R$ {item['valor']:.2f}\n"
        reply_markup = {
        'keyboard': [[],
                     ['voltar']],
        'one_time_keyboard': True,
        'resize_keyboard': True,
    }
        for item in opcoes:
            reply_markup['keyboard'].append([{'text': item['nome']}])

        requests.get(URL['url'] + 'SendMessage',
                        {'chat_id': data['message']['chat']['id'],
                        'text': Car, 
                        'reply_markup': json.dumps(reply_markup),
                        'disable_web_page_preview': 'true'})