"""
PROJETO DE DOWNLOAD E CONVERSÃO DE VÍDEOS DO YOUTUBE PARA MP3
"""

""""
Autor: Gregory Wells
Criado: 18/02/22
Objetivo: Criar meu próprio app de download e conversão de vídeos do Youtube para MP3.

OBS.: Toda vez que for baixar uma música precisará indicar o caminho do diretório para onde mandar a música!
"""
from pytube import YouTube  #aqui importei o objeto Youtube
import moviepy.editor as me #Esse módulo fará a edição para o formato MP3
import re
import os   #aqui estou importando meu sistema operacional para conseguir salvar o arquivo em uma pasta

#Entrada dos dados:
link = input('Digite o link do vídeo: ')    #traga a url aqui
yb = YouTube(link)  #instanciei um objeto yb na classe Youtube utilizando o link como parâmetro
caminho = input('Digite o caminho onde deseja salvar o arquivo: ')

#Baixando
print('Aguarde um momento') #aqui é para verificar que até então o código está rodando como deveria
youtube = yb.streams.filter(only_audio=True).first().download(caminho)  #essa linha de código fará o download e salvará
#no caminho apresentado ao programa. Only_audio mostra que sairá do formato vídeo para o formato áudio como queremos!
print('Convertendo')    #novamente, para mostrar que o código está progredindo

#Conversão de mp4 para mp3
for file in os.listdir(caminho): #para cada arquivo na lista de arquivos do diretório apresentado pelo caminho, faça:
    if re.search('mp4', file):  #caso encontre um arquivo em mp4, faça:
        mp4_caminho = os.path.join(caminho, file)   #irá procurar o caminho onde foi salvo
        mp3_caminho = os.path.join(caminho, os.path.splitext(file)[0]+'.mp3')  #transformar em áudio
        new_file = me.AudioFileClip(mp4_caminho)    #
        new_file.write_audiofile(mp3_caminho)   #transforma o arquivo em mp3
        os.remove(mp4_caminho)  #após convertido, o arquivo em mp4 será removido
print('Processo Finalizado!')

