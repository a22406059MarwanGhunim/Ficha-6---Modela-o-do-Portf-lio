from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    Instituicao = models.CharField(max_length=100)
    duracao = models.IntegerField()
    creditos = models.IntegerField()
    semestre = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Disciplina = models.ManyToManyField('UC', blank=True)
    URL = models.URLField()

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True)
    URL = models.URLField()
    interesseNivel = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    ConceitosAplicados = models.CharField(max_length=250)
    imagem = models.ImageField(null=True, blank=True)
    githubRepo = models.URLField()
    video = models.URLField()
    dataRealizacao = models.DateField()
    NotaFinal = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )

    def __str__(self):
        return self.titulo


class UC(models.Model):
    course_code = models.IntegerField()                    
    codigo_legivel = models.CharField(max_length=30, unique=True)  
    nome = models.CharField(max_length=150)                
    semestre = models.CharField(max_length=30, blank=True) 
    ano = models.IntegerField(null=True, blank=True)   
    creditos = models.IntegerField()     
    descricao = models.TextField(blank=True)               
    programa = models.TextField(blank=True)                
    avaliacao = models.TextField(blank=True)               
    obrigatorio = models.BooleanField(default=True)        
    lingua = models.CharField(max_length=10, blank=True)   
    imagem = models.ImageField(null=True, blank=True)
    URL = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    nivel = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    URL = models.URLField()
    imagem = models.ImageField(null=True, blank=True)
    tecnologia = models.ManyToManyField(Tecnologia, blank=True)
    area = models.ManyToManyField(Competencia, blank=True)
    destaque = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=150)
    dataInicio = models.DateField()
    dataConclusao = models.DateField()
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class MakingOFF(models.Model):
    DescricaoDescisoes = models.CharField(max_length=250)
    Erros = models.CharField(max_length=150)
    Correcoes = models.CharField(max_length=150)
    Justificacao = models.CharField(max_length=250)
    usoAI = models.BooleanField()
    FotoCaderno = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.tipo