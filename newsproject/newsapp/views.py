from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from newsapp.forms import SignUpForm
from django.http import HttpResponseRedirect
import requests
import json
API_KEY='bc6991af90324b98a43143cd2bcfe85d'

# def search_view(request):
#     q=request.GET.get('q')
#     url = ('http://newsapi.org/v2/everything?'
#                            'q=[q]&'
#                            # 'sortBy=popularity&'
#                            # 'from=2022-07-20&'
#                           'language=en&'
#                          'apiKey=3ffb14b98bb3416da13501d87ac3b867')
#     news=requests.get(url).json()
#     articles=news['articles']
#     context={
#     'articles': articles,
#     }
#     return render(request,'testapp/search.html',context)

def search_view(request):
    if request.method=='GET':
        q=request.GET.get('q')
        url = ('http://newsapi.org/v2/everything?'
                               'q=[q]&'
                               # 'sortBy=popularity&'
                               # 'from=2022-07-20&'
                              'language=en&'
                             'apiKey=bc6991af90324b98a43143cd2bcfe85d')
        news=requests.get(url).json()
        articles=news['articles']
    context={
    'articles': articles,
    }
    return render(request,'testapp/search.html',context)

def home_page_view(request):
    return render(request,'testapp/home.html')

def news_view(request):
    return render(request,'testapp/news.html')

# @login_required
def world_view(request):
    url='https://newsapi.org/v2/top-headlines/sources?apiKey=bc6991af90324b98a43143cd2bcfe85d'
    news=requests.get(url).json()
    sources=news['sources']
    context={
    'sources': sources
    }
    return render(request,'testapp/world.html',context)

# @login_required
def science_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           # 'country=ca&'
                     'category=science&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/science.html',context)

# @login_required
def general_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=ca&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/general.html',context)

# @login_required
def india_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=in&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/india.html',context)

# @login_required
def us_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=us&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/us.html',context)

# @login_required
def gb_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=gb&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/gb.html',context)

# @login_required
def sg_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=sg&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/sg.html',context)

# @login_required
def za_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=za&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/za.html',context)

# @login_required
def ca_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=ca&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/ca.html',context)

# @login_required
def australia_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=au&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/au.html',context)

# @login_required
def my_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=my&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/my.html',context)

# @login_required
def nz_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           'country=nz&'
                     'category=general&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/nz.html',context)

# @login_required
def entertainment_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           # 'country=ca&'
                     'category=entertainment&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/entertainment.html',context)

# @login_required
def technology_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           # 'country=ca&'
                     'category=technology&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/technology.html',context)

# @login_required
def health_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           # 'country=ca&'
                     'category=health&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/health.html',context)

# @login_required
def sports_view(request):
    url = ('http://newsapi.org/v2/top-headlines?'
                           # 'country=ca&'
                     'category=sports&'
                          'language=en&'
                    'pageSize=100&'
                         'apiKey=bc6991af90324b98a43143cd2bcfe85d')
    news=requests.get(url).json()
    articles=news['articles']
    context={
    'articles': articles
    }
    return render(request,'testapp/sports.html',context)

def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
