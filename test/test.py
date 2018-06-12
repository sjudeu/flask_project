from mdblog.cli import flask_app, init_db
import unittest

class MdblogTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        init_db(flask_app)

    def setUp(self):
        self.flask_app = flask_app.test_client()

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.flask_app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_user_login(self):
        response = self.login("admin", "admin")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login successful", response.data)

    def test_invalid_user_login(self):
        response = self.login("foo", "bar")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid credentials", response.data)

    ## HELPERS
    def login(self, username, password):
        return self.flask_app.post(
                "/admin/login/",
                data=dict(username=username, password=password),
                follow_redirects=True)
