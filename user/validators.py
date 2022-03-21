from django.core.exceptions import ValidationError


class ContainsLetterLowerValidator:
    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre minuscule', code='password_no_lower_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre minuscule.'

class ContainsLetterUpperValidator:
    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre majuscule', code='password_no_upper_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule.'

class ContainsDigitValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir un chiffre', code='password_no_digit')
        
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un chiffre.'
    
sc_list = list('[@_!#$%^&*()<>?/\|}{~:]')

class ContainsSpecialCharacterValidator:
    def validate(self, password, user=None):
        if not any(char in sc_list for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir un caractère spécial', code='password_no_special_character')
        
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un caractère spécial.'
