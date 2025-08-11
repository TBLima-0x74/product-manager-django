import re
from urllib import request
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
import json
from .util import salvar_produtos, ler_produtos

print("http://127.0.0.1:8000/hello/Tiago")

def produtos(request):

    if request.method=="GET":
        return JsonResponse(ler_produtos(), safe=False)
    elif request.method=="POST":
        # Recebe JSON do frontend
        data = json.loads(request.body)
        
        produtos = ler_produtos()
        produtos.append(data)  # Adiciona o novo produto
        salvar_produtos(produtos)  # Salva no arquivo
        
        return JsonResponse({"mensagem": "Produto adicionado com sucesso!"})

def user(request, username):
    return HttpResponse(f"Viado:, {username}!")

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
        }
    )









