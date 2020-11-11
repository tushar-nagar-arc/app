from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.
class BlogTests(TestCase):

    def setUp(self):
        self.user=get_user_model().objects.create(username='testuser',email='tushar@gmail.com',password='secret')
        self.post = Post.objects.create(title="A good title",author=self.user,body="Nice body content")
    def test_string_representation(self):
        post=Post(title='A sample title')
        self.assertEqual(str(post),post.title)
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','Nice body content')
    def test_post_list_view(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateUsed(response,'home.html')
    def test_post_detail_view(self):
        response=self.client.get('/post/1/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateUsed(response,'detail.html')
