from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

class TestPost(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='jungo', email='jungo@gmail.com', password='1234'
        )

    def test_get_posts_page(self):
        url = reverse('posts:post_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_create.html')

    def test_creating_posts(self):
        login = self.client.login(username = 'jungo', email='jungo@gmail.com', password='1234')
        self.assertTrue(login)

        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg", b"whatevercontents")
        response = self.client.post(
            url,
            {"image":image, "caption":'test test'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsede(response, "posts/base.html")
    
    def test_post_posts_create_not_login(self):
        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg", b"whatevercontents")
        response = self.client.post(
            url,
            {"image":image, "caption":'test test'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsede(response, "users/main.html")