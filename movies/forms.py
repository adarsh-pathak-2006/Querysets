from django.forms import ModelForm
from movies.models import movies

class movieform(ModelForm):

    class Meta:
        model=movies
        fields=['name', 'description']