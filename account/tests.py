from django.test import TestCase
from account import models as amod
from datetime import datetime
# Create your tests here.


class AccountTests(TestCase):
    fixtures = ['account.yaml']

    # @classmethod
    # def setUpTestData(cls):
    #     cls.foo = Foo.objects.create(bar='Test')

    def test_user_get(self):
        u1 = amod.User.objects.get(id=1)
        self.assertEqual(u1.username, 'homer', msg="Username should have been homer")
        self.assertTrue(u1.check_password('marge'), msg="WRONG PASSWORD!")       
    def test_user_create(self):
        u1 = amod.User()
        u1.username = 'luke'
        u1.birthdate = datetime(2008, 6, 24)
        u1.save()
        u2 = amod.User.objects.get(id= u1.pk)

        self.assertEqual(u1.username, u2.username, msg="Username didn't match")

    def test_change_password(self):
        u1 = amod.User.objects.get(pk=1)
        u1.set_password('newpassword')
        self.assertTrue(u1.check_password('newpassword'), msg="Username didn't match")


    def test_login(self):
        #send login data
        response = self.client.post('/account/login', self.credentials, follow=False)
        self.assertTrue(response.context['user'].is_authenticated)
   
    def setUp(self):
       self.credentials = {
           'username': 'homer',
           'password': 'marge'
       }
       
        