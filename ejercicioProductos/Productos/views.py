from django.shortcuts import render

def renderIndex(request):
    seccion = "botones"

    if request.method == "POST":
        seccion = request.POST.get('seccion')
    data0 = {
        "p1":"Electronica",
        "p2":"Juguetes",
        "p3":"Ropa"
    }
    data1 = {
        "pr1":"Electronica",
        "pp1":"Mac",
        "pp2":"Iphone",
        "pp3":"Playstation"
    }
    data2 = {
        "pr1":"Jueguetes",
        "pp1":"Auto",
        "pp2":"Pelota de Futbol",
        "pp3":"Figura de Accion"
    }
    data3 = {
        "pr1":"Ropa",
        "pp1":"Pantalones",
        "pp2":"Chaqueta",
        "pp3":"Camisa"
    }
    data = {
        "seccion":seccion,
        "data0":data0,
        "data1":data1,
        "data2":data2,
        "data3":data3,
    }
    

    return render (request, 'templatesProductos/index.html',data)

def renderProductos(request):
    return render(request, 'templatesProductos/electronica.html')