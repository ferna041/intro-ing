from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "green"

urlpatterns = [
    path("",views.home, name="home.html"),
        path("Basica_Matematicas_primero/",views.m1, name="Basica_Matematicas_primero"),
    path("Basica_Lenguaje_primero/",views.l1, name="Basica_Lenguaje_primero"),
    path("Basica_Ciencias_primero/",views.c1, name="Basica_Ciencias_primero"),
    path("Basica_Historia_primero/",views.h1, name="Basica_Historia_primero"),
    path("Basica_Otros_primero/",views.o1, name="Basica_Otros_primero"),
    path("Basica_Ingles_primero/",views.i1, name="Basica_Ingles_primero"),
    path("Basica_Matematicas_segundo/",views.m2, name="Basica_Matematicas_segundo"),
    path("Basica_Lenguaje_segundo/",views.l2, name="Basica_Lenguaje_segundo"),
    path("Basica_Ciencias_segundo/",views.c2, name="Basica_Ciencias_segundo"),
    path("Basica_Historia_segundo/",views.h2, name="Basica_Historia_segundo"),
    path("Basica_Otros_segundo/",views.o2, name="Basica_Otros_segundo"),
    path("Basica_Ingles_segundo/",views.i2, name="Basica_Ingles_segundo"),
    path("Basica_Matematicas_tercero/",views.m3, name="Basica_Matematicas_tercero"),
    path("Basica_Lenguaje_tercero/",views.l3, name="Basica_Lenguaje_tercero"),
    path("Basica_Ciencias_tercero/",views.c3, name="Basica_Ciencias_tercero"),
    path("Basica_Historia_tercero/",views.h3, name="Basica_Historia_tercero"),
    path("Basica_Otros_tercero/",views.o3, name="Basica_Otros_tercero"),
    path("Basica_Ingles_tercero/",views.i3, name="Basica_Ingles_tercero"),
    path("Basica_Matematicas_cuarto/",views.m4, name="Basica_Matematicas_cuarto"),
    path("Basica_Lenguaje_cuarto/",views.l4, name="Basica_Lenguaje_cuarto"),
    path("Basica_Ciencias_cuarto/",views.c4, name="Basica_Ciencias_cuarto"),
    path("Basica_Historia_cuarto/",views.h4, name="Basica_Historia_cuarto"),
    path("Basica_Otros_cuarto/",views.o4, name="Basica_Otros_cuarto"),
    path("Basica_Ingles_cuarto/",views.i4, name="Basica_Ingles_cuarto"),
    path("Basica_Matematicas_quinto/",views.m5, name="Basica_Matematicas_quinto"),
    path("Basica_Lenguaje_quinto/",views.l5, name="Basica_Lenguaje_quinto"),
    path("Basica_Ciencias_quinto/",views.c5, name="Basica_Ciencias_quinto"),
    path("Basica_Historia_quinto/",views.h5, name="Basica_Historia_quinto"),
    path("Basica_Otros_quinto/",views.o5, name="Basica_Otros_quinto"),
    path("Basica_Ingles_quinto/",views.i5, name="Basica_Ingles_quinto"),
    path("Basica_Matematicas_sexto/",views.m6, name="Basica_Matematicas_sexto"),
    path("Basica_Lenguaje_sexto/",views.l6, name="Basica_Lenguaje_sexto"),
    path("Basica_Ciencias_sexto/",views.c6, name="Basica_Ciencias_sexto"),
    path("Basica_Historia_sexto/",views.h6, name="Basica_Historia_sexto"),
    path("Basica_Otros_sexto/",views.o6, name="Basica_Otros_sexto"),
    path("Basica_Ingles_sexto/",views.i6, name="Basica_Ingles_sexto"),
    path("Basica_Matematicas_septimo/",views.m7, name="Basica_Matematicas_septimo"),
    path("Basica_Lenguaje_septimo/",views.l7, name="Basica_Lenguaje_septimo"),
    path("Basica_Ciencias_septimo/",views.c7, name="Basica_Ciencias_septimo"),
    path("Basica_Historia_septimo/",views.h7, name="Basica_Historia_septimo"),
    path("Basica_Otros_septimo/",views.o7, name="Basica_Otros_septimo"),
    path("Basica_Ingles_septimo/",views.i7, name="Basica_Ingles_septimo"),
    path("Basica_Matematicas_octavo/",views.m8, name="Basica_Matematicas_octavo"),
    path("Basica_Lenguaje_octavo/",views.l8, name="Basica_Lenguaje_octavo"),
    path("Basica_Ciencias_octavo/",views.c8, name="Basica_Ciencias_octavo"),
    path("Basica_Historia_octavo/",views.h8, name="Basica_Historia_octavo"),
    path("Basica_Otros_octavo/",views.o8, name="Basica_Otros_octavo"),
    path("Basica_Ingles_octavo/",views.i8, name="Basica_Ingles_octavo"),
    path("media_biologia_primero", views.bI, name="media_biologia_primero"),
    path("media_fisica_primero", views.fI, name="media_fisica_primero"),
    path("media_historia_primero", views.hI, name="media_historia_primero"),
    path("media_ingles_primero", views.iI, name="media_ingles_primero"),
    path("media_lenguaje_primero", views.lI, name="media_lenguaje_primero"),
    path("media_matematicas_primero", views.mI, name="media_matematicas_primero"),
    path("media_otros_primero", views.oI, name="media_otros_primero"),
    path("media_quimica_primero", views.qI, name="media_quimica_primero"),
    path("media_biologia_segundo", views.bII, name="media_biologia_segundo"),
    path("media_fisica_segundo", views.fII, name="media_fisica_segundo"),
    path("media_historia_segundo", views.hII, name="media_historia_segundo"),
    path("media_ingles_segundo", views.iII, name="media_ingles_segundo"),
    path("media_lenguaje_segundo", views.lII, name="media_lenguaje_segundo"),
    path("media_matematicas_segundo", views.mII, name="media_matematicas_segundo"),
    path("media_otros_segundo", views.oII, name="media_otros_segundo"),
    path("media_quimica_segundo", views.qII, name="media_quimica_segundo"),
    path("media_biologia_tercero", views.bIII, name="media_biologia_tercero"),
    path("media_fisica_tercero", views.fIII, name="media_fisica_tercero"),
    path("media_historia_tercero", views.hIII, name="media_historia_tercero"),
    path("media_ingles_tercero", views.iIII, name="media_ingles_tercero"),
    path("media_lenguaje_tercero", views.lIII, name="media_lenguaje_tercero"),
    path("media_matematicas_tercero", views.mIII, name="media_matematicas_tercero"),
    path("media_otros_tercero", views.oIII, name="media_otros_tercero"),
    path("media_quimica_tercero", views.qIII, name="media_quimica_tercero"),
    path("media_quimicaA_tercero", views.qaIII, name="media_quimicaA_tercero"),
    path("media_biologiaA_tercero", views.baIII, name="media_biologiaA_tercero"),
    path("media_fisicaA_tercero", views.faIII, name="media_fisicaA_tercero"),
    path("media_matematicasA_tercero", views.maIII, name="media_matematicasA_tercero"),

    path("media_biologia_cuarto", views.bIV, name="media_biologia_cuarto"),
    path("media_fisica_cuarto", views.fIV, name="media_fisica_cuarto"),
    path("media_historia_cuarto", views.hIV, name="media_historia_cuarto"),
    path("media_ingles_cuarto", views.iIV, name="media_ingles_cuarto"),
    path("media_lenguaje_cuarto", views.lIV, name="media_lenguaje_cuarto"),
    path("media_matematicas_cuarto", views.mIV, name="media_matematicas_cuarto"),
    path("media_otros_cuarto", views.oIV, name="media_otros_cuarto"),
    path("media_quimica_cuarto", views.qIV, name="media_quimica_cuarto"),
    path("media_quimicaA_cuarto", views.qaIV, name="media_quimicaA_cuarto"),
    path("media_biologiaA_cuarto", views.baIV, name="media_biologiaA_cuarto"),
    path("media_fisicaA_cuarto", views.faIV, name="media_fisicaA_cuarto"),
    path("media_matematicasA_cuarto", views.maIV, name="media_matematicasA_cuarto"),
    path("media_matematicasA_cuarto", views.maIV, name="media_matematicasA_cuarto"),

    path("pdt_biologia", views.b, name="pdt_biologia"),
    path("pdt_fisica", views.f, name="pdt_fisica"),
    path("pdt_historia", views.h, name="pdt_historia"),
    path("pdt_lenguaje", views.l, name="pdt_lenguaje"),
    path("pdt_matematicas", views.m, name="pdt_matematicas"),
    path("pdt_otros", views.o, name="pdt_otros"),
    path("pdt_quimica", views.q, name="pdt_quimica"),
    path("pdt_quimicaA", views.qa, name="pdt_quimicaA"),
    path("pdt_biologiaA", views.ba, name="pdt_biologiaA"),
    path("pdt_fisicaA", views.fa, name="pdt_fisicaA"),
    path("pdt_matematicasA", views.ma, name="pdt_matematicasA"),
    
    path('post/', views.create_post, name= 'create_post'),
]


