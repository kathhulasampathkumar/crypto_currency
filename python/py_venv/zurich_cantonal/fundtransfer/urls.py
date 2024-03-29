from django.urls import path, include
from fundtransfer import views

urlpatterns = [
    path('login_page', views.login_page, name='login_page'),            #default index page url      
    path('', views.home, name='home'),            #default index page url      
    path('getUserData', views.getUserData, name='getUserData'),            #default index page url      
    path('getCurrValues', views.getCurrValues, name='getCurrValues'),            #default index page url      
        
]
# handler404 ='certificate_module.views.error_404'
