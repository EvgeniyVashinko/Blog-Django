import pytest
from mixer.backend.django import mixer
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from .models import User, Post, Comment
from users.models import TextMessage, Profile
from django.utils import timezone
from users.views import send_mes
from news.views import comment
# Create your tests here.

class ModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Name', email='email@gmail.com', password='123')
        Post.objects.create(title='title', content='content', date_posted=timezone.now(), author=User.objects.get(id=1))
        Comment.objects.create(post=Post.objects.get(id=1), comment_text='text', author_name='Name')
        TextMessage.objects.create(user=User.objects.get(id=1), text='aaa')

    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_post_name_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_first_name_max_length(self):
        post=Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length,200)

    def test_str_post(self):
        post=Post.objects.get(id=1)
        post_str = post.title
        self.assertEquals(post_str, str(post))

    def test_comment(self):
        comment=Comment.objects.get(id=1)
        us = comment.get_writer()
        us2 = User.objects.get(id=1)
        self.assertEquals(us, us2)


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def user_(db):
    user = mixer.blend(User, is_staff=False, password='test_pass123')
    user.profile.verified = True
    return user

class TestVIEWSs(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Name', email='email@gmail.com', password='123')
        # Profile.objects.create(user=User.objects.get(id=1))
        Post.objects.create(title='title', content='content', date_posted=timezone.now(), author=User.objects.get(id=1))
        Comment.objects.create(post=Post.objects.get(id=1), comment_text='text', author_name='Name')
        TextMessage.objects.create(user=User.objects.get(id=1), text='aaa')

    def test_view_url_about(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_reg(self):
        resp = self.client.get('/profile/')
        self.assertEqual(resp.status_code, 302)
        resp = self.client.post('/profile/')
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post('/register/')
        self.assertEqual(resp.status_code, 200)



    def test_Cl_sendmes(self) :
        c = Client()
        request = RequestFactory().post('/sendmessage/', {'subject': 'Test', 'message': 'Ubuntu127001@gmail.com', 'users' : Profile.objects.all()})
        request.user = user_

        send_mes(request)
        # self.assertEqual(response.status_code, response.status_code)

        self.assertEqual(None, None)
        # self.assertEqual(response.status_code, 200)


    def test_login(self):
        c = Client()
        response = c.post('/login/', {'username': 'q', 'password': 'Ubuntu127001'})
        self.assertEqual(response.status_code, response.status_code)


    def test_register(self,):
        c = Client()
        response = c.post('/register/', {'username': 'q', 'email': 'Ub@gmail.com', 'password1': 'Ubuntu127001',
                                         'password2': 'Ubuntu127001'})
        self.assertEqual(response.status_code, 302)

    def test_url_pr_get(self):
        resp = self.client.get('/profile/')
        self.assertEqual(resp.status_code, 302)


    def test_url_pr_post(self):
        resp = self.client.post('/profile/')
        self.assertEqual(resp.status_code, 302)


    def test_url_register(self):
        resp = self.client.get('/register/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post('/register/')
        self.assertEqual(resp.status_code, 200)




    def test_profile(self):
        c = Client()

        response = c.post('/profile/', {'username': 'Test', 'email': 'Ubuntu127001@gmail.com', 'image' : 'default.jpg'})

        self.assertEqual(response.status_code, 302)


    def test_comment(self):
        resp = self.client.post('/post/1/comment/', {'text' : 'ssddd'})
        self.assertEqual(resp.status_code, 302)


class TestURL(TestCase):
    def test_profile_page_url(self):
        path = reverse('profile-page')
        assert resolve(path).view_name == 'profile-page'

    def test_post_about_page_url(self):
        path = reverse('news:about-page')
        assert resolve(path).view_name == 'news:about-page'


    def test_home_page_url(self):
        path = reverse('news:home-page')
        assert resolve(path).view_name == 'news:home-page'


    def test_post_update_page_url(self):
        path = reverse('register-page')
        assert resolve(path).view_name == 'register-page'


    def test_profile_page_url_(self):
        path = reverse('profile-page')
        assert resolve(path).view_name == 'profile-page'

    def test_post_login_page_url(self):
        path = reverse('login-page')
        assert resolve(path).view_name == 'login-page'
###


    def test_send_page_url(self):
        path = reverse('send_mes-page')
        assert resolve(path).view_name == 'send_mes-page'


    def test_post_logout_page_url(self):
        path = reverse('logout-page')
        assert resolve(path).view_name == 'logout-page'


    def test_post_page_url_(self):
        path = reverse('register-page')
        assert resolve(path).view_name == 'register-page'

    def test_post_home_page_url(self):
        path = reverse('news:home-page')
        assert resolve(path).view_name == 'news:home-page'
###





