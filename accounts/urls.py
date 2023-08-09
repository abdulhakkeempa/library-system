from django.urls import path
from .views import createMember, updateMember, getMembers, deleteMember

urlpatterns = [
    path('/accounts/member', getMembers, name="library-member"),
    path('/accounts/member/create', createMember, name="library-member-create"),
    path('/accounts/member/<int:pk>/update', updateMember, name="library-member-update"),
    path('/accounts/member/<int:pk>/delete', deleteMember, name="library-member-delete"),
]
