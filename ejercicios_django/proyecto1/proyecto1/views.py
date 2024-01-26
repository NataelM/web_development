from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    '''
    Las funciones en un framework de django se llaman funciones
    vista
    '''
    p1 = Persona('Act Jonathan', 'Ramirez')
    #nombre = 'Jonathan'
    #apellido = 'Ramirez'

    temas_curso = ['plantillas', 'modelos', 'formualrios', 'vistas', 'despliegue'] 

    ########################### metodo a la antiguita para caragr el template
    #apertura del html
    #path = 'C:/Users/jonat/OneDrive/Documentos/Proyectos/desarrollo_web/ejercicios_django/proyecto1/proyecto1/templates/mi_plantilla.html'
    #doc_externo = open(path)
    # aquí se lee el archivo html previamente cargado
    #plantilla = Template(doc_externo.read())
    #doc_externo.close()
    # aquí (en el context) se configuran los parametros que son variables en el html

    ########################## metodo loader para cargar las plantillas 
    # cuando se usa el metodo loader, en el archivo settings.py debemos poner la ruta de
    # donde vive nuestra plantilla, esta ruta va dentro de la lista llamada TEMPLATES(DIR)
    # plantilla = loader.get_template('mi_plantilla.html')
    
    # ahora no es necesario pasarle el diccionario dentro del metodo context
    # con el loader ahora sólo hay que pasar el diccionario
    dict_contexto = {'nombre_persona':p1.nombre,
                        'apellido_persona': p1.apellido,
                        #pasarle una lista
                        'temas': temas_curso,
                        }
    # Renderizar documento
    #texto = plantilla.render(dict_contexto)

    #return HttpResponse(texto)

    ####################### tercera forma de cargar plantilla: ahora es con loader pero de shortcuts
    return render(request, "mi_plantilla.html", dict_contexto)

    
def video_yt(request):
    fecha_actual = datetime.datetime.now()
    dict_contexto = {
                    'dame_fecha': fecha_actual
                    }

    return render(request, "video.html", dict_contexto)


def equipo(request):
    fecha_actual = datetime.datetime.now()
    dict_contexto = {
                    'dame_fecha': fecha_actual
                    }

    return render(request, "equipos.html", dict_contexto)



def despedida(request):
    '''
    Las funciones en un framework de django se llaman funciones
    vista
    '''
    return HttpResponse('adios')

def dame_fecha(request):

    fecha_actual = datetime.datetime.now()
    str_fecha = f'''
    <body>
    <h2>
    Fecha y hora actuales: {fecha_actual}
    </h2>
    </body>
    '''

    return HttpResponse(str_fecha)

def calcula_edad(request, edad:int, anio:int):
    
    periodo = anio - int(datetime.datetime.now().year)

    edad_futura = edad + periodo

    documento = f'''
    <body>
    <h2>
    en el año {anio} tendras {edad_futura} años
    </h2>
    </body>
    '''
    return HttpResponse(documento)
