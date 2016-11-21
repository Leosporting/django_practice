#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response


def  menu123(requests):
    food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
    food2={'name':'炒山豬肉','price':160,'comment':'好吃','is_spicy':True}

    foods=[food1,food2]
    #foods.reverse()

    #t=get_template('menu123.html')
    #c=template.Context({'foods':foods})
    #return HttpResponse(t.render(c))
    return render_to_response('menu.html',locals())


#字典轉換成元組
#food1={'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy':False}
#items=food1.items()
#print items

def test(requests):
    return render_to_response('test.html','')