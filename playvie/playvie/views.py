from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.http import JsonResponse

# ERROR HANDLING
def handler404(request, exception=None):
    return JsonResponse({'error': 'Resource Not Found (404)'}, status=404)

#AUTHENTICATION
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username

        return token
