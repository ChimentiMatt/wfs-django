from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse, request
from .models import EventPosts


def BaseView(request):
    return render(request, 'myapp/landing.html')

def FooterView(request):
    return render(request, 'myapp/footer.html')

def AboutView(request):
    return render(request, 'myapp/about.html')

def MembersView(request):
    return render(request, 'myapp/members.html')

def SupportView(request):
    return render(request, 'myapp/support.html')
    
class EventsView(ListView):
    model = EventPosts
    template_name = 'myapp/events.html'

def ContactView(request):
    return render(request, 'myapp/contact.html')

def StayUpToDateView(request):
    return render(request, 'myapp/stayuptodate.html')

# heroku test push again

# def myview(request):
#     myinstances = MyModel.objects.all()
#     context = {
#         'myinstances': myinstances
#     }
#     return render(request, 'myapp/pageb.html', context)

# def mycreate(request):
#     myfield = request.POST['myfield']
#     mymodel = MyModel(myfield=myfield)
#     mymodel.save()
#     return HttpResponseRedirect(reverse('myapp:myview'))