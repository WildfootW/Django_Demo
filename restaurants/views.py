#-*- coding: utf-8 -*-
from django.http import HttpResponse
#自動載入templates(failed)
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template
	
def menu(request):
    food1 = {
            'name' : '番茄炒蛋','price' : 60,'comment' : '好吃','is_spicy' : False}
    food2 = {
            'name' : '蒜泥白肉','price' : 100,'comment' : '人氣','is_spicy' : False}
    foods = [food1, food2]

    return render_to_response('menu.html', locals())