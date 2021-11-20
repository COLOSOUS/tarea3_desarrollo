#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
from utils import imprimeerror
import os
import filetype
MAX_FILE_SIZE = 10000 * 1000  # 10 MB
class Event:

    def __init__(self, host, user, password, database):
        self.db=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor=self.db.cursor()

    def save_event(self, data):
        # procesar y guardar el archivo
        fileobj = data[5]

        filename = fileobj.filename

        if not filename:
            imprimeerror(10, 'Archivo no subido')

        # verificamos el tipo
        size = os.fstat(fileobj.file.fileno()).st_size

        if size > MAX_FILE_SIZE:
            imprimeerror(1000, 'Tamaño excede 10mb')

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM archivos"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = 'media/' + hash_archivo+".png"
        open(file_path, 'wb').write(fileobj.value)

        # verificamos el tipo, si no es valido lo borramos de la db
        tipo = filetype.guess(file_path)
        if (tipo.mime != 'image/png') and (tipo.mime != 'image/jpeg'):
            os.remove(file_path)
            imprimeerror(40, 'Tipo archivo no es una imagen png o jpeg')

        # guardamos la imagen en la db
        sql = """
                    INSERT INTO archivos (path,filename, peso)
                    VALUES ( %s,%s, %s)
                """
        self.cursor.execute(sql, (file_path,filename,size))
        self.db.commit()  # id
        id_archivo = self.cursor.getlastrowid()
        #print(id_archivo)
        ##---------------------------------------------------------------

        sql="""
            INSERT INTO m_encontrada(Region,Comuna,Sector,Nombre,Email,Numero,Redes,Inicio,Termino,Descripcion,Tipo,foto_id)
            VALUES(%s,%s,%s,%s,%s,%s)
            """
        self.cursor.execute(sql,(*data[0:5], id_archivo))
        self.db.commit()


    """def get_pets(self):
        self.cursor.execute(f'SELECT * FROM m_encontrada')
        return self.cursor.fetchall()
    def get_images(self):
        self.cursor.execute(f'SELECT path  FROM medico, archivos WHERE medico.foto_id=archivos.id')
        return self.cursor.fetchall()
        """
