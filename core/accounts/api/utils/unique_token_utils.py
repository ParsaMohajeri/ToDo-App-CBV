from rest_framework_simplejwt.tokens import RefreshToken
import uuid

def generate_unique_token(user):
    token = RefreshToken.for_user(user)
    token['jti'] = str(uuid.uuid4())
    return str(token.access_token)