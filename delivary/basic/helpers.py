from rest_framework_simplejwt.tokens import AccessToken


def get_role_and_user_id(request):
    token = AccessToken(request.META.get("HTTP_AUTHORIZATION")
                        .split(" ")[1])
    return token['role'], token['user_id']
