from django.db import models

# Create your models here.
class Reader(models.Model):  
    full_name = models.TextField(max_length=100, unique=True, verbose_name='ФИО читателя')  
    birth_year = models.SmallIntegerField(verbose_name='Год рождения', null = True)  
    comment = models.TextField(max_length=100, unique=True, verbose_name='Комментарий', null = True)  

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
        ordering = ['full_name']
    
    def clean(self, *args, **kwargs):
        if self.full_name is None:
            raise ValidationError('Не указано ФИО читателя.')

        qs = Reader.objects.filter(full_name=self.full_name).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Схожий читатель уже заведен.')
        return super(Reader, self).clean(*args, **kwargs)
