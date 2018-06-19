# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
import os
import json
import requests
from telebot import types # Tipos para la API del bot.
from datetime import datetime, date, time, timedelta
import calendar
from threading import Thread
from random import randrange
import time # Librería para hacer que el programa que controla el bot no se acabe.
import os.path
from pathlib import Path

import os
import subprocess



import time
import schedule




idUserJuego = 0
idUserJuegoResp = 0
msg = ""
juegoUsersListId = list()
juegoUsersListNick = list()
juegoUserNumber = 0

msgDuelo= ""
parada = ""

idBan = 239822769
estaBan = False
pole = False
hora = "00:00"
#datetime.datetime.strptime(hora, '%H:%M').time()
#horaBn= datetime.datetime(2017,11,8,)
#print(horaBn)
#if horaBn.date() == datetime.today().date().second :
    #print('horaBnsas')

TOKEN = '[Telegram bot TOKEN]' # Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
'''
def job():
    #bot.sendMessage(239822769,'poleadaaaaa') -1001090423519
    global pole

    pole=True
    if pole == True:
        bot.send_message(-1001090423519,'Pole')
        time.sleep(5)
        bot.send_message(-1001090423519,'La pole es mia cabrones jaajjajaaj')
        time.sleep(55)
        bot.send_message(-1001090423519,'Samu estara durmiendo que os jodan cabrones de la pole')
        time.sleep(60)
        bot.send_message(-1001090423519,'Dentro de 5 segundos os enviaré toda la mierda jajaja')
        time.sleep(1)
        bot.send_message(-1001090423519,'5')
        time.sleep(1)
        bot.send_message(-1001090423519,'4')
        time.sleep(1)
        bot.send_message(-1001090423519,'3')
        time.sleep(1)
        bot.send_message(-1001090423519,'2')
        time.sleep(1)
        bot.send_message(-1001090423519,'1')
        time.sleep(1)
        bot.send_message(-1001090423519,'0')
        time.sleep(0)
        print ('prueba')

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at(hora).do(job)

while pole==False:
    schedule.run_pending()
    time.sleep(1)




'''

'''
def sendSimpleText(chat_id):
    bot.sendMessage(chat_id,'pole')


def main():
    MessageLoop(bot, handle).run_as_thread()
    job = sched.add_job(sendSimpleText, run_date=exec_date, args=['239822769'])

    while True:
        time.sleep(1)
        sys.stdout.write('.'); sys.stdout.flush()

'''


#Listener

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
        for m in messages: # Por cada dato 'm' en el dato 'messages'
            if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
                cid = m.chat.id # Almacenaremos el ID de la conversación.
                print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

#####################################################################33 variables









#############################################

text_messages = {
    'holat':
        u'Hola a todos? menudo subnormal nadie te quiere :V \n',
    'manco':
        u'yo no hablo con bronces si quieres habla con mis torres tendras una conversación muy interesante gilipollas :V \n',
    'comemela':
        u'comemela entera puto subnormal.\n',
    'estudiado':
        u'yo no necesito estudiar soy un genio choff choff ijjijijij\n',
    'juanma':
        u'Juanma = Rager del asco \n',
    'slene':
        u'Callate la puta boca gilipollas se dice Sleene joder!!!!! \n',
    'salsa':
        u'I salsa your face \n',
    'promo':
        u'Tranquilo no pasa nada tu deja de fedear y de jugar rankeds así la gente podrá subir elo sin que otros les jodan ;) \n',
    'gracias':
        u'De nada puedo ayudar en lo que se pueda ;) \n',
    'adios':
        u'Chau pescau \n',
    'puto':
        u'Me importa una mierda lo que digas sigues siendo un bronze de mierda (?? ³?)? \n',
    'putoBot':
        u'No se si te refieres a mi pero: --> Te jodes jajaja ??? \n',
    'chocala':
        u'(????)??(????)   Toma esa!!\n',
    'llora':
        u'Llora inutil de mierda nadie te quiere \n',
    'buenosDias':
        u'Buenos serán para ti tengo las putas torretas congeladas joder!!! \n',
    'remusen':
        u'Se dice resumen joderrrrrrr!!!!!! o(-?-)o     \n',

}




#randommmmmmmmmmmmmmmmmmmmmmm




#Funciones

# Handle '/start' and '/help'

@bot.message_handler(commands=['start'])


def send_welcome(m):
    cid = m.chat.id
    x=m.text
    parametro = x[6:].strip()
    if parametro == 'normas':
        rules = ""
        with open('normas/normas.txt', 'r') as rules:
            rules = rules.read()
        bot.send_message(cid, rules )

    else:

        bot.reply_to(m, """\
        Hola soy un bot para entretener a la peña a demás de reirme de la gente aporto estos comandos:  /tempo , /juego , /sera , /ts , /discord
    \
    """)

@bot.message_handler(commands=['donacion'])
def command_donacion(m):
    cid = m.chat.id
    idUser = m.from_user.id
    if (m.from_user.username is None):
        nun = m.from_user.first_name
        if (m.from_user.last_name is not None):
            nun += " "
            nun += m.last_name
    else:
        nun = m.from_user.username
    bot.send_message( cid, 'Si te apetece hacer una pequeña aportación para el desarrollador de este bot pincha aqui : paypal.me/segoitz \nMuchas gracias por tu ayuda amijo.')
    bot.send_message(239822769,'@' + nun + ' ' + str(idUser) + ' a pulsado /donacion ' )
