from .models import User


class UserService:
    @staticmethod
    def create_user(username, email, phone, password):
        user = User.objects.create(username=username, email=email, phone=phone)
        user.set_password(password)
        user.save()
        return user
