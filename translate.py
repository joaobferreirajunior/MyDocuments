from googletrans import Translator
import json

translator = Translator()
with open("translateconf.json", encoding='utf-8') as file:
    data = json.load(file)

def menu():
    language = data["language"]["comment"]
    print("#" * 50)
    print("#" * 20, "Tradutor", "#" * 20)
    print("#" * 50)

    for i in language:
       print(" " * 15, i)

menu()
item = input("Entre com o codigo da linguagem pra tradução:")

while item not in data["language"]["itens"]:
    print("Opção invalida!")
    print("Escolha uma outra opção")
    menu()
    item = input("Entre com o codigo da linguagem para tradução:")

lang = data["language"][item]
frase = input("Entre com o texto para tradução:")

traducao = translator.translate(frase, dest=lang)
print("Palavra traduzida ->", traducao.text)
