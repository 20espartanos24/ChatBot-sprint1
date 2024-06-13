import re
import random

# Función principal que procesa la entrada del usuario y obtiene la respuesta del chatbot
def obtener_respuesta(entrada_usuario):
    # Dividir el mensaje del usuario en palabras individuales
    mensaje_dividido = re.split(r'\s|[,:;.?!-_]\s*', entrada_usuario.lower())
    # Obtener la respuesta basada en las palabras del mensaje
    respuesta = verificar_todos_los_mensajes(mensaje_dividido)
    return respuesta

# Función para calcular la probabilidad de que el mensaje del usuario coincida con una respuesta reconocida
def calcular_probabilidad(mensaje_usuario, palabras_reconocidas, respuesta_unica=False, palabras_requeridas=[]):
    certeza_mensaje = 0
    tiene_palabras_requeridas = True

    # Contar cuántas palabras reconocidas están en el mensaje del usuario
    for palabra in mensaje_usuario:
        if palabra in palabras_reconocidas:
            certeza_mensaje += 1

    # Calcular el porcentaje de certeza
    porcentaje = float(certeza_mensaje) / float(len(palabras_reconocidas))

    # Verificar si todas las palabras requeridas están en el mensaje del usuario
    for palabra in palabras_requeridas:
        if palabra not in mensaje_usuario:
            tiene_palabras_requeridas = False
            break

    # Retornar la probabilidad como un entero de 0 a 100
    if tiene_palabras_requeridas or respuesta_unica:
        return int(porcentaje * 100)
    else:
        return 0

