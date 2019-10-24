from rest_framework.permissions import BasePermission


class OnlyStaffAndYou(BasePermission):
	message='You are not allowed to see this page only the staff and owner of this item can view it!'
	def has_object_permission(self, request, view, obj):

		if request.user == obj.added_by or request.user.is_staff :

			return True 

		return False