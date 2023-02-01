import json 
import requests
from threading import Thread

global URL
Token_my = ''
URL = {'url':'https://api.telegram.org/bot{}'.format(Token_my)}
URL_File = {'url':'https://api.telegram.org/file/bot{}'.format(Token_my)}


class bot():
    
    def delete_updates(data):
        requests.get(URL['url'] + 'getUpdates', {'offset': data['update_id'] + 1})
    
    def get_message(data,command, msg):
        if data['message']['text'] == command:
            requests.get(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'], 'text' : str(msg)})
    
    def get_file(data, file,command):
        if data['message']['text'] == command:
            aqv = { 'png': {'metodo': 'sendPhoto', 'send': 'photo'},
                    'jpg': {'metodo': 'sendPhoto', 'send': 'photo'}}
            return requests.get(URL['url'] + aqv['jpg' if '.jpg' in file else 'png']['metodo'], {'chat_id': data['message']['chat']['id']}, files={aqv['jpg' if '.jpg' in file else 'png']['send']: open(file, 'rb')}).text
    
    def send_markup(data,command,keyboard,msg):
        reply_markup = keyboard
        if data['message']['text'] == command:
            requests.post(URL['url'] + 'sendMessage', {  'text': msg, 
                                                                    'chat_id': data['message']['chat']['id'], 
                                                                    'reply_markup': json.dumps(reply_markup), 
                                                                    'disable_web_page_preview': 'true'})
 
while True:
    x=''
    while 'result' not in x:
        try:
            x = json.loads(requests.get(URL['url'] + 'getUpdates').text)
        except Exception as e:
            x=''
            if 'Failed to establish a new connection' in str(e):
                print('Perca de conexão')
            else:
                print('Erro desconhecido: ' + str(e))
                        
    if len(x['result']) >0:
        for data in x['result']:
            bot.delete_updates(data)
                
            print(json.dumps(data, indent=1)) 
            
            bot.get_message(data, '/oi', 'oi')
            bot.get_message(data, '/ola', 'oie')
            bot.get_message(data, 'x', 'x')
            bot.get_file(data,'local da imagem', 'foto')
            bot.send_markup(data,'c',{'keyboard': [
                                    [{'text': '1'}], 
                                    [{'text': '2'}],
                                    [{'text': '3'}],
                                    [{'text': '4'}],
                                    [{'text': '5'}],]}, 'test')
            """
            para ultilizar eco bot, abaixo está o comando atual. 
            bot.get_message(data,data['message']['text'],data['message']['text'])
            
            """
            
        """
            A base é simple praticamente são IFs, get_message(data, 'comando', 'message')
        o código está em desenvolmento ainda, a meta é criar dois bots, um para fazer uma loja no telegram, 
        com calculo de frete, e pagamento pelo API do mercado Pago, e o segundo é intregar o chatGp nele.
            
            Caso tenha alguma duvida mande e-mail darioaraujo44@gmail.com, a cada semana posto atualização no Github.
        espero que gostem e que seja util. 
        
        """
