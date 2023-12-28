from django.shortcuts import render, HttpResponse
#from .models import Paciente
from django.template import loader
import pymongo
from .forms import AltaPaciente

# Create your views here.
def home(request):
    return render(request, "core/home.html")
def paciente(request):
   # return HttpResponse("pacciente")
    return render(request, "core/paciente.html")
#def prueba(request):
#    return render(request, "core/prueba.html")

def prueba(request):
  formulario = AltaPaciente(request.POST)
  # mydata = Paciente.objects.values_list('nombre')
  # pacientes = Paciente.objects.all()
  # print ('-->', Paciente.objects.values('nombre'))

  # context = {'pacientes': pacientes}
  # return render(request, 'core/prueba.html', context)

  myclient = pymongo.MongoClient("mongodb://localhost:27017/")

  print('-------------------------------')
  mydb = myclient["gestion"]
  mycol = mydb["paciente"]
  myquery = { "dni": "46833262H" }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print('x', x)
  print('fin')

  x = mycol.find()

  context = {'pacientes': x}
 # return render(request, 'core/prueba.html', context)

  if request.method == 'POST':
      print('se mete por el POST')
      # Si la solicitud es POST, procesa el formulario
      formulario = AltaPaciente(request.POST)
    #  if formulario.is_valid():
          # Haz algo con los datos del formulario
      nombre = request.POST.get('nombre')
      print('nombre: ' + nombre)
      apellido1 =  request.POST.get('apellido1')
      dni =  request.POST.get('dni')
      print('dni: ', dni, ', nombre: ', nombre)
          # Puedes realizar acciones como guardar en la base de datos, enviar correos, etc.
  else:
      print('Se mete por el ELSE')
      # Si la solicitud no es POST, simplemente muestra el formulario vacío
      #formulario = AltaPaciente()
      return render(request, 'core/prueba.html', {'formulario': formulario, 'pacientes': x})

  return render(request, 'core/prueba.html', {'formulario': formulario})
#  return HttpResponse(template.render(context, request))

def mi_vista(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        formulario = AltaPaciente(request.POST)
        if formulario.is_valid():
            # Haz algo con los datos del formulario
            nombre = formulario.cleaned_data['nombre']
            apellido1 = formulario.cleaned_data['apellido1']
            dni = formulario.cleaned_data['dni']
            # Puedes realizar acciones como guardar en la base de datos, enviar correos, etc.
    else:
        # Si la solicitud no es POST, simplemente muestra el formulario vacío
        formulario = AltaPaciente()

    return render(request, 'core/prueba.html', {'formulario': formulario})
