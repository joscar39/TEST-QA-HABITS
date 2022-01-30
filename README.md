###### TEST-QA-HABITS   ######
Repositorio para prueba Tecnica, postulacion al puesto de QA Automatizador

El repositorio cuenta con dos carpetas, cada una identificada con el titulo de la prueba propuesta



La primera carpeta llamada API – PRUEBA DE CARGA Y PERFORMANCE


muestra todo el desglose que contiene el proceso de ejecucion de pruebas de api en la prueba

se utilizo la herramienta Jmeter para esta tarea, la carpeta cuenta con:

    -Folder de Recursos: Contiene archivos CSV con una listqa de datos usados como variables dentro de la automatizacion
  
    -Archivo "DESARROLLO DE LA PRUEBA": Este archivo es la documentacion de todos los procesos que se hiceron en cada uno de los pasos de la prueba de API
  
    -Archivo PizzaOrders.jmx : Este archivo es el el formato exportado de toda la prueba, para poder correrlo, deberan abrirlo con Jmeter para que se muestre el contenido completo
  
    -Archivo Summary.CSV : Este archivo contiene el resultado del test report con lo que mostrara una tabla con los contenidos de tiempo de ejecucion por cada request ademas de        otros   datos de relevancia en la prueba. para mostrar la tabla correctamente se debera abrir un archivo excel e ingresar a la pestaña de "Datos" entre las opciones de la          pestaña buscar   una llamada datos de texto, y alli pedira buscar un archivo para abir es alli donde se debera seleccionar el archivo CSV de Summary
 
 
 
La Segunda carpeta es llamada INTERFAZ – PRUEBA DE FUNCIONALIDAD


Muestra el contenido de los archivos utilizados para la realizacion de la prueba manual y de automatizacion

el contenido de la carpeta esta distribuido de la siguiente manera:

      - Carpeta .idea : Parte de la configuracion de las variables de entorno creadas por python
      
      - Carpeta venv : PArte de la configuracion de las variables de entorno creadas por python
      
      - Archivo Casos de prueba.xlxs: Plantilla de testcases a realizar, donde se muestra los casos de usos con resultados esperados, los resultados obtenidos y las incidencias         o errores encontrados en le proceso de la ejecucion de pruebas manuales
      
      - Archivo Recursos.zip : Es una carpeta comprimida que contiene todos los recursos usados en la ejecucion de pruebas tanto manuiales como automatizadas, dentro de dicha          carpeta se encontrara
                Carpeta de Drivers: Esta carpeta contiene el chromdriver,exe necesario para poder hacer las automatizaciones
                
                carpeta de screenshot: esta carpeta almacena cada una de las capturas de pantallas que se generaban al concretar un paso exitoso en la automatizacion
                
                Imagen avatar.png : Imagen usada para la automatizacion en el paso donde amerita ingresar una imagen en un campo
                
                Imagen de CAPTURA DE FINALIZACION: dicha imagen es una captura de pantalla de momenot en que se finalizo la prueba manual demostrando el tiempo tardado para la                   ejecucion de la prueba, esta captura de pantalla fue solicitada en lso requerimeintos de la prueba
                
                Archivo Datos.xlsx: Archivo que contiene conjunto de datos utilizados para llenarse automaticamente en el formulario de registro de correo en la pantalla 2 del                   sistema
        - Resumen de la prueba.docs : documento worl con el resumen general de la prueba manual y automatizada, donde se describe los distintas novedades obtenidas a lo largo de           la ejecucion de las pruebas
        
        - UserInyerface.py : Archivo python unittest archivo que contiene todo el codigo de la prueba, dicho codigo solo llego hasta el proceso de la pantalla 3 ya que un                  problema mayor con el diseño de la web no dejaron avanzar con la codificacion de la automatizacion, ya que ameritaba obtener mas recurso de tiempo para ejecutar casos            de prueba con herramientas para el manejo de elementos del sistema operativo de windows
        
        
    :::::::::::: NOTA   POR NADA DEL MUNDO SE DEBE MODIFICAR LA EXTRUCTURA DE LSO ARCHIVOS Y LAS CARPETAS YA QUE LA CODIFICACION DE LAS RUTAS EN ALGUNOS CASOS DEBEN MANTENER EL MISMO ESQUEMA QUE ESTA ACTUALMENTE:::::::::::::::::::::::
    
    ::::::::::::: PARA LA CARPETA DE RECURSOS UNICAMENTE DEBERAN UTILIZAR LA OPCION DE ""EXTRAER AQUI"" CON DICHA ACCION ES SUFICIENTE PARA DEJAR TODO IGUAL PARA QUE LAS PRUEBAS FUNCIONEN CORRECTAMENTE:::::::::::::::::::::::::::::::::::
                
                
