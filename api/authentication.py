from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokeAuthentication(BaseTokenAuth):
    keyword = "Bearer"
