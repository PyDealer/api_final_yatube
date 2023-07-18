from rest_framework import permissions


class OwnerOnly(permissions.BasePermission):
    '''Ограничения для неавторов и неаутентифицированных пользователей'''

    def has_permission(self, request, view):
        '''Только аутентифицированный пользователь может делать небезопасные
        запросы'''
        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        '''Только автор может изменять свои посты или комментарии.'''
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated
        elif request.method == 'PUT' or 'PATCH' or 'DELETE':
            return obj.author == request.user
