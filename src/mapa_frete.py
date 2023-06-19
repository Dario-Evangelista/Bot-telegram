import requests
import json
import math
import unicodedata
import csv
from funcoes import bot
from chave import URL
import Selecionar_Ham
from Lista_de_lanche import opcoes, pedido

cep=""
cep_loja = "endereço da loja"
numero_loja = ""
numero_cliente = ""
key = "chave do mapquestapi"
valor = 2
dados = []

def localizacao(cep):
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Por favor, insira um CEP válido com 8 dígitos.")
        return None

    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("CEP inválido. Por favor, insira um CEP válido.")
        return None

    if response.status_code == 400:
        print("CEP inválido. Por favor, insira um CEP válido.")
        return None

    if "erro" in data:
        print("CEP não encontrado na base de dados.")
        return None

    logradouro_cliente = data['logradouro']
    bairro_cliente = data['bairro']
    localidade_cliente = data['localidade']

    logradouro = unicodedata.normalize('NFKD', logradouro_cliente).encode('ASCII', 'ignore').decode('utf-8')
    bairro = unicodedata.normalize('NFKD', bairro_cliente).encode('ASCII', 'ignore').decode('utf-8')
    localidade = unicodedata.normalize('NFKD', localidade_cliente).encode('ASCII', 'ignore').decode('utf-8')

    if cep == cep_loja:
        return logradouro, numero_loja, bairro, localidade
    else:
        return logradouro, numero_cliente, bairro, localidade

def cordenada(data):
    locations = data['results'][0]['locations']
    latitude = locations[0]['latLng']['lat']
    longitude = locations[0]['latLng']['lng']
    return latitude, longitude

def encontrar_endereço_lat_lon(lat,lon):
    url = f'http://www.mapquestapi.com/geocoding/v1/reverse?key={key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['info']['statuscode'] == 0:
            
            ender = data['results'][0]['locations'][0]['street']
            cidade = data['results'][0]['locations'][0]['adminArea5']
            estado = data['results'][0]['locations'][0]['adminArea3']
            pais = data['results'][0]['locations'][0]['adminArea1']
        
            ender = unicodedata.normalize('NFKD', ender).encode('ASCII', 'ignore').decode('utf-8')
            cidade = unicodedata.normalize('NFKD', cidade).encode('ASCII', 'ignore').decode('utf-8')
            estado = unicodedata.normalize('NFKD', estado).encode('ASCII', 'ignore').decode('utf-8')
            pais = unicodedata.normalize('NFKD', pais).encode('ASCII', 'ignore').decode('utf-8')
            
            logradouro = ender, cidade, estado, pais
            
            print('Endereço encontrado:')
            print(f'{ender}, {cidade}, {estado}, {pais}')
            
            return logradouro
        else:
            print('Não foi possível encontrar o endereço.')
    else:
        print('Erro na requisição:', response.status_code)

def dados_local():
    with open("mapa/dados_endereco.csv", "w", newline="") as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(dados)
    return True

def carregar_dados_local():
    dados = []
    with open("mapa/dados_endereco.csv", "r") as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            dados.extend(linha)

    resultado = ", ".join(map(str, dados))
    return resultado

def calcular_distancia2(data,logradouro,lat1, lon1, lat2, lon2,pedido):
    raio_terra = 6371.0

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = int(raio_terra * c)
    valor = 2
    preco = distancia * valor
      

    endereco_completo = "\n".join(logradouro) 
    frete = f"Seu endereço é:\n {endereco_completo}\n Frete é R${preco},00"
    
    requests.get(URL['url'] + "SendMessage", {'chat_id': data['message']['chat']['id'], 'text': frete})
    reply_markup = {
                                                    'keyboard': [
                                                        [{'text': 'Sim'}],
                                                        [{'text': 'Não'}],
                                                        [{'text': 'Voltar'}],
                                                    ],
                                                    'one_time_keyboard': True,
                                                    'resize_keyboard': True,
                                                }

    requests.get(URL['url'] + 'SendMessage',
            {'chat_id': data['message']['chat']['id'],
            'text': 'o endereço está corrteto?',
            'reply_markup': json.dumps(reply_markup),
            'disable_web_page_preview': 'true'})
    
    

    valor_total, frete = bot.calculo_preco(pedido, preco)  # Calcular o valor total e obter o valor do frete
    opcoes.append({'nome': "frete", 'valor': preco})
    pedido.append('frete')
    
    return distancia, frete, valor_total


