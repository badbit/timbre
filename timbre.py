#!/usr/bin/env python
# coding=utf-8
# Programa para elegir una canción aleatoriamente y reproducirla.

import os
import random
import dircache

# Carpeta donde se encuentran las canciones.
dir = "/home/patria/mp3/nuevas"
dirv = "/home/patria/mp3/viejas"

#Elegir una canción al azar.
filename = random.choice(os.listdir(dir))
print filename

# Crear el nombre completo con ruta, cambia los espacios por caracteres
# de escape.
path = os.path.join(dir, filename).replace(" ", "\ ").replace("(", "\(").replace("&", "\&").replace("&", "\&").replace("\'", "\\'").replace(")", "\)")
#reproducidas = os.path.join
print path

# Comando para reproducir la canción.
cmd = 'cvlc --play-and-exit ' + path

print cmd

# Ejecutar el comando.
os.system(cmd)

# Mover la canción reproducida a una nueva carpeta.
cmd = 'mv ' + path + ' ' + dirv

os.system(cmd)

print cmd
