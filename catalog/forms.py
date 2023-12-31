from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        # fields = "__all__"
        fields = ('name', 'description', 'category', 'price', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        list_prohib_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                             'радар']
        cleaned_data = self.cleaned_data['description']
        for item in list_prohib_words:
            if item in cleaned_data:
                raise forms.ValidationError('Использованы недопустимые слова')
        return cleaned_data

    def clean_name(self):
        list_prohib_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                             'радар']
        cleaned_data = self.cleaned_data['name']
        for item in list_prohib_words:
            if item in cleaned_data:
                raise forms.ValidationError('Использованы недопустимые слова')
        return cleaned_data
class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        # fields = "__all__"
        fields = ('version_number', 'version_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
