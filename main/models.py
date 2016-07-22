from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name = _('Имя'))
    address = models.CharField(max_length=50, verbose_name = _('Адрес'))
    city = models.CharField(max_length=60, verbose_name = _('Город'))
    state_province = models.CharField(max_length=30, verbose_name = _('Регион'))
    country = models.CharField(max_length=50, verbose_name = _('Страна'))
    website = models.URLField(verbose_name = _('Веб-сайт'))
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Author(models.Model):
    salutation = models.CharField(max_length=10, verbose_name = _('Приветствие'))
    first_name = models.CharField(max_length=30, verbose_name = _('Имя'))
    last_name = models.CharField(max_length=40, verbose_name = _('Фамилия'))
    email = models.EmailField(blank=True, verbose_name = _('E-mail'))
    headshot = models.ImageField(upload_to='./tmp', verbose_name = _('Обложка'))
    
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    class Meta:
        ordering = ["last_name"]

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Название'))
    authors = models.ManyToManyField(Author, verbose_name=_('Автор'))
    publisher = models.ForeignKey(Publisher, verbose_name=_('Издательство'))
    publication_date = models.DateField(verbose_name=_('Дата публикации'))
    
    class Meta:
        ordering = ["title"]
