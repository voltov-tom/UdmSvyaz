from django.forms import ModelForm, TextInput, Textarea

from .models import Elevators


class ElevatorsForm(ModelForm):
    class Meta:
        model = Elevators
        fields = ['city', 'street', 'house', 'entrance', 'elevator',
                  'communication_type', 'station_type', 'comment']

        widgets = {
            "city": TextInput(),
            "street": TextInput(attrs={
                'placeholder': 'Союзная'
            }),
            "house": TextInput(attrs={
                'placeholder': '6б'
            }),
            "entrance": TextInput(attrs={
                'placeholder': '1'
            }),
            "elevator": TextInput(attrs={
                'placeholder': 'груз/пасс'
            }),
            "communication_type": TextInput(attrs={
                'placeholder': 'обь/есдкл/тм88/энергия'
            }),
            "station_type": TextInput(attrs={
                'placeholder': 'ул'
            }),
            "comment": Textarea(attrs={
                'placeholder': 'Пример: 10.11.12.13. Точка ростелеком Берша 54 второй подъезд(моноблок), воздушка с первого(Берша 54) на пятый подъезд(Берша 32), перемычки между подъездами по тех.этажу, ключи на союзной, 123'
            })
        }


class ElevatorsFormFind(ModelForm):
    class Meta:
        model = Elevators
        fields = ['city', 'street', 'house']

        widgets = {
            "city": TextInput(),
            "street": TextInput(attrs={
                'placeholder': 'Союзная'
            }),
            "house": TextInput(attrs={
                'placeholder': '6б'
            })
        }
