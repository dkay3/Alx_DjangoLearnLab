from django import forms
from .models import Tag

class TagWidget(forms.CheckboxSelectMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = [(tag.id, tag.name) for tag in Tag.objects.all()]
