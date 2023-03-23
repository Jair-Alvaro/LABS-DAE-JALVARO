from django.http import HttpResponse

def index(request):
    return HttpResponse('Operaciones aritmeticas')

def suma(request,numero_1,numero_2):
    rpta = numero_1 + numero_2
    return HttpResponse('RESULTADO: ' + 'La suma de %s' % numero_1 + ' + %s' % numero_2 + ' = %s' % rpta) 

def resta(request,numero_1,numero_2):
    rpta = numero_1 - numero_2
    return HttpResponse('RESULTADO: ' + 'La resta de %s' % numero_1 + ' - %s' % numero_2 + ' = %s' % rpta) 

def multiplicacion(request,numero_1,numero_2):
    rpta = numero_1 * numero_2
    return HttpResponse('RESULTADO: ' + 'La multiplicación de %s' % numero_1 + ' x %s' % numero_2 + ' = %s' % rpta) 