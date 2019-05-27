#Autor Juan Leonardo Ramírez Velasquez
#github.com/leorami99
import telebot
import RPi.GPIO as GPIO
import time
from gpiozero import LightSensor
ldr=LightSensor(21)#en este pin se van a leer las señales de la LDR
GPIO.setmode(GPIO.BCM)#Se establece el modo para trabajr la nomenclatura de los pines GPIO de la Raspberry pi
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
TOKEN = 'AQUI VA EL TOKEN DEL BOT DE TELEGRAM' #Ponemos el TOKEN generado con el @BotFather
mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN
print('Esperando mensaje:')
def listener(msg):  ##Cuando llega un mensaje se ejecuta esta funcion		
		for m in msg:
			print(ldr.value)
        		chat_id = m.chat.id
        		if m.content_type == 'text':
            			text = m.text
            			mi_bot.send_message(chat_id,"Se ejecuto el comando correctamente")
            			mi_bot.send_message(chat_id, text)
	    		if text == 'Sala' or text== 'sala':
					print('Sala Encendida')
					mi_bot.send_message(chat_id, 'Sala encendida')
					GPIO.output(5, 1)
	    		if text == 'A sala' or text== 'a sala':
					print('Sala apagada')
					mi_bot.send_message(chat_id, 'Sala apagada')
					GPIO.output(5, 0)
				if text == 'Cuarto' or text=='cuarto':
					GPIO.output(6, 1)
					print('Cuarto encendido')
					mi_bot.send_message(chat_id, 'Cuarto encendido')
				if text == 'A cuarto' or text=='a cuarto':
					y=False
					GPIO.output(6, 0)
					print('Cuarto apagado')
					mi_bot.send_message(chat_id, 'Cuarto apagado')
				if text == 'Wc' or text == 'wc':
					y=False
					print('Banio encendido')
					GPIO.output(13, 1)
					mi_bot.send_message(chat_id, 'Banio encendido')
				if text == 'A wc' or text == 'a wc':
					print('Banio apagado')
					GPIO.output(13 , 0)
					mi_bot.send_message(chat_id, 'Banio apagado')
				if text == 'Garaje' or text == 'garaje':
					y=False
					print('Garaje encendido')
					GPIO.output(19, 1)
					mi_bot.send_message(chat_id, 'Garaje encendido')
				if text == 'A garaje' or text=='a garaje':
					y=False
					print('Garaje apagado')
					GPIO.output(19, 0)
					mi_bot.send_message(chat_id, 'Garaje apagado')
				if text == 'Cocina' or text == 'cocina':
					y=False
					print('Cocina encendida')
					GPIO.output(26, 1)
					mi_bot.send_message(chat_id, 'Cocina encendida')
				if text == 'A cocina' or text=='a cocina':
					print('Cocina apagada')
					GPIO.output(26, 0)
					mi_bot.send_message(chat_id, 'Cocina apagada')
				if text == 'Apagar todo' or text == 'apagar todo':
					y=False
					GPIO.output(5, 0)
					GPIO.output(6, 0)
					GPIO.output(13, 0)
					GPIO.output(19, 0)
					GPIO.output(26 ,0)
					mi_bot.send_message(chat_id, 'Se ha apgado todo')
				if text == 'Encender todo' or text == 'encender todo':
					y=False
					GPIO.output(5, 1)
					GPIO.output(6, 1)
					GPIO.output(13, 1)
					GPIO.output(19, 1)
					GPIO.output(26, 1)
					mi_bot.send_message(chat_id, 'Se ha encendido todo')
				if text == 'alarma' or text=='Alarma':
					while True:
						if ldr.value <= 0.3:#Cuando el valor de la LDR sea menor o igual 0.3 envia señal a el pin donde va estar conectado un buzzer y se enviara un mensaje a telegram
							print('intruso')
							mi_bot.send_message(chat_id, 'Se a detectado un intruso')
							for i in range(1, 100):
								GPIO.output(20, 1)
								time.sleep(0.1)
								GPIO.output(20, 0)
								time.sleep(0.1)	
mi_bot.set_update_listener(listener) #registrar la funcion listener
mi_bot.polling()

while True: #No terminamos nuestro programa
    GPIO.cleanup()# cuando se termine el programa se va ejecutar esta función lo cual permite poner en un estado de desconexion los pines GPIO de la raspberry pi
    pass
