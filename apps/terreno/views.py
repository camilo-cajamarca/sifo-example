
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from apps.terreno.models import Poligono

def index(request):
    obj = Poligono.objects.filter(usuario=request.user)


    for abc in Poligono.objects.raw('''select tp.id,
    (select count(distinct(tps.especie_id)) from terreno_punto_siembra tps where tps.poligono_id=tp.id) as especie,
    (select SUM(fd.valor)from terreno_siembra ts, financiacion_donacion fd, terreno_punto_siembra tps
    where ts.donacion_id=fd.id and ts.punto_siembra_id=tps.id and tps.poligono_id=tp.id) as valor_donacion,
    (select COUNT(fd.donador_id) from terreno_siembra ts, financiacion_donacion fd, terreno_punto_siembra tps
    where ts.donacion_id=fd.id and ts.punto_siembra_id=tps.id and tps.poligono_id=tp.id) as cant_donadores
    from terreno_poligono tp'''):
        obj_nombre = abc.nombre
        obj_coordenadas_puntos = abc.coordenadas_puntos
        obj_area = abc.area
        obj_perimetro= abc.perimetro
        obj_tipo_patron = abc.tipo_patron
        obj_municipio = abc.municipio
        obj_fecha=abc.fecha
        obj_especie=abc.especie
        obj_valor_donacion=abc.valor_donacion
        obj_cant_donadores=abc.cant_donadores

    context = { }
    if obj.exists():
        context = {
            "obj": obj,
            "obj_nombre": obj_nombre,
            "obj_coordenadas_puntos": obj_coordenadas_puntos,
            "obj_area": obj_area,
            "obj_perimetro": obj_perimetro,
            "obj_tipo_patron": obj_tipo_patron,
            "obj_municipio": obj_municipio,
            "obj_fecha": obj_fecha,
            "obj_especie": obj_especie,
            "obj_valor_donacion": obj_valor_donacion,
            "obj_cant_donadores": obj_cant_donadores
        }

    return render(request, "terreno/index.html", context)

def registro(request):
    return render(request, "terreno/registrar.html")