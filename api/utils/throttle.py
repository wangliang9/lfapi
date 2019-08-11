from rest_framework.throttling import BaseThrottle,SimpleRateThrottle

# 基于IP做频率限制
class VisitThrottle(SimpleRateThrottle):
    scope = "Luffy"

    def get_cache_key(self, request, view):
        return self.get_ident(request)


# 基于用户做频率限制
class UserThrottle(SimpleRateThrottle):
    scope = "LuffyUser"

    def get_cache_key(self, request, view):
        return request.user.username