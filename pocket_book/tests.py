from django.test import TestCase

from pocket_book.models import PocketBook


class PocketBookTests(TestCase):

    def setUp(self) -> None:
        PocketBook.objects.create(author='test_author')

    def test_pocketbook_model_return(self):
        test_author = PocketBook.objects.get(author='test_author')
        self.assertEqual(test_author, 'test_author')
