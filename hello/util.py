import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PRODUTOS = os.path.join(BASE_DIR, "produtos.json")
def ler_produtos():
    if os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
         return json.load(f)
    return []

def salvar_produtos(lista_produtos):
    if os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
           json.dump(lista_produtos, f, indent=4, ensure_ascii=False)