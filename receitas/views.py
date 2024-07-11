from django.shortcuts import render


# Create your views here.


def index(request):
    receitas = {
        1: "Sorvete",
        2: "Coxinha",
        3: "Pastel",
        4: "Bolo",
        5: "Torta",
        6: "Sushi",
    }
    dados = {"nome_da_receita": receitas}
    return render(request, "Index.html", dados)


def receita(request):
    return render(request, "Receita.html")
