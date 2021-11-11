from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    """Base Model"""
    ICONES_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-leaf', 'Folha')
    )

    criados = models.DateTimeField('Criado em', auto_now_add=True)
    modificados = models.DateTimeField('Modificado em', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    servico = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=255)
    icone = models.CharField('Ícone', max_length=50, choices=Base.ICONES_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Profissao(Base):
    profissao = models.CharField('Profissao', max_length=100)

    class Meta:
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'

    def __str__(self):
        return self.profissao


class Funcionarios(Base):
    nome = models.CharField('Nome', max_length=100)
    profissao = models.ForeignKey('core.Profissao', verbose_name='Profissão', on_delete=models.CASCADE)
    bio = models.TextField('Descrição', max_length=255)
    imagem = StdImageField('Imagem', upload_to='funcionarios', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Clientes(Base):
    nome = models.CharField('Nome', max_length=100)
    bio = models.TextField('Descrição', max_length=255)
    profissao = models.ForeignKey('core.Profissao', verbose_name='Profissão', on_delete=models.CASCADE)
    imagem = StdImageField('Imagem', upload_to='clientes', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Produtos(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=255)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
