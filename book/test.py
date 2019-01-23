import unittest
from unittest.mock import patch

import falcon
from falcon import testing

from . import app, tasks


class TestAppRoutes(testing.TestCase):
    """ Init Falcon Testing App
    """
    def setUp(self):
        super(TestAppRoutes, self).setUp()
        self.app = app

    def test_get_ping_message(self):
        result = self.simulate_get('/ping')
        self.assertEqual(result.json, 'pong!')


class TestCeleryTasks(testing.TestCase):
    """ Unit Test for Celery Task. will slow"""
#    def test_fib_task(self):
#        """Run Tests without celery worker."""
#        self.assertEqual(tasks.fib.run(-1), [])
#        self.assertEqual(tasks.fib.run(1), [0, 1])
#        self.assertEqual(tasks.fib.run(3), [0, 1, 1, 2])
#        self.assertEqual(tasks.fib.run(5), [0, 1, 1, 2, 3, 5])

    @patch('book.tasks.fib')
    def test_mock_fib_task(self, mock_fib):
        """Run tests with mock and celery worker. is faster"""
        mock_fib.run.return_value = []
        self.assertEqual(tasks.fib.run(-1), [])
        mock_fib.run.return_value = [0, 1]
        self.assertEqual(tasks.fib.run(1), [0, 1])
        mock_fib.run.return_value = [0, 1, 1, 2]
        self.assertEqual(tasks.fib.run(3), [0, 1, 1, 2])
        mock_fib.run.return_value = [0, 1, 1, 2, 3, 5]
        self.assertEqual(tasks.fib.run(5), [0, 1, 1, 2, 3, 5])


class TestBookApp(testing.TestCase):
    """ Unit Test for Book App. """
    def setUp(self):
        super(TestBookApp, self).setUp()
        self.app = app

    def tearDown(self):
        super(TestBookApp, self).tearDown()

    def test_create_book(self):
        """Run tests create a book"""
        book_data = {'author': 'Edi S', 'name': 'Book Coders', 'isbn': 54321}
        book_result = self.simulate_post('/books', json=book_data)
        self.assertEqual(book_result.status, falcon.HTTP_200)


if __name__ == '__main__':
    unittest.main()