# Función para verificar todas las posibles respuestas y seleccionar la mejor coincidencia
def verificar_todos_los_mensajes(mensaje):
    mayor_probabilidad = {}

    # Función auxiliar para agregar una posible respuesta al diccionario de probabilidades
    def agregar_respuesta(respuesta_bot, lista_de_palabras, respuesta_unica=False, palabras_requeridas=[]):
        nonlocal mayor_probabilidad
        mayor_probabilidad[respuesta_bot] = calcular_probabilidad(mensaje, lista_de_palabras, respuesta_unica, palabras_requeridas)
        
    # SALUDOS
    # Definir las respuestas posibles y sus palabras clave asociadas
    agregar_respuesta('Hola', ['hola', 'saludo', 'saludos', 'buenas'], respuesta_unica=True)
    agregar_respuesta('Estoy bien y tú?', ['como', 'estas', 'vas', 'sientes'], respuesta_unica=True)
    agregar_respuesta('Que bueno que te encuentres bien', ['bien', 'todo', 'encuentro', 'super', 'genial'], palabras_requeridas=['bien'])
    agregar_respuesta('¡Claro! Estoy aquí para ayudarte. ¿Qué deseas saber?', ['ayuda','necesito', 'quisisera', 'ayudes', 'ayuda','ayudar'], respuesta_unica=True)
    agregar_respuesta('Me llamo Espartano, en que puedo ayudarte?', ['nombre','como','cual','llamas'], respuesta_unica=True)
    agregar_respuesta('No te preocupes, estare aqui para ayudar!', ['perdon', 'siento'], respuesta_unica=True)
    agregar_respuesta('Lamento oir eso. Procura repasar a tiempo y consulta tus dudas al docente', ['estoy', 'mal','curso','que','pesimo','grave'], respuesta_unica=True)


    # ACERCA DE LA UNIVERSIDAD CONTINENTAL
    # Definir las respuestas posibles y sus palabras clave asociadas
    agregar_respuesta('La Organización Educativa Continental nace en Huancayo como Centro de Cómputo en 1983.'+ 
                      'Sin embargo, gracias al crecimiento e innovación, en 1998 se fundó la Universidad Continental'+ 
                      ' de Ciencias e Ingeniería (Hace 23 años iniciábamos con 3 carreras y con solo 180 estudiantes.'+ 
                      ' Hoy somos más de 44 mil estudiantes en nuestros diferentes campus Huancayo, Arequipa, Cusco y Lima.)', 
                      ['contar', 'reseña', 'historia', 'universidad', 'continental'], respuesta_unica=True)
    agregar_respuesta('La Universidad Continental cuenta con 29 carreras profesionales', ['carrera', 'carreras','cuantas','que'], respuesta_unica=True)
    agregar_respuesta('La Universidad Continental cuenta con las modalidades presencial, semipresencial y a distancia.', ['modalidad', 'modalidad','modalidades','que'], respuesta_unica=True)
    agregar_respuesta('Estamos ubicados en Sector Angostura km. 10 - San Jerónimo', ['ubicados', 'dirección', 'donde', 'cusco','Cusco','cual'], respuesta_unica=True)
    agregar_respuesta('Estamos ubicados en Av. Alfredo Mendiola 5210 Los Olivos - Lima', ['ubicados', 'dirección', 'donde', 'lima','Lima','cual'], respuesta_unica=True)
    agregar_respuesta('Estamos ubicados en La Canseco II / Sector: Valle Chili José Luis Bustamante y Rivero - Arequipa', ['ubicados', 'dirección', 'donde', 'arequipa','Arequipa','cual'], respuesta_unica=True)
    agregar_respuesta('Estamos ubicados en Av. San Carlos 1980 Urb. San Antonio - Huancayo', ['ubicados', 'dirección', 'donde', 'huancayo','Huancayo','cual'], respuesta_unica=True)
    agregar_respuesta('¡De nada! Estoy aquí para ayudar', ['gracias', 'te lo agradezco', 'informacion','información'], respuesta_unica=True)
    #A cerca de los cursos
    agregar_respuesta('Este semestre estás inscrito en los siguientes cursos: Arquitectura Empresarial,'+
                      ' Redes de Computadores, Construccion de Software, Ingenieria economica, Gestion profesional e innovacion social',   ['Que', 'cursos', 'que', 'llevando','llevo'], respuesta_unica=True)
    agregar_respuesta('El curso de Arquitectura empresarial lo dicta el docente Erick Alcca Zela.', ['arquitectura', 'empresarial','quien'], respuesta_unica=True)
    agregar_respuesta('El curso de Construccion de software lo dicta el docente Hugo Espetia Huamanga.', ['construccion', 'software','quien'], respuesta_unica=True)
    agregar_respuesta('El curso de Gestion Profesional lo dicta el docente Jesus Castro Mardiaga.', ['gestion', 'profesional','quien'], respuesta_unica=True)
    agregar_respuesta('El curso de Ingenieria economica lo dicta la docente Veronica Garcia Tovar.', ['ingenieria', 'economica','quien'], respuesta_unica=True)
    agregar_respuesta('El curso de Innovacion social lo dicta la docente yesenia Florez Mujica.', ['innovacion', 'social','quien'], respuesta_unica=True)
    agregar_respuesta('El curso de Redes de Computadores lo dicta el docente Erick Alcca Zela.', ['redes', 'computadores','quien'], respuesta_unica=True)
        #Horario y dias
    agregar_respuesta('El curso de Arquitectura empresarial lo llevas los dias lunes de 5:20 pm a 6:49 pm '+
                      'y los dias miercoles de 3:40 pm a 6:49 pm', ['arquitectura', 'empresarial','dia','dias'], respuesta_unica=True)
    agregar_respuesta('El curso de Construccion de Software lo llevas los dias miercoles de 2:00 pm a 3:29 pm '+
                      'y los dias jueves de 2:00 pm a 5:09 pm', ['construccion', 'software','dia','dias'], respuesta_unica=True)
    agregar_respuesta('El curso de Gestion Profesional lo llevas el dia jueves de manera remota a las 7:00 pm a 8:29 pm ', ['gestion', 'profesional','dia','dias'], respuesta_unica=True)
    agregar_respuesta('El curso de Ingenieria Economica lo llevas los dias lunes a las 7:00 am a 8:29 am '+
                      'y los dias jueves de 8:40 am a 10:09 am', ['ingenieria', 'economica','dia','dias'], respuesta_unica=True)
    agregar_respuesta('El curso de Innovacion Social lo llevas el dia viernes de 2:00 pm a 5:09 pm ', ['innovacion', 'social','dia','dias'], respuesta_unica=True)
    agregar_respuesta('El curso de Redes de Computadores lo llevas el dia lunes de 3:40pm a 5:09pm '+
                      'y los dias martes de 3:40 pm a 6:49 pm ', ['redes', 'computadores','dia','dias'], respuesta_unica=True)
    agregar_respuesta('El curso de construccion de software lo llevas en el aula A304 los dias miercoles y los'
                      +' jueves en el aula A801', ['construccion', 'aula','salon','clase','en','que'], respuesta_unica=True)
    agregar_respuesta('El NRC del curso de construccion de software es: 12861. ', ['nrc', 'NRC','que','construccion','software'], respuesta_unica=True)
    agregar_respuesta(' Las pruebas unitarias son como revisiones detalladas de cada parte del código,'
                      +'como inspeccionar piezas de un rompecabezas para asegurarse de que encajen perfectamente.'
                      +' Ayudan a encontrar errores desde el principio y mantienen el software confiable al verificar'
                      +'funciones y métodos individualmente. Es fundamental para asegurar que todo funcione como se '
                      +'espera y para evitar problemas costosos en etapas avanzadas del desarrollo.', ['pruebas', 'unitarias','construccion','que'], respuesta_unica=True)

    agregar_respuesta('Fui creado en junio del 2024 en Cusco-Peru, mi dueño legal es el señor Hugo Espetia pero '
                      +'suelen usarme de manera gratuita sin restricciones.', ['dueño', 'quien','te','creo','es','naciste','cuando'], respuesta_unica=True)
    
    agregar_respuesta('El primer sprint del proyecto debe presentarse el dia 13 de junio del 2024. ', ['sprint', 'construccion','dia','dias','primer'], respuesta_unica=True)
    agregar_respuesta('El segundo sprint del proyecto debe presentarse el dia 27 de junio del 2024. ', ['sprint', 'construccion','dia','dias','segundo'], respuesta_unica=True)
    agregar_respuesta('El actual semestre academico(2024-1) culmina el dia viernes 5 de julio. Puede extenderse en caso lleves '
                      'un examen sustiturio.', ['cuando', 'acaba','termina','culmina','semestre'], respuesta_unica=True)

    
    # Encontrar la mejor coincidencia basada en la mayor probabilidad
    mejor_coincidencia = max(mayor_probabilidad, key=mayor_probabilidad.get)
    
    # Retornar una respuesta desconocida si la mejor coincidencia tiene una probabilidad muy baja
    return obtener_respuesta_desconocida() if mayor_probabilidad[mejor_coincidencia] < 1 else mejor_coincidencia

# Función para generar una respuesta aleatoria en caso de que no se entienda la entrada del usuario
def obtener_respuesta_desconocida():
    respuestas_desconocidas = [
        '¿Puedes decirlo de nuevo?',
        'No estoy seguro de lo que quieres decir.'
    ]
    return respuestas_desconocidas[random.randrange(len(respuestas_desconocidas))]

# Función principal para iniciar el chat
def iniciar_chat():
    print("¡Hola! Soy el ChatBot Espartano. Para salir, escribe 'adiós'.")
    while True:
        entrada_usuario = input("Tú: ")
        if entrada_usuario.lower() in ["adios", "hasta luego", "nos vemos","chau"]:
            print("ChatBot: Hasta luego.")
            break
        respuesta = obtener_respuesta(entrada_usuario)
        print("ChatBot: " + respuesta)

# Iniciar el chat si el script se ejecuta directamente
if __name__ == "__main__":
    iniciar_chat()
