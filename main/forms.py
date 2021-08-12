from django.forms import ModelForm, TextInput, Textarea

from .models import Elevators


class ElevatorsForm(ModelForm):
    class Meta:
        model = Elevators
        fields = ['address', 'communication_type', 'station_type', 'comment']

        widgets = {
            "address": TextInput(attrs={
                'placeholder': 'Т.Барамзиной 9-1гр'
            }),
            "communication_type": TextInput(attrs={
                'placeholder': 'обь/есдкл/тм88/энергия'
            }),
            "station_type": TextInput(attrs={
                'placeholder': 'ШУЛК'
            }),
            "comment": Textarea(attrs={
                'placeholder': 'Пример: 10.11.12.13. Точка ростелеком Берша 54 второй подъезд(моноблок), воздушка с первого(Берша 54) на пятый подъезд(Берша 32), перемычки между подъездами по тех.этажу, ключи на союзной, 123'
            })
        }
