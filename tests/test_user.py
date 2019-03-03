# import unittest
# from app.models import User

# class UserModelTest(unittest.TestCase):

#     def setUp(self):
#         self.new_user = User(id = 1, password = 'oppo', username = 'wecode', email="nshutioppo1987@gmail.com", bio = 'i have to learn more', profile_pic_path='/pictures/oppo.JPG')

#     # def test_instance(self):
#     #     self.assertTrue(isinstance(self.new_user, User))

#     def test_password_setter(self):
#         self.assertTrue(self.new_user.password_hash is not None)

#     def test_no_access_password(self):
#         with self.assertRaises(AttributeError):
#             self.new_user.password

#     def test_password_verification(self):
#         self.assertTrue(self.new_user.verify_password('oppo'))

# if __name__ == '__main__':
#     unittest.main()

import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))