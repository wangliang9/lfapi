from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from api import models
import uuid
from api.utils.throttle import VisitThrottle

class AuthView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [VisitThrottle,]
    def post(self,request,*args,**kwargs):
        """
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        ret = {'code':1000}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')

            obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['error'] = '用户名或密码错误'
            else:
                uid = str(uuid.uuid4())
                models.UserToken.objects.update_or_create(user=obj,defaults={'token':uid})
                ret['token'] = uid
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'

        return JsonResponse(ret)

