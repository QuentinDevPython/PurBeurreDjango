from django import forms

class ProductForm(forms.Form):
    product = forms.CharField(
        label="Produit",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Produit',
                'class': 'form-control btn-xl'
            }
        )
    )

class SearchForm(forms.Form):
    product = forms.CharField(
        label="Produit",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Chercher',
                'class': 'd-flex',
                'id': 'form-navbar',
                'style': 'padding: 5px 5px 5px 5px; margin-top:3.5%; margin-right: 20px;',
            }
        )
    )