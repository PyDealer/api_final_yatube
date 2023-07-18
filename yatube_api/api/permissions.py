from rest_framework import permissions


class OwnerOnly(permissions.BasePermission):
    '''Ограничения для неавторов и неаутентифицированных пользователей'''

    def has_permission(self, request, view):
        '''Только аутентифицированный пользователь может делать небезопасные
        запросы'''
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        '''Только автор может изменять свои посты или комментарии.'''
        return (
            request.method in permissions.SAFE_METHODS
            or request.method == 'POST'
            or (request.method in ['PUT', 'PATCH', 'DELETE']
                and obj.author == request.user)
        )
