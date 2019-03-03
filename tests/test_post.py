import unittest
from app.models import Post

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_post= Post(id = 1, title = 'Python', post_content = 'Programming language that helps to build application', like = 3, dislike = 0)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

if __name__ == '__main__':
    unittest.main()