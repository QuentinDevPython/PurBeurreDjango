import pytest

from django.test import Client
from user.models import User


class TestModelsUser:

    @pytest.mark.django_db
    def test_user_model(self):

        client = Client()

        # Normal user
        user = User.objects.create_user(
            email = "tototestmail@gmail.com",
            first_name = "toto",
            last_name="Foret",
            password="Aqwzsx123@"
        )

        expected_value = "tototestmail@gmail.com"
        
        assert str(user) == expected_value

        # Superuser
        superuser = User.objects.create_superuser(
            email = "superuser@gmail.com",
            password = "superuser"
        )
        
        expected_value = "superuser@gmail.com"
        
        assert str(superuser) == expected_value
