from django.contrib.auth.forms import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name'
        ]