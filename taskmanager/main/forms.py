from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateField, DateInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task','date_task','date_result','status']
        widgets = {
            
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Вкажіть назву завдання'
        }),
        'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Bкажіть опис завдання'
        }),
        'date_task': DateInput(attrs={
                'class': 'form-control',
                'placeholder':'Вкажіть дату завдання'
        }),
        'date_result': DateInput(attrs={
                'class': 'form-control',
                'placeholder':'Вкажіть дату виконання'
        }),
        'status': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Вкажіть статус завдання'
        }),
        
        }