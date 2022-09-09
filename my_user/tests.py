from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'test@super.com', 'test_user', '', 'test_password')
        self.assertEqual(super_user.email, 'test@super.com')
        self.assertEqual(super_user.username, 'test_user')
        self.assertEqual(super_user.first_name, '')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'test_user')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='test@super.com', username='test_user', first_name='',
                password='test_password', is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='test@super.com', username='test_user', first_name='',
                password='test_password', is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='test@super.com', username='test_user', first_name='',
                password='test_password', is_active=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', username='test_user', first_name='test_first_name',
                password='test_password', is_superuser=True)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'test@user.com', 'test_user', '', 'test_password')
        self.assertEqual(user.email, 'test@user.com')
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.first_name, '')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertEqual(str(user), 'test_user')

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', username='test_user', first_name='test_first_name', password='test_password')
