from django.conf.urls import url
from Basic import views
#TEMPLATE TAGGING
app_name='Basic'
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^UserLogin/$',views.user_login,name='Login'),

]