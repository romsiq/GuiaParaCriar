# Importar bibliotecas -  Adafruit DHT
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import csv
from datetime import datetime




# Leitura do DHT11 na porta pinout 4 do raspberry e variáveis de Umidade e Temperatura

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 4

# Informacoes iniciais - Características
print("*** Realizando coleta de dados sobre a Temperatura Ambiente e Umidade Relativa do Ar");
print("*** Faixa de leitura – Umidade: 20 à 80%");
print("*** Precisão umidade: 5%");
print("*** Faixa de leitura – Temperatura: 0 – 50 ºC");
print("*** Precisão temperatura: +/- 2 ºC");

#Definição das variaveis para coleta de dados
variaveis = ['coleta', 'umid', 'temp']

#Função para coletar os dados, apresentar e salvar em csv.
def processamento_coleta(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(variaveis)

    while (1):
        # Efetua a leitura do sensor
        umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);

        # Objeto datetime contando data e hora atual
        data_hora = datetime.now()
        coleta = data_hora.strftime("%d/%m/%Y %H:%M:%S")

        # Caso leitura esteja ok, mostra os valores na tela
        if umid is not None and temp is not None:
            print("Coleta", coleta);
            print("Temperatura", temp);
            print("Umidade", umid)
            print("Próxima coleta em 5 segundos");
            #gravando resultado no arquivo csv
            csv_writer.writerow([coleta, umid, temp])
            csvfile.flush()
            #proxima coleta em 5 segundos
            time.sleep(5)

    else:
        # Mensagem de erro de comunicacao com o sensor
        print("Falha ao ler dados do sensor!")

with open('coleta_temp_umidade_ameno.csv', 'w') as csvfile:
    processamento_coleta(csvfile)



'''
A Agência de Vigilância Sanitária, a Anvisa, diz que a temperatura ideal em ambientes fechados é algo entre 23°C e 26°C.

No inverno, é comum a umidade relativa do ar nas grandes cidades cair até abaixo dos 30%. 
Algo preocupante, quando se sabe que o ideal, de acordo com a Organização Mundial de Saúde (OMS), 
é que ela varie entre 50% e 80%. 

'''