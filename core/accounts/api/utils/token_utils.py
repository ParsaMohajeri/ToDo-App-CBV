from rest_framework_simplejwt.tokens import RefreshToken

def generate_activation_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)