@bot.message_handler(commands=['slene']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_slene(m): # Definimos una función que resuleva lo que necesitemos.

        cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
        bot.send_message( cid, 'selenee a no seeleene')
'''
@bot.message_handler(commands=['stickers']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_stickers(m): # Definimos una función que resuleva lo que necesitemos.
        cid =m.chat.id

        #/home/heimbiBot/stickers convert ai.jpg -size 512x512 ai.png
        path = '/home/heimiBot/stickers'
        lstFiles = []
        lstDir = os.walk(path)

        list = os.listdir(path) # dir is your directory path
        number_files = len(list)
        bot.send_message(cid,'El numero de archivos del fichero es : ' +str(number_files))

        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ".jpg") or (extension == ".png"):
                    #p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
                    #bot.send_message(cid, p.communicate())
                    #lstFiles.append(nombreFichero+extension)
                    firstpart = "/home/heimiBot/stickers/"+nombreFichero+extension
                    secondpart = "/home/heimiBot/stickers/"+nombreFichero+'_sticker.png'
                    bot.send_message(cid, "convirtiendo : " + firstpart + " a: " + secondpart)
                    a = subprocess.Popen(["convert", firstpart, "-size", "512x512", secondpart],stdout=subprocess.PIPE)
                    a.communicate()[0].decode('utf-8')
                #bot.send_message( cid,nombreFichero+extension)
'''

@bot.message_handler(commands=['stickersBien']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_stickersBien(m): # Definimos una función que resuleva lo que necesitemos.
        cid =m.chat.id

        #/home/heimbiBot/stickers convert ai.jpg -size 512x512 ai.png
        path = '/home/heimiBot/stickers'
        lstFiles = []
        lstDir = os.walk(path)

        list = os.listdir(path) # dir is your directory path
        number_files = len(list)
        bot.send_message(cid,'El numero de archivos del fichero es : ' +str(number_files))

        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ".jpg") or (extension == ".png"):
                    #p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
                    #bot.send_message(cid, p.communicate())
                    #lstFiles.append(nombreFichero+extension)
                    firstpart = "/home/heimiBot/stickers/"+nombreFichero+extension
                    secondpart = "/home/heimiBot/stickers/"+nombreFichero+'-sticker.png'
                    bot.send_message(cid, "convirtiendo : " + firstpart + " a: " + secondpart)
                    a = subprocess.Popen(["ffmpeg","-i", firstpart, "-vf", "scale=512:512", secondpart],stdout=subprocess.PIPE)
                    a.communicate()[0].decode('utf-8')
                #bot.send_message( cid,nombreFichero+extension)

@bot.message_handler(commands=['audios']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_audios(m): # Definimos una función que resuleva lo que necesitemos.
        cid =m.chat.id
        bot.send_message(cid,'hola audios')
        #ffmpeg -i vuelve.mp3 -ac 1 -c:a opus -b:a 16k vuelve.ogg
        path = '/home/heimiBot/audios'
        lstFiles = []
        lstDir = os.walk(path)

        list = os.listdir(path)
        number_files = len(list)
        bot.send_message(cid,'El numero de archivos del fichero es : ' +str(number_files))

        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ".mp3"):
                    #p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
                    #bot.send_message(cid, p.communicate())
                    #lstFiles.append(nombreFichero+extension)
                    firstpart = "/home/heimiBot/audios/"+nombreFichero+extension
                    secondpart = "/home/heimiBot/audios/"+nombreFichero+'_audio.ogg'
                    bot.send_message(cid, "convirtiendo : " + firstpart + " a: " + secondpart)
                    a = subprocess.Popen(["ffmpeg","-i", firstpart, "-ac","1","-c:a","opus","-b:a","16k", secondpart],stdout=subprocess.PIPE)
                    a.communicate()[0].decode('utf-8')
                #bot.send_message( cid,nombreFichero+extension)
'''
@bot.message_handler(commands=['gifs']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_gifs(m): # Definimos una función que resuleva lo que necesitemos.
        cid =m.chat.id
        bot.send_message(cid,'hola gifs')
        #ffmpeg -i vuelve.mp3 -ac 1 -c:a opus -b:a 16k vuelve.ogg
        path = '/home/heimiBot/gifs/'
        lstFiles = []
        lstDir = os.walk(path)

        list = os.listdir(path)
        number_files = len(list)
        bot.send_message(cid,'El numero de archivos del fichero es : ' +str(number_files))

        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ".flv")or(extension == ".mp4"):
                    #p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
                    #bot.send_message(cid, p.communicate())
                    #lstFiles.append(nombreFichero+extension)
                    firstpart = path+nombreFichero+extension
                    secondpart = path+'frames/ffout%03.png'
                    thirdpart = path+nombreFichero+'_output.gif'
                    bot.send_message(cid, "convirtiendo : " + firstpart + " a: " + secondpart)
                    a = subprocess.Popen(["ffmpeg","-y","-ss","30","-t","3","-i", firstpart, " \ ","-vf","fps=10,scale=320:-1:flags=lanczos,palettegen", secondpart],stdout=subprocess.PIPE)
                    a.communicate()[0].decode('utf-8')
                    b = subprocess.Popen(["ffmpeg","-ss","30","-t","3","-i", firstpart,"-i", secondpart,  "-filter_complex", " \ ","fps=10,scale=320:-1:flags=lanczos[x];[x][1:v]paletteuse", secondpart],stdout=subprocess.PIPE)
                    b.communicate()[0].decode('utf-8')
                    #c = subprocess.Popen(["ffmpeg","-v","warning","-ss","45","-t","2","-i", firstpart, "-gifflags","-trandsdiff","-y","bbb-" + secondpart],stdout=subprocess.PIPE)
                    #c.communicate()[0].decode('utf-8')

                    d= subprocess.Popen(["mkdir","frames"],stdout=subprocess.PIPE)
                    d.communicate()[0].decode('utf-8')
                    e= subprocess.Popen(["ffmpeg","-i",firstpart,"-vf","scale=320:-1:flags=lanczos,fps=10",secondpart],stdout=subprocess.PIPE)
                    e.communicate()[0].decode('utf-8')
                    f= subprocess.Popen(["convert","-loop","0","frames/ffout*.png", secondpart],stdout=subprocess.PIPE)
                    f.communicate()[0].decode('utf-8')

                #bot.send_message( cid,nombreFichero+extension)
'''



@bot.message_handler(commands=['ts']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_ts(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        bot.send_message( cid, 'La ip: segoitz.tk\nLa pass: haberestudiao123')

@bot.message_handler(commands=['discord']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_discord(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        bot.send_message( cid, 'El discord del grupo es: https://discord.gg/tZTkxnS')

@bot.message_handler(commands=['salseo']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_pregonado(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        id = m.from_user.id
        x=m.text
        rules = ' '.join(x.split(" ")[1:])
        with open('normas/salsa.txt','w') as fo:
            fo.write(rules)

@bot.message_handler(commands=['salsa']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_rules(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        cid = m.chat.id
        rules = ""
        with open('normas/salsa.txt', 'r') as rules:
            rules = rules.read()
        bot.send_message(cid, rules )

@bot.message_handler(commands=['meternorma']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_pregonado(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    id = m.from_user.id
    if id == 239822769:
        x=m.text
        rules = ' '.join(x.split(" ")[1:])
        with open('normas/normas.txt','w') as fo:
            fo.write(rules)
    bot.send_message(cid, 'Normas guardadas correctamente' )

@bot.message_handler(commands=['normas']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_rules(m): # Definimos una función que resuleva lo que necesitemos.
    global normasActivadas
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        idUser = m.from_user.id
        destino = idUser
        cid = m.chat.id

        if m.chat.type != "private" and cid == -1001090423519 or cid == -1001084826863:

            click_kb = types.InlineKeyboardMarkup()
            click_button1 = types.InlineKeyboardButton('Normas', url = 't.me/heimibot?start=normas' )
            click_kb.row(click_button1)
            bot.send_message(cid, 'Tienes la normas por privado juapo', reply_markup=click_kb, disable_web_page_preview=True)




@bot.message_handler(commands=['malzi']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_malzi(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        bot.send_message( cid, 'No me hables de ese le pone ebola a mis torres y las derrite puto malz de la polla comeme el rabo si me escuchas destruire el vacio entero para matarte cabrón :v') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.bot
        bot.send_photo( cid, open( 'malz.jpg', 'rb'))

@bot.message_handler(commands=['chistaco']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_chistaco(m): # Definimos una función que resuleva lo que necesitemos.

    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        cid = m.chat.id
        numLinea=0
        chiste = ""
        chistoso = ""
        numChiste=0

        numLista=0

        infile = open('chistes/chistes.txt', 'r')
        for fich in infile:
            numLinea = numLinea +1
        infile.close()



        rnd = randrange(0, int(numLinea))

        infile = open('chistes/chistes.txt', 'r')
        for line in infile:
            numLinea = numLinea +1
            numchisteS = line.split(' ')[0]

            if numchisteS.isnumeric():
                numChiste = int(numchisteS)
            if rnd == numChiste :
                chiste = line.split(' * ')[1]
                chistoso = line.split(' ')[1]



        infile.close()

        bot.send_message(cid, 'Atentos todos al pedazo chiste que se ha marcado ' + chistoso + ': \n' + chiste )

@bot.message_handler(commands=['duelo'])
def duelo(m):

    global msgDuelo
    global parada

    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id

    #if idUser == 239822769 or idUser == 22605669 or idUser == 181575406 or idUser == 137216452 or idUser == 365770260 :
    if parada == "" or parada != "stop":
        idLista = ''
        estaEnLaLista = None
        numLinea = 0
        disparo = False
        infile = open('users/baneados.txt', 'r')
        for line in infile:
            numLinea = numLinea +1
            idListaS = line.split(' ')[0]
            idLista = int(idListaS)
            if idUser == idLista:
                baneado = idLista
        infile.close()
        if id != baneado:
            cid = m.chat.id
            username = m.from_user.username
            idUserJuego = m.from_user.id


            bot.send_message(cid, 'Empieza el duelo preparen las pistolas........')
            time.sleep(1)
            bot.send_message(cid, 'Preparados')
            time.sleep(1)
            msg = bot.send_message(cid, 'Listos')

            rnd = randrange(0, int(10))
            time.sleep(rnd)
            msgDuelo = bot.send_message(cid, 'YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!!!!!!')

            bot.register_next_step_handler(msgDuelo, step_disparo)
    else:
        bot.send_message(cid,"el duelo esta parado")

def step_disparo(m):
    global parada
    global msgDuelo

    cid = m.chat.id
    username = m.from_user.username
    idUser = m.from_user.id
    if m.text != None  :
        disparo = m.text.lower()

        if disparo == "pium":
            bot.send_message(cid, '@' + username + ' es el mas rápido del oeste, cuidado con el wachines')
            bot.send_message(239822769,'@' + username + ' ' + str(idUser) )
            bot.register_next_step_handler(msgDuelo, step_cooldown)
        else:
            bot.register_next_step_handler(msgDuelo, step_disparo)
    else:
        bot.register_next_step_handler(msgDuelo, step_disparo)

def step_cooldown(m):
    global parada
    cid = m.chat.id
    bot.send_message(cid, 'entra en cd')
    parada = "stop"
    bot.send_message(cid,parada)
    time.sleep(5)
    bot.send_message(cid, 'el duelo esta habilitado wachines')
    parada = ""

@bot.message_handler(commands=['juego'])
def juego(m):

    global idUserJuego
    global msg

    global juegoUsersListId
    global juegoUsersListNick
    global juegoUserNumber

    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        cid = m.chat.id
        username = m.from_user.username
        idUserJuego = m.from_user.id

        juegoUsersListId.insert(juegoUserNumber,idUserJuego)


        msg = bot.send_message(cid, 'Elige piedra papel tijera ')
        bot.register_next_step_handler(msg, step_opcion)

def step_opcion(m):

    global idUserJuego
    global idUserJuegoResp
    global msg


    cid = m.chat.id
    username = m.from_user.username
    idUserJuegoResp = m.from_user.id
    opcion = m.text.lower()
    rnd = randrange(0, int(2))

    if idUserJuego == idUserJuegoResp :

        if opcion == 'tijera' or opcion == 'tijeras' or opcion == 'piedra' or opcion == 'papel' :

            if rnd == 0 :
                if opcion == 'tijera' or opcion == 'tijeras' :
                    bot.send_message(cid, 'Me ha salido piedra has perdido @'+ username + ' jajajajja')
                if opcion == 'piedra':
                   bot.send_message(cid, 'Me ha salido piedra empate @'+ username + ' chocala :D')
                if opcion == 'papel':
                    bot.send_message(cid, 'Me ha salido piedra he perdido. Tu ganas @'+ username + ' :C')

            if rnd == 1 :
                if opcion == 'piedra':
                    bot.send_message(cid, 'Me ha salido papel has perdido @'+ username + ' jajajajja')
                if opcion == 'papel':
                    bot.send_message(cid, 'Me ha salido papel empate @'+ username + ' chocala :D')
                if opcion == 'tijera' or opcion == 'tijeras' :
                    bot.send_message(cid, 'Me ha salido papel he perdido. Tu ganas @'+ username + ' :C')

            if rnd == 2 :
                if opcion == 'papel':
                    bot.send_message(cid, 'Me ha salido tijeras has perdido @'+ username + ' jajajajja')
                if opcion == 'tijera' or opcion == 'tijeras' :
                    bot.send_message(cid, 'Me ha salido tijeras empate @'+ username + ' chocala :D')
                if opcion == 'piedra':
                    bot.send_message(cid, 'Me ha salido tijeras he perdido. Tu ganas @'+ username + ' :C')
        else:
            bot.send_message(cid, 'No válido. Elige piedra papel tijera ')
            bot.register_next_step_handler(msg, step_opcion)

    else:
        bot.register_next_step_handler(msg, step_opcion)




#audios-----------------------------------------------------------------------------------





@bot.message_handler(commands=['esungenio']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_esungenio(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        bot.send_audio( cid, open( 'genio.ogg', 'rb'))


@bot.message_handler(commands=['brah']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_brah(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        bot.send_audio( cid, open( 'brah.ogg', 'rb'))

#audios looooooooooooooool -------------------------------------------------------------------

@bot.message_handler(commands=['brazo']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_brazo(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        bot.send_audio( cid, open( 'brazo.mp3', 'rb'))

@bot.message_handler(commands=['miembros']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_rules(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        if m.chat.type != "private":
            miembros = ""
            infile = open('users/miembros.txt', 'r')
            for line in infile:
                numero = line.split(' * ')[0]
                miembro = line.split(' * ')[2]
                nombre = line.split(' * ')[3]
                miembros = miembros + numero + ".- " + miembro + ' es --> ' +nombre+ '\n'
            infile.close()
            bot.send_message(cid, miembros )

@bot.message_handler(commands=['tempo']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def tempo(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        cid = m.chat.id
        x=m.text
        nombre = ' '.join(x.split(" ")[1:])
        if not x == '/tempo' and not nombre.isdigit():
            params = { "q" : nombre, "lang" : "es", "appid" : "[WEATHER TOKEN]"  }
            data = requests.get("http://api.openweathermap.org/data/2.5/weather", params)
            ciudad = data.json()['name']
            tiempo = data.json()['weather'][0]['description'].capitalize()
            nubosidad = data.json()['clouds']['all']
            viento = data.json()['wind']['speed']
            temperatura = round(data.json()['main']['temp'] - 273)
            humedad = data.json()['main']['humidity']
            bot.send_message(cid, "Bienvenidos al pronostico de heimer pedazo feeders :V \n\nEste es el pronostico del tiempo : \n\nEn *" + ciudad + "\n*Tiempo actual: *" + tiempo + "\n*Nubosidad actual: *" + str(nubosidad) + '%' + "\n*Viento actual: *" + str(viento) + 'km/h' + "\n*Temperatura actual: *" + str(temperatura) + ' C' + "\n*Humedad actual: *" + str(humedad) + '%' + "*\n", parse_mode='markdown')

        else:
             bot.send_message(cid,'tienes que escribir el comando /tempo seguido de una ciudad')


#@bot.message_handler(commands=['temazo']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
#def temazo(m): # Definimos una función que resuleva lo que necesitemos.
    #cid = m.chat.id
    #x=m.text
    #nombre = ' '.join(x.split(" ")[1:])
    #if not x == '/temazo' and not nombre.isdigit():
        #params = { "q" : nombre, "lang" : "es", "appid" : "8619764d7016e3f9410454bb4879186e" , format : "json" }
        #data = requests.get("http://www.last.fm/api/show/track.search", params)
        #name = data.json()['name']
        #artist = data.json()['artist']
        #url = data.json()['url&format=json']
        #streamable = data.json()['streamable']
        #bot.send_message(cid, "Quien ha pedido temazo :V \n\nEsta es la info del temazo que has pedido crack : \n\nNombre:*" + name + "\n*Artista: *" + artist + "\n*URL: *" + url + "\n*Stream: *" + streamable + "*\n", parse_mode='markdown')
        #bot.send_message(cid, "Quien ha pedido temazo :V \n\nEsta es la info del temazo que has pedido crack : ", parse_mode='markdown')







@bot.message_handler(commands=['saludo']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def saludo(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        x=m.text
        saludo = ' '.join(x.split(" ")[1:])
        username = m.from_user.username
        id = m.from_user.id

        import json

        data = {
            'username' : username,
            'idUser' : id,
            'saludo' : saludo,
        }
        json_str = json.dumps(data)
        data = json.loads(json_str)

        with open('data.json', 'w') as f:
            json.dump(data, f)

@bot.message_handler(commands=['sera']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def sera(m): # Definimos una función que resuleva lo que necesitemos.

    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        x = m.text
        nombre = ' '.join(x.split(" ")[1:])
        #bot.send_message(cid,nombre)

        if nombre == "":
            bot.send_message(cid,'tienes que escribir el comando /sera seguido de lo que quieras preguntar')
        else:

            rnd = randrange(0, 100)

            if rnd >= 0 and rnd < 20:
                bot.send_message( cid, 'Vuelve a repetirlo que no me apetece leerlo')

            if rnd >= 20 and rnd < 30:
                bot.send_message( cid, 'Hablale a mis torres seguro que te lo dicen jajaja')

            if rnd >= 30 and rnd < 60:
                bot.send_message( cid, 'Fijo que si campeon')

            if rnd >= 60 and rnd < 90:
                bot.send_message( cid, 'Lo siento amigo pero no XD no va ser eso')

            if rnd >= 90 and rnd < 100:
                bot.send_message( cid, 'Puede que si puede que no')

@bot.message_handler(commands=['sorteito']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def sorteito(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:
        x=m.text
        if x == "/sorteito":
            bot.send_message(cid, 'pon /sorteito seguido de un número positivo')
        else:
            n1 = x.split(" ")[1]
            if n1 == " ":
                bot.send_message(cid,'tienes que escribir el comando /sorteito seguido de un número positivo')
            else:
                if n1.isnumeric():
                    if int(n1)<=0 or int(n1) == 0 or int (n1)>9999999999999999999999999999999999:
                        bot.send_message(cid,'tienes que escribir el comando /sorteito seguido de un número positivo que no sea mayor de 9999999999999999999999999999999999')
                    else:
                        rnd = randrange(0, int(n1))
                        bot.send_message(cid, 'Vamos chicos decid vuestros numeros del 0 al ' + n1)
                        time.sleep(8)
                        bot.send_message(cid, 'Me ha salido el número: ' + str(rnd))



@bot.message_handler(commands=['remindpene']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def recuerdapene(m): # Definimos una función que resuleva lo que necesitemos.

    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        cid = -1001090423519
        id = m.from_user.id
        x=m.text

        if x == "/remindpene":
            bot.send_message(cid,'tienes que escribir el comando /recuerdapene seguido de el tiempo que quieras')
        else:

            n1 = x.split(" ")[1]

            if n1.isnumeric():
                if int(n1)<=0 or int(n1) == 0 or int (n1)>9999999999999999999999999999999999:
                    bot.send_message(cid,'tienes que escribir el comando /recuerdapene seguido de un número positivo que no sea mayor de 9999999999999999999999999999999999')

                else:
                    time.sleep(int(n1))
                    bot.send_message(cid, 'kari di pole')


@bot.message_handler(commands=['dado']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def dado(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id
    baneado = 0
    id = m.from_user.id
    idUser = m.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        id = m.from_user.id
        x=m.text
        if x == "/dado":
            bot.send_message(cid,'tienes que escribir el comando /dado seguido de un número positivo')
        else:
            n1 = x.split(" ")[1]
            if n1.isnumeric():
                if int(n1)<=0 or int(n1) == 0 or int (n1)>9999999999999999999999999999999999:
                    bot.send_message(cid,'tienes que escribir el comando /sorteito seguido de un número positivo que no sea mayor de 9999999999999999999999999999999999')
                    if n1 == 1:
                        bot.send_message(cid, 'hay millones de millonesimos!!')
                else:
                    rnd = randrange(1, int(n1))
                    bot.send_message(cid, rnd)


@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def command_bye(m):

    cid = m.chat.id
    if (m.left_chat_member.username is None):
        nun = m.left_chat_member.first_name
        if (m.left_chat_member.last_name is not None):
            nun += " "
            nun += m.left_chat_member.last_name
        else:
            despedida = "Hasta lue "
            despedida += str(m.left_chat_member.last_name)
            despedida += " "
    else:
        nun = m.left_chat_member.username
        despedida = "Hasta lue "
        despedida += " @"

    bot.send_message(cid, str(despedida) + str(nun) + '\n\nMe parece que alguien ha hecho ragequit XD')


@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_hi(m):
    cid = m.chat.id
    cname = m.chat.title
    id = m.new_chat_members.id
    bienvenida= ""
    if (m.new_chat_members.username is None):
        nun = m.new_chat_members.first_name
        if (m.new_chat_members.last_name is not None):
            nun += " "
            nun += m.new_chat_members.last_name
        else:
            bienvenida = "Bienvenido al grupo "
            bienvenida += str(cname)
            bienvenida += " "
    else:
        nun = m.new_chat_members.username
        bienvenida = "Bienvenido al grupo "
        bienvenida += str(cname)
        bienvenida += " @"

    if cid == -1001090423519:

        bot.send_message(cid, str(bienvenida) + str(nun) + ', donde charlamos de LOL, competitivo además de más juegos y mucho offtopic :D.\nAntes de nada, responde a estas preguntas para que te conozcamos mejor:\n¿Nombre?¿Estudias o trabajas?¿En que?¿Cosas que te encanta hacer?¿Que división eres?¿Cual es tu rol favorito?¿Cual es tu campeón favorito? \n\n¿De que servidor eres? \n\nSi tienes alguna duda del grupo habla a cualquier admin bienvenido y a pasarlo bien')

        click_kb = types.InlineKeyboardMarkup()
        click_button1 = types.InlineKeyboardButton('Normas', url = 't.me/heimibot?start=normas' )
        click_kb.row(click_button1)
        bot.send_message(cid, 'A continuación tienes las normas. Pincha en el boton de debajo para ver las normas', reply_markup=click_kb, disable_web_page_preview=True)

    else:
        bot.send_message(cid, str(bienvenida) + str(nun) + ' vas a tomar parte de un grupo de ragers y feeders :V ' )


#para almacenar los usuarios en txt

    today = date.fromtimestamp(time.time())
    hoy = date(today.year, today.month, today.day)
    info = str(id) + ' * ' + nun + ' * ' + str(hoy)

    my_file = Path('grupos/' + cname + '.txt')
    if my_file.is_file():

        idLista = 0
        nombre = ' '
        numLista = 0
        estaEnLaLista = None
        numLinea = 0
        infile = open('grupos/' + cname + '.txt', 'r')
        for line in infile:
            numLinea = numLinea +1
            idListaS = line.split(' * ')[1]
            idLista = int(idListaS)
            numListaS = line.split(' * ')[0]
            numLista = int(numListaS) + 1
            if id == idLista:
                estaEnLaLista = True
        infile.close()

        if estaEnLaLista == True:
            pass
        else:

            with open('grupos/' + cname + '.txt','a') as fo:
                fo.write(str(numLista) + ' * ' + info + '\n' )



    else:

        with open('grupos/' + cname + '.txt','w') as fo:
            fo.write('1' + ' * ' + info + '\n')

'''@bot.message_handler(func=lambda message: True)
def echo_message(message):
        cid = message.chat.id
        if "5" in message.text.lower():
            x=message.text
            listfrase = x.split()
            ultimo = list(listfrase)
            if ultimo[-2] == '5' and ultimo.long > 1:
                bot.send_message(cid,'por el culo te la inco')'''



def get_streetview(latitude, longitude, key, size='640x320', fov=90, heading=235, pitch=10):
    url = 'http://maps.googleapis.com/maps/api/streetview'
    params = {
        'size': size,
        'location': '%s,%s' % (latitude, longitude),
        'fov': fov,
        'heading': heading,
        'pitch': pitch,
        'key': key
    }

    return download(url, params=params)


@bot.message_handler(func=lambda message: True)
def echo_message(message):

    cid = message.chat.id
    baneado = 0
    id = message.from_user.id
    idUser = message.from_user.id
    idLista = ''
    estaEnLaLista = None
    numLinea = 0
    infile = open('users/baneados.txt', 'r')
    for line in infile:
        numLinea = numLinea +1
        idListaS = line.split(' ')[0]
        idLista = int(idListaS)
        if idUser == idLista:
            baneado = idLista
    infile.close()
    if id != baneado:

        if message.text.lower() == "holi":
            username = message.from_user.username
            id = message.from_user.id
            cid = message.chat.id

            if id == 239822769:
                bot.send_message( cid, 'Hola mi creador 😙')

            elif id == 150982158:
                bot.send_message( cid, 'Hola mi pequeño rager 😎')

            elif id == 197761815:
                bot.send_message( cid, 'Hola Slenee swan awwww 😍' )

            elif id == 22605669:
                bot.send_message( cid, 'OH Emilio o dios mio callaos todos emilio ha dicho holi 😍. Qu tal está su excelentisima persona? ' )

            elif id == 181575406:
                bot.send_message( cid, 'Aiba el ruso loco que pazaaaaa locoooooooooooo!! ' )

            elif id == 17997495:
                bot.send_message( cid, 'Hola señor de las torres ??' )

            elif id == 165425329:
                bot.send_message( cid, 'Hola señorito Halecs ツ')

            elif id == 247295279:
                bot.send_message( cid, 'Hola? Hola y adios \nNo te quiero ni ver puto main shaco de mierda. Solo vienes a hacer ks y te piras en invisible para dejarme vendido mamon')

            elif id == 6857913:
                bot.send_message( cid, 'Hola Bochan achusss! no me contagies ~_~')

            elif id == 241930911:
                bot.send_message( cid, 'Holi holi? \n tipitamadri oli,  yi vini el autista main yasui ojjjjj ?? ')

            elif id == 151637199:
                bot.send_message( cid, 'Saludar a un main singed?\nPara genios splitpushers estoy yo pero bueno por ser un genio loco te dire un: Hola cuando descubras una pocion para ser mas sensual que yo me avisas XD')

            elif id == 9056637:
                bot.send_message( cid, 'Hola su señor o todo poderoso Alejandro perdon ... Aquí esta el tio que no para de matarme y matarme.....')

            elif id== 227675491:
                bot.send_message( cid, 'Hola miri *_* que tal va el día? 😍')

            elif id== 223916845:
                bot.send_message( cid, 'Hola potatoman he estado a punto de morir sigo investigando la desaparición de tu padre algún dia lo encontraré MR.Potatooo :C')

            elif id== 329154829:
                bot.send_message( cid, 'Hola samu. daudd..  a no saduel que tal? :D espero que bien te quieroo *_*')

            elif id== 151637199:
                bot.send_message( cid, 'Saludar a un main singed?\nPara genios splitpushers estoy yo pero bueno por ser un genio loco te dire un: Hola cuando descubras una pocion para ser mas sensual que yo me avisas XD')

            elif id == 125245687 or id == 466540441:
                bot.send_message( cid, 'Saludar a un main akali puff perdona amigo pero si me matas sin verte tampoco te saludare sin verte 😠')

            elif id == 166313667:
                bot.send_message( cid, 'Buenas Silver Wolf, espero que algún día seas Silver Gold :D')

            elif id == 52033876:
                bot.send_message( cid, 'Muy buenas señorito eduardo aunque seas el creador de @League_of_Legends_bot no creas que vayas a superarme soy un 100tifiko muy prestigiado en la ciudad de Bandle tu no seras mas que un simple programador que nadie lo conocerá :V ')

            elif id == 232633539:
                bot.send_message(cid, 'Buenas perrete :) marcate un chiste de esos que me hagan reir :3 ')

            elif id == 137216452:
                bot.send_message(cid, 'Buenas yordle como va la locura? uajajajaja espero que no te pongas a liarla por aqui algunos somos unos 100tifikos que necesitan un poco de paz -.-" ' )

            elif id == 12050858:
                bot.send_message(cid, 'Hola aunque seas casta te saludo no te preocupes. Conmigo igualdad para todos me contradigo pero bueh :V')

            elif id == 278375866:
                bot.send_message(cid, 'Hola nuri como estas :3 😘 jejeje ' )

            elif id == 365770260:
                bot.send_message(cid, 'Hola señor o dios main malzahar' )

            elif id == 318442388:
                bot.send_message(cid, 'Uff uff un experimento fallido de Zaun en tus joder ten cuidado con lo que haces wey vas a matarnos a todos :,( ')

            elif id == 14160671:
                bot.send_message(cid, 'Hola señor del tiempo :) jajaja venga porfavor no se ni que digo este hombre ni tan si quiera juega a zilean XD vete a suparla')

            elif id == 205564581:
                bot.send_message(cid, 'Hola Yafo se que los bots no te quieren pero aqui me tienes que te voy a dar amor del bueno ☺️')

            elif id == 335689163:
                bot.send_message(cid, 'Hola rafi, se que das asco con kata pero eres buen chaval :D')

            elif id == 35434424:
                bot.send_message(cid, 'Hola wachin no me dispares tanto que al final me vas a matar')

        if message.text.lower() == "hola a todos":
            bot.reply_to(message, text_messages['holat'])

        if message.text.lower() == "comemela gilipollas":
            bot.reply_to(message, text_messages['comemela'])

        if message.text.lower() == "manco tu":
            bot.reply_to(message, text_messages['manco'])

        if "haber estudiao" in message.text.lower():
             cid = message.chat.id
             bot.reply_to(message, text_messages['estudiado'])
             bot.send_audio( cid, open( 'extrasLol/estudiao.ogg', 'rb'))

        if "juanma" in message.text.lower():
             bot.reply_to(message, text_messages['juanma'])


        if "selene" in message.text.lower():
             bot.reply_to(message, text_messages['slene'])

        if "salsa" in message.text.lower():
             bot.reply_to(message, text_messages['salsa'])

        if "que dise" in message.text.lower():
            cid = message.chat.id
            bot.send_message(cid, 'Que dise que dise')

        if "he perdido la promo" in message.text.lower():
             bot.reply_to(message, text_messages['promo'])

        if "gracias heimi" in message.text.lower():
             bot.reply_to(message, text_messages['gracias'])

        if "adios" in message.text.lower():
             bot.reply_to(message, text_messages['adios'])

        if ":c" in message.text.lower():
             bot.reply_to(message, text_messages['llora'])

        if "buenos dias" in message.text.lower() or "buenos días" in message.text.lower() :
            #bot.reply_to(message, text_messages['buenosDias'])
            #bot.reply_to(message, "¿Buenos días? chupame un pie no he pegado ojo en toda la noche que puto calor joderrrrrrr!")
            bot.reply_to(message, 'Que buenos días ni que buenos días, que si hoy hace frío que si hoy hace calor , que te den los buenos días mis torres. Mamonaso. ')
        if "remusen" in message.text.lower():
             bot.reply_to(message, text_messages['remusen'])



        if "chocala" in message.text.lower() or "choca esos cinco" in message.text.lower() or "choca" in message.text.lower() or "que buena heimer" in message.text.lower():
                bot.reply_to(message, text_messages['chocala'])


        if "puto heimer" in message.text.lower():
                bot.reply_to(message, text_messages['puto'])

        if "puto bot" in message.text.lower():
                bot.reply_to(message, text_messages['putoBot'])


        if "baia" in message.text.lower():

            with open('/home/heimiBot/baia.var', 'r') as baia:
	            cont = int(baia.readline())

            cid = message.chat.id

            if cont<8:
                with open('/home/heimiBot/baia.var', 'w') as baia_w:
                    baia_w.write(str(cont+1))

                if cont < 4:
                    bot.send_message( cid, message.text + ' baia' )


                if cont == 4:
                    bot.send_message( cid, ' Paraaaaaaaad con el baia')

            elif cont>=8:
                with open('/home/heimiBot/baia.var', 'w') as baia_w:
                    baia_w.write(str(0))
                    cont = 0



        if "tarta" in message.text.lower():
            cid = message.chat.id
            bot.send_photo( cid, open( 'ahri.jpg', 'rb'))

        if "emilio" in message.text.lower():
            cid = message.chat.id
            bot.send_message( cid, 'emilio = puto amo')

        if "soraka" in message.text.lower():
            cid = message.chat.id
            bot.send_message( cid, 'ains mi Soraka 😍❤️ 😍')

        if "yasuo" in message.text.lower():
            cid = message.chat.id
            bot.send_message( cid, 'Manuel odia a Jhon Elmis y su yasuo')


        if "heimi di " in message.text.lower():
            id = message.from_user.id
            cid = message.chat.id
            if id != 50105411:
                x=message.text
                nombre = ' '.join(x.split(" ")[2:])
                bot.send_message(cid, nombre)


        if  message.text.lower() == "felis navidad":
            cid = message.chat.id
            bot.send_message(cid, 'prospero ano y falosidad ')

        if "heimer mata a elmo" in message.text.lower() or "elmo muere" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'elmo.gif', 'rb'))

        if "caranchoa" in message.text.lower() or "cara anchoa" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'caranchoa.gif', 'rb'))

        if "no sense" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'nosense.gif', 'rb'))

        if "dick" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.



            rnd = randrange(1, 43)

            bot.send_photo( cid, open( 'pene/' + str(rnd) + '.jpg', 'rb'))

        if "heimi te amo" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.



            rnd = randrange(1, 40)

            bot.send_photo( cid, open( 'heimiF/' + str(rnd) + '.jpg', 'rb'))

        if "kappa" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_photo( cid, open( 'kappa.png', 'rb'))

        if "toma toma" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'toma.gif', 'rb'))

        if "barba" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'barba.gif', 'rb'))

        if "killsteal" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'ks.gif', 'rb'))

        if "facepalm" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'facepalm.gif', 'rb'))

        if "heimi mata a " in message.text.lower():
            cid = message.chat.id
            x=message.text
            nombre = ' '.join(x.split(" ")[3:])
            bot.send_message( cid, 'tratratra pichum pichum pujjjj pujj muere ' + nombre + ' mecauen tiiii!!!!')

        if "me suisido" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'alakbar.ogg', 'rb'))

        if "vodka" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'vodka.ogg', 'rb'))

        if "me aburro" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'extrasLol/aburrido.ogg', 'rb'))


        if "kata" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_document( cid, open( 'audios/kata_audio.ogg', 'rb'))


        if "troll" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'extrasLol/villaTroll.ogg', 'rb'))

        if "boom" in message.text.lower():
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/headshot.ogg', 'rb'))

        if "boom" in message.text.lower():
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/ganee_audio.ogg', 'rb'))

        if "zas en toda la boca" in message.text.lower():
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/zas en toda la boca_audio.ogg', 'rb'))

        if "a trollear" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'extrasLol/hacerTroll.ogg', 'rb'))

        if "quien juega" in message.text.lower() or "alguien juega" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'extrasLol/solo2.ogg', 'rb'))

        if "perdido" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'extrasLol/perdido.ogg', 'rb'))

        if "estoy solo" in message.text.lower() or "estoy sola" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'extrasLol/solo1.ogg', 'rb'))

        if "buenas noches" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
            bot.send_audio( cid, open( 'extrasLol/buenasNoches.ogg', 'rb'))

        if "#miembro" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder
            x=message.text
            user = ' '
            usuario = ' '
            idUser = message.from_user.id
            idLista = ''
            estaEnLaLista = None
            numLinea = 0
            infile = open('users/miembros.txt', 'r')
            for line in infile:
                numLinea = numLinea +1
                idListaS = line.split(' * ')[1]
                idLista = int(idListaS)
                if idUser == idLista:
                    estaEnLaLista = True
            infile.close()

            if estaEnLaLista == True:
                bot.send_message(cid, 'ya estabas en la lista wap@')
            else:

                if (message.from_user.username is None):
                    user = message.from_user.first_name
                else:
                    user = '@ '+message.from_user.username
                miembroI = x.split(' ')[0]
                if miembroI == '#miembro':

                    with open('/home/princebot/users/cont1.var', 'r') as cont:
                        cont = int(cont.readline())
                    with open('/home/princebot/users/cont1.var', 'w') as cont_w:
                        cont_w.write(str(cont+1))
                    mensaje = ' '.join(x.split(" ")[1:])
                    with open('users/miembros.txt','a') as fo:
                        fo.write(str(cont-6) + ' * ' + str(idUser) + ' * ' + user + ' * ' + mensaje + '\n')
                    bot.send_message(cid, 'gracias ' +user+ ' te acabo de apuntar en la lista de mancos, gracias por aportar tu nickname, ahora sabré que tampoco tengo que jugar contigo porque eres un manco de mierda :D ')
                else :
                    bot.send_message(cid, 'si quieres que te pase la lista introduce #miembro seguido de tu nombre salu2 torpe de mierda  ')

        if "#chistedeldia" in message.text.lower():
            cid = message.chat.id # Guardamos el ID de la conversación para poder responder
            x=message.text

            if (message.from_user.username is None):
                user = message.from_user.first_name
            else:
                user = '@'+message.from_user.username
            chisteI = x.split(' ')[0]

            if chisteI == '#chistedeldia':

                with open('/home/heimiBot/chistes/cont.var', 'r') as cont:
                    cont = int(cont.readline())
                with open('/home/heimiBot/chistes/cont.var', 'w') as cont_w:
                    cont_w.write(str(cont+1))
                mensaje = ' '.join(x.split(" ")[1:])
                with open('chistes/chistes.txt','a') as fo:
                    fo.write(str(cont) + ' '+ user + ' * ' + mensaje + '\n')
                bot.send_message(cid, 'gracias ' +user+ ' tu chiste se ha guardado correctamente :)')
            else :
                bot.send_message(cid, 'si quieres que guarde tu chiste haz el favor de escribir primero #chistedeldia seguido del chiste :) ')
        if "audio lux" in message.text.lower():

            cid = message.chat.id

            rnd = randrange(1, 4)
            bot.send_audio( cid, open( 'lux/' + str(rnd) + '.ogg', 'rb'))


        if "audio ralph" in message.text.lower():
            cid = message.chat.id
            rnd = randrange(1, 24)
            bot.send_audio( cid, open( 'ralf/' + str(rnd) + '.ogg', 'rb'))


        if "audio peli" in message.text.lower():
            cid = message.chat.id
            rnd = randrange(1, 53)
            bot.send_audio( cid, open( 'peli/' + str(rnd) + '.ogg', 'rb'))

        if "audio lol" in message.text.lower():
            cid = message.chat.id
            rnd = randrange(1, 8)
            bot.send_audio( cid, open( 'lol/' + str(rnd) + '.ogg', 'rb'))

        if message.text.lower() == "microagresion" or message.text.lower() == "@estrellito":
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/microagresion_audio.ogg', 'rb'))

        if message.text.lower() == "chupala":
            cid = message.chat.id
            bot.send_audio( cid, open( 'audios/chupala_audio.ogg', 'rb'))





#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
