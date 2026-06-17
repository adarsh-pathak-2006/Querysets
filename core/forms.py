from django.forms import ModelForm
from .models import f1


class driver(ModelForm):
    class Meta:
        model=f1
        fields=['driver','team']
    

