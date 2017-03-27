from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        restricted_actions = ("update", "partial_update", "delete",)
        return view.action in restricted_actions and request.user == obj
