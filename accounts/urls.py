from django.urls import path
from .views import createMember, updateMember, getMembers, deleteMember

urlpatterns = [
    path('/member', getMembers, name="library-member"),
    path('/member/create', createMember, name="library-member-create"),
    path('/member/<int:pk>/update', updateMember, name="library-member-update"),
    path('/member/<int:pk>/delete', deleteMember, name="library-member-delete"),
]
