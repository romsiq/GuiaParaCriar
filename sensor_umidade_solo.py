###  Sensor de Umidade do Solo

# Bibliotecas necessárias
import RPi.GPIO as GPIO
import time
import csv
from datetime import datetime

# Leitura do sensor no canal 4 - pinout 4 do raspberry
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Apenas um título do tema do projeto
print("*** Verificando se o Solo está úmido ou não");

#Definição das variaveis para coleta de dados
variaveis = ['data_coleta', 'resultado_coleta']

#Função para coletar os dados, apresentar e salvar em csv.
def processamento_coleta(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(variaveis)

    while (1):

        if GPIO.input(channel):
            print("Sensor de solo seco")
            resultado_coleta = "solo seco"
        else:
            print("Sensor de solo úmido")
            resultado_coleta = "solo umido"

        # Objeto datetime coleta data e hora atual
        data_coleta = datetime.now()
        coleta = data_coleta.strftime("%d/%m/%Y %H:%M:%S")

        #Gravando resultado no arquivo csv
        csv_writer.writerow([coleta, resultado_coleta])
        csvfile.flush()

        #Proxima coleta em 5 segundos para este experimento, pode-se configurar coletas de 15 minutos por exemplo (15*60)
        time.sleep(5)

    # Configuração do GPIO para detecção da Umidade
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
    GPIO.add_event_callback(channel, processamento_coleta)


with open('coleta_umidade_solo.csv', 'w') as csvfile:
    processamento_coleta(csvfile)
