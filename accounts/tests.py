from django.test import TestCase
from accounts.models import Member, User
# Create your tests here.

class LibrarianTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(email="test@library.com",full_name="Test", password="Test@123")
        self.member = Member.objects.create(account=user)

    def check_member_debt_balance(self):
        self.member
        self.assertEqual(self.member.isDebtOutstanding(), False)
