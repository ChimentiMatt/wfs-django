from django.urls import path
from .views import BaseView, AboutView, FooterView, MembersView, SupportView, EventsView, ContactView, StayUpToDateView

 
app_name = 'myapp'
urlpatterns = [
    path('', BaseView, name='base'),
    path('footer/', FooterView, name="footer"),
    path('about/', AboutView, name='about'),
    path('members/', MembersView, name="members"),
    path('support/', SupportView, name="support"),
    path('events/', EventsView.as_view(), name="events"),
    path('contact/', ContactView, name="contact"),
    path('stayuptodate/', StayUpToDateView, name="stayuptodate"),

    # path('myview/', views.myview, name='myview'),
    # path('mycreate/', views.mycreate, name='mycreate')
]