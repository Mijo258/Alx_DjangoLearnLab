from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # You can specify the model if you have a custom user model,
        # but the default User model works fine here.
        # You can also add more fields if needed.
        fields = UserCreationForm.Meta.fields + ('email',)