from django.urls import path
from . import views
app_name = 'sitesapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<str:site>/',views.SiteDetail.as_view(),name='detail'),
    path('<str:site>/<int:guestid>',views.SiteDetail.as_view(),name='detail'),
    path('<str:site>/confirm',views.SiteDetail.as_view(),name='detail'),
]