from django.urls import path
from .views import CreateNewUsersTemplateAPIView, PostFormAPIView


urlpatterns = [
    path('post_form/', CreateNewUsersTemplateAPIView.as_view(), name='create_new_user_template'),
    path('get_form/', PostFormAPIView.as_view(), name='get_form'),
    # path('get_form/<str:f_name1>&<str:f_name2>', PostFormAPIView.as_view(), name='post_template_name'),
]