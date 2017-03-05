from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        restricted_actions = ("update", "partial_update", "delete",)
        if view.action in restricted_actions:
            return request.user == obj
        else:
            return True
