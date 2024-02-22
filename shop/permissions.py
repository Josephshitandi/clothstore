from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
        
class IsAdmin(BasePermission): 
    def has_permission(self, request, view):
        admin = request.user.user_type ==3
        return bool(
             super().has_permission(request, view)
             and (admin)
            )
    
class IsCustomerOrAdmin(BasePermission): 
    def has_permission(self, request, view):
        customer = request.user.user_type ==1
        admin = request.user.user_type ==2
        return bool(
             super().has_permission(request, view)
             and (admin or customer)
            )