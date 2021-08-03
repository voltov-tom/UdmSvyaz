from django.db import models


class Elevators(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField('Адрес', max_length=255, unique=True)
    communication_type = models.CharField('Тип связи', max_length=255, default='нет данных')
    station_type = models.CharField('Станция', max_length=255, default='нет данных')
    comment = models.TextField('Комментарий', default='нет данных')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.address}, комментарий: {self.comment}, {self.updated_at}'

    def get_absolute_url(self):
        return f'/main/{self.id}'

    class Meta:
        verbose_name = 'Лифт'
        verbose_name_plural = 'Лифты'

    def save(self, *args, **kwargs):
        self.validate_unique()
        self.address = self.address.upper()  # save 'address' uppercase into DB
        super(Elevators, self).save(*args, **kwargs)
