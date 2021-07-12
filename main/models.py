from django.db import models


class Elevators(models.Model):
    city = models.CharField('Город', max_length=20, default='ИЖЕВСК')
    street = models.CharField('Улица', max_length=50)
    house = models.CharField('Дом', max_length=4)
    entrance = models.CharField('Подъезд', max_length=2)
    elevator = models.CharField('Лифт №', max_length=50)
    communication_type = models.CharField('Тип связи', max_length=50)
    station_type = models.CharField('Станция', max_length=50, default='нет данных')
    comment = models.TextField('Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.street}, {self.house}-{self.entrance}, {self.comment}'


    class Meta:
        verbose_name = 'Лифт'
        verbose_name_plural = 'Лифты'

    def save(self, *args, **kwargs):
        self.city = self.city.upper()
        self.street = self.street.upper()
        self.house = self.house.upper()
        self.entrance = self.entrance.upper()
        self.elevator = self.elevator.upper()
        self.communication_type = self.communication_type.upper()
        self.station_type = self.station_type.upper()
        return super(Elevators, self).save(*args, **kwargs)
