from django.urls import path
from blog import views

urlpatterns = [
    # path('',views.signup,name='base'),    
    path('',views.index,name='index'),    
    # path('postblog',views.postblog,name='postblog'),    
    # path('signup/',views.signup,name='signup'),    
    path('signin/',views.signin,name='signin'),    
]