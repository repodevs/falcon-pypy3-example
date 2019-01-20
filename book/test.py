import unittest

from falcon import testing

from .app import app


class TestAppRoutes(testing.TestCase):
    """ Init Falcon Testing App
    """
    def setUp(self):
        super(TestAppRoutes, self).setUp()
        self.app = app

    def test_get_ping_message(self):
        result = self.simulate_get('/ping')
        self.assertEqual(result.json, 'pong!')


if __name__ == '__main__':
    unittest.main()

