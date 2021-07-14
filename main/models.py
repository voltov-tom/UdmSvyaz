from django.db import models


class Elevators(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField('Адрес', max_length=255, unique=True)
    communication_type = models.CharField('Тип связи', max_length=255)
    station_type = models.CharField('Станция', max_length=255, default='нет данных')
    comment = models.TextField('Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.address}, обновлено: {self.updated_at}'

    class Meta:
        verbose_name = 'Лифт'
        verbose_name_plural = 'Лифты'


# save 'address' with uppercase into DB
# def save(self, *args, **kwargs):
#     self.address = self.address.upper()
#     return super(Elevators, self).save(*args, **kwargs)
