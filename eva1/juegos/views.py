from django.shortcuts import render
def inicio(request):
    data={"foto1":"gta.jpg",
          "foto2":"red.jpg",
          "foto3":"bully.jpg",}
    return render(request,'inicio.html',data)

def gta(request):
    data={"juego":"gta",
          "Descripcion" : "Juego del año",
          "Valoracion":"10/10",
          "foto":"gta.jpg"}
    return render(request,'juego.html',data)

def red(request):
    data={"juego":"red dead redeption 2",
          "Descripcion" : "super bueno",
          "Valoracion":"10000/10",
          "foto":"red.jpg"}
    return render(request,'juego.html',data)

def bully(request):
    data={"juego":"bully",
          "Descripcion" : "muy bueno",
          "Valoracion":"9/10",
          "foto":"bully.jpg"}
    return render(request,'juego.html',data)