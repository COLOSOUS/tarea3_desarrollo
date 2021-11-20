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
hbdb=db.Event('localhost','usuario','usuario','foundbypets')

data=(form['region'].value,form['comuna'].value,form['sector'].value,form['nombre'].value,form['email'].value,form['celular'].value,form['red-social'].value,form['dia-hora-inicio'].value,form['dia-hora-termino'].value,form['descripcion-evento'].value,form['tipo-comida'].value,form["foto-comida"])



hbdb.save_pet1(data)
mensaje = """
<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <title></title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <meta property="og:title" content="">
  <meta property="og:type" content="">
  <meta property="og:url" content="">
  <meta property="og:image" content="">

  <link rel="manifest" href="site.webmanifest">
  <link rel="apple-touch-icon" href="icon.png">
  <!-- Place favicon.ico in the root directory -->

  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/main.css">

  <meta name="theme-color" content="#fafafa">

</head>

<body>


  <button onclick="window.location.href = '../formulario_evento.html';">Informar evento</button><br>
  <button onclick="window.location.href = '../lista.html';">Ver listado de eventos</button><br>
  <button onclick="window.location.href = '../estadisticas.html';">Estadísticas</button><br>




  <!-- Add your site or application content here -->
  <p>Listado de eventos</p>
  <script src="js/vendor/modernizr-3.11.2.min.js"></script>
  <script src="js/plugins.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  <script src="js/main.js"></script>
  <script>

  </script>
  <style type="text/css">
.tftable {font-size:25px;color:#333333;width:100%;border-width: 1px;border-color: #a9a9a9;border-collapse: collapse;}
.tftable th {font-size:25px;background-color:#b8b8b8;border-width: 1px;padding: 8px;border-style: solid;border-color: #a9a9a9;text-align:left;}
.tftable tr {background-color:#cdcdcd;}
.tftable td {font-size:25px;border-width: 1px;padding: 8px;border-style: solid;border-color: #a9a9a9;}
</style>



El formulario se a enviado con exito





  </body>
</html>
        """
print(mensaje)
