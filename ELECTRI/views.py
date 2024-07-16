from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from .models import Solicitud

def index_view(request):
    # Lógica de la vista index
    return render(request, 'index.html')

@csrf_protect
def solicitar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo_reparacion = request.POST.get('tipo-reparacion')
        marca = request.POST.get('marca')
        alta_eficiencia = request.POST.get('alta-eficiencia')
        descripcion_problema = request.POST.get('descripcion-problema')
        
        # Asegurarse de que alta_eficiencia tenga un valor antes de convertirlo a booleano
        if alta_eficiencia and alta_eficiencia.lower() == 'si':
            alta_eficiencia = True
        else:
            alta_eficiencia = False
        
        try:
            solicitud = Solicitud.objects.create(
                nombre=nombre,
                tipo_reparacion=tipo_reparacion,
                marca=marca,
                alta_eficiencia=alta_eficiencia,
                descripcion_problema=descripcion_problema
            )
            # Redirigir a una página de éxito o renderizar una página de éxito
            return render(request, 'success.html', {'solicitud': solicitud})
        
        except ValidationError as e:
            # Manejar los errores de validación
            return render(request, 'error.html', {'error': e})
    
    # Si el método de solicitud no es POST, renderizar el formulario inicial
    return render(request, 'solicitar.html')
