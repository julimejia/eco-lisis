from django.shortcuts import render
import metodos
import arduino as ar
from django.shortcuts import redirect


def login(request):
      targeta = ar.superLectura()
      if targeta == None :
        conexion = metodos.ConnectToMongo
        db = conexion.datos_clientes
        collection = db['datos_clientes']
        filter_ = {
                "$and": [
                    {"Codigo_tarjeta": {targeta}},
                ]
            }
        results = metodos.SearchDocuments(conexion,"datos_clientes","datos_clientes", filter_)
        resultsList = list(results)
        
        
        if resultsList > 0:
            return redirect('menu.html')
        else:
          return render(request, 'login.html')


def inicio(request):
    
    
    
    return render(request, 'menu.html')




def reclamar(request):
    
    
    
    return render(request, 'reclamar.html')