from rest_framework import permissions

class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):            #safe_method GET,LIST,DETAIL         #Unsafe_method PUT/PATCH,DELETE
        
        if request.method in permissions.SAFE_METHODS :
            return True
        return request.user==obj.user