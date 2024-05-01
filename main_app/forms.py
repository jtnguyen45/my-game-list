from django import forms
from django.forms import ModelForm
from .models import Note

class DateInput(forms.DateInput):
    input_type = 'date'

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'date', 'note',)
        widgets = {
            "date": DateInput()
        }