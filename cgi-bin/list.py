#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()
import db

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
form=cgi.FieldStorage()
hbdb=db.Doctor('localhost','usuario','usuario','ejercicio4')
data=hbdb.get_doctors()
data2=hbdb.get_images()
html=f"""
        <!-- HTML5 -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8"/>
    <title> Ejercicio 4</title>
    <link rel="stylesheet" type="text/css" media="screen" href="../style.css"/>
</head>
<body>

<ul class="topnav">
    <li><a class="active" href="../index.html">Inicio</a></li>
    <li><a href="../add_doctor.html">Agregar Datos de Médico</a></li>
</ul>

<div>
    <!-- Body of page -->
    <h1>Tabla de medicos</h1>
    <table>
    <tr>
    <th>Nombre </th>
    <th>Experiencia</th>
    <th>Especialidad</th>
    <th>Email</th>
    <th>Celular</th>
    <th>Foto</th>
"""
print(html)
for d,d2 in zip(data,data2):
    row=f"""
        <tr>
            <th>{str(d[1])}</th>
            <th>{str(d[2])}/th>
            <th>{str(d[3])}</th>
            <th>{str(d[4])}</th>
            <th>{str(d[5])}</th>
            <th><img src={"../"+str(d2[0])} alt="" width="120" height="120"></th>
        </tr>
        """
    print(row)
        


b2="""
</table>
</div>
</body>
</html>

"""
print(b2)