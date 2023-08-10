from django.test import TestCase
from accounts.models import Member, User, Librarian
from datetime import datetime
# Create your tests here.

class LibrarianTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(email="test@library.com",full_name="Test", password="Test@123",dob=datetime(2023, 1, 1))
        super_user = User.objects.create_superuser(email="librarian@library.com", full_name="Librarian",dob=datetime(2023, 1, 15) ,password="Librar1an#", account_type="Librarian")
        self.librarian = Librarian.objects.create(account=super_user)
        self.member = Member.objects.create(account=user)

    def check_member_debt_balance(self):
        self.assertEqual(self.member.isDebtOutstanding(), False)
