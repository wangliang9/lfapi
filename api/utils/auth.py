from rest_framework import exceptions
from api import models
from rest_framework.authentication import BaseAuthentication

class FirstAuthtication(BaseAuthentication):
    def authenticate(self, request):
        pass

    def authenticate_header(self, request):
        pass

class Authtication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # 在rest framework内部会将整个两个字段赋值给request,以供后续操作使用
        return (token_obj.user,token_obj)

    def authenticate_header(self, request):
        return 'Basic realm="api"'