def frete_get():
    frete_true = True
    while frete_true:
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
                
                message = data['message']
                                                       
                if 'text' in message:
                    text= message['text']

                    cep = text
                    
                    if text.lower() == "não":
                        requests.post(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'],
                                                                    'text': "Digite seu CEP:"})
                        frete_true = False
                        frete_get()
                        continue
                    
            
                    elif text.lower() == "voltar":
                        frete_true = False
                        bot.send_cardapio(data)
                        continue
                    
                    elif text.lower() == "sim":
  
                        op1 = "Seu carrinho é:\n\n"
                        for item in pedido:
                            for opcao in opcoes:
                                if opcao['nome'] == item:
                                    valor_item = opcao['valor']
                                    op1 += f"{item} R$ {valor_item:.2f}\n"
                                    break
                        op1 += "\nO valor total é R$ {:.2f}. Qual seria sua forma de pagamento?".format(valor_total)
                        requests.post(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'], 'text': op1})

                        continue                        

                    elif len(cep) != 8 or not cep.isdigit():
                        requests.post(URL['url'] + 'SendMessage', {'chat_id': data['message']['chat']['id'], 'text': "Cep Inválido"})
                    
                    else:
                        
                        logradouro_loja = localizacao(cep_loja)
                        logradouro = localizacao(cep)

                        url_loja = "https://www.mapquestapi.com/geocoding/v1/address?key={}&location={}".format(key, logradouro_loja)
                        url = "https://www.mapquestapi.com/geocoding/v1/address?key={}&location={}".format(key, logradouro)

                        if logradouro_loja is not None:
                            dados.append(logradouro_loja)
                            data_loja = json.loads(requests.get(url_loja).text)
                            data_cliente = json.loads(requests.get(url).text)
                            print("\n Seus dados foram salvos com sucesso!")
                        else:
                            print("Não foi possível salvar os dados.")
                
                        dados_local()
                        carregar_dados_local()

                        lat1, lon1 = cordenada(data_loja)
                        lat2, lon2 = cordenada(data_cliente)

                        distancia_km, preco, valor_total = calcular_distancia2(data, logradouro, lat1, lon1, lat2, lon2,pedido)
                        print(f"A distância é {distancia_km}KM")
                        print(f"Frete é R${preco},00")
                        
                elif 'location' in data['message']:
                    location = data['message']['location']
                    latitude = location['latitude']
                    longitude = location['longitude']
                    
                    logradouro_loja = localizacao(cep_loja)
                    url_loja = "https://www.mapquestapi.com/geocoding/v1/address?key={}&location={}".format(key, logradouro_loja)
                
                    if logradouro_loja is not None:
                        dados.append(logradouro_loja)
                        data_loja = json.loads(requests.get(url_loja).text)
                        print("\n Seus dados foram salvos com sucesso!")
                    else:
                        print("Não foi possível salvar os dados.")
                    
                    logradouro_loja = localizacao(cep_loja)
                    logradouro = encontrar_endereço_lat_lon(latitude, longitude)
 
                    lat2 = latitude
                    lon2 = longitude
                    
                    lat1, lon1 = cordenada(data_loja)

                    distancia_km, preco, valor_total = calcular_distancia2(data, logradouro, lat1, lon1, lat2, lon2,pedido)
                    print(f"A distância é {distancia_km}KM")
                    print(f"Frete é R${preco},00")
                
                
                    
                    
                
