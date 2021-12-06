from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid


class Post(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(max_length=20)
    grados=(
        ('1', 'Primero basico'),
        ('2', 'Segundo basico'),
        ('3', 'Tercero basico'),
        ('4', 'Cuarto basico'),
        ('5', 'Quinto basico'),
        ('6', 'Sexto basico'),
        ('7', 'Septimo basico'),
        ('8', 'Octavo basico'),
        ('I', 'Primero medio'),
        ('II', 'Segundo medio'),
        ('III', 'Tercero medio'),
        ('IV', 'Cuarto medio'),
        ("PDT", "PDT"),
    )
    grado = models.CharField(max_length=12, choices=grados)
    asignaturas_Basica= (
        ('N', 'No'),
        ('M', 'Matemáticas '),
        ('C', 'Ciencias Naturales '),
        ('L', 'Lenguaje y comunicación '),
        ('H', 'Historia, Geografía y Ciencias Sociales '),
        ('I', 'Ingles'),
        ('O', 'Otros'),
    )
    asignatura_Basica= models.CharField(max_length=1, choices= asignaturas_Basica,default='N')
    asignaturas_Media= (
        ('N', 'No'),
        ('Z', 'Matemáticas '),
        ('C', 'Matemáticas avanzadas'),
        ('L', 'Lenguaje y comunicación '),
        ('H', 'Historia, Geografía y Ciencias Sociales '),
        ('F', 'Física '),
        ('E', 'Física avanzada '),
        ('Q', 'Química '),
        ('S', 'Química avanzada'),
        ('B', 'Biología '),
        ('A', 'Biología avanzada'),
        ('I', 'Ingles'),
        ('O', 'Otros'),
    )
    asignatura_Media= models.CharField(max_length=1, choices=asignaturas_Media, default='N' )

    description = models.TextField()
    image = models.ImageField(
        upload_to="images/",
        default="images/Fondo.png"
    )
    published = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="green_post"
    )

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.description


class Comment(models.Model):
    text= models.TextField()
    author= models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="green_comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="green_comments"
    )