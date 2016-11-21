#-*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from  restaurants.models import Restaurant,Comment
from django.http import HttpResponse,HttpResponseRedirect
from  django.utils import timezone
from  django.template import RequestContext
from restaurants.forms import CommentForm
from django.contrib import auth
import datetime

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user= auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html',RequestContext(request,locals()))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')


def index(request):
    return render_to_response('index.html',RequestContext(request,locals()))


def menu(request,id):
    if id:
        restaurant=Restaurant.objects.get(id=id)
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")


def  menu456(request):
    if 'id' in request.GET  and request.GET['id']!='':
        restaurant= Restaurant.objects.get(id=request.GET['id'])
        a=request.GET['id']
        b=request.GET
        return render_to_response('menu.html',locals())
    else :
        return HttpResponseRedirect("/restaurants_list/")


def  menu123(request):
    restaurant = Restaurant.objects.get(id=1)
    #food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
    #food2={'name':'炒山豬肉','price':160,'comment':'好吃','is_spicy':True}

    #foods=[food1,food2]
    path=request.get_full_path()
    host=request.get_host()
    #foods.reverse()
    #from  django import template
    #t=get_template('menu123.html')
    #c=template.Context({'foods':foods})
    #return HttpResponse(t.render(c))
    #print foods
    #print locals()
    return render_to_response('menu.html',locals())


#字典轉換成元組
#food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
#items=food1.items()
#print items

def  list_restaurants(request):
    restaurants=Restaurant.objects.all()
    return render_to_response('restaurants_list.html', locals())

#menu(123)

def  meta(request):
    values=request.META.items()
    values.sort()
    html=[]
    for  k,v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k,v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def  welcome(request):
    if 'user_name' in  request.GET and  request.GET['user_name']!="":
        return  HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())


def  comment1(request,restaurant_id):
    errors=[]
    if  restaurant_id :
        r= Restaurant.objects.get(id=restaurant_id)
    else:
        return HttpResponseRedirect("/restaurants_list/")

    if request.POST:
        visitor=request.POST['visitor']
        content=request.POST['content']
        email=request.POST['email']
        date_time=timezone.localtime(timezone.now()) #擷取現在時間
        a=request.POST
        if any(not request.POST[k] for k in request.POST):
            #errors.append(' uuu* 有空白欄位,請不要留空 ,')
            errors+=[' uuu* 有空白欄位,請不要留空 ,']
        if '@' not in email:
            errors.append('aaa* email格式錯誤 , 請重新輸入!')
        if not errors:
            Comment.objects.create(
                visitor=visitor,
                email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
            visitor,email,content=("","","")

    f= CommentForm()
    return  render_to_response('comments.html',RequestContext(request,locals()))



def  comment(request,restaurant_id):

    if  restaurant_id :
        r= Restaurant.objects.get(id=restaurant_id)
    else:
        return HttpResponseRedirect("/restaurants_list/")

    if request.POST:
        f=CommentForm(request.POST)
        if f.is_valid():
            visitor=f.cleaned_data['visitor']
            content=f.cleaned_data['content']
            email=f.cleaned_data['email']
            date_time=datetime.datetime.now() #擷取現在時間

            c= Comment.objects.create(
                visitor=visitor,
                email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
            f=CommentForm(initial={'content':'我沒意見'})
    else:
        f = CommentForm(initial={'content': '我沒意見'})

    return  render_to_response('comments.html',RequestContext(request,locals()))

def set_c(request):
    response = HttpResponse('Set  your  lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse ('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies')

def use_session(request):
    request.session['lucky_number']=8
    if 'lucky_number' in request.session:
        lucky_number=request.session['lucky_number']
        response=HttpResponse('Your lucky_number is {0}'.format(lucky_number))
        del request.session['lucky_number']
        return response








        #errors=[]
#errors+=[u' uuu* 有空白欄位,請不要留空 ,'.encode('utf-8')]
#print ' uuu* 有空白欄位,請不要留空 ,'
#print (errors[0])