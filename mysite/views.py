#-*- coding: utf-8 -*-
from django.http import HttpResponse
#自動載入templates(failed)
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template

def here(request):
	return HttpResponse('Mother fucker?媽的法克？')

#參數為字串,記得轉型
def math(request, a, b):
	#s = int(a) + int(b)
	#return HttpResponse(str(s))
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	#這是把view logic(Template)混到business logic(views.py負責控制器)的情況
#	html = """
#		<html>
#			sum={s}<br>
#			dif={d}<br>
#			pro={p}<br>
#			quo={q}
#		</html>
#	""".format(s=s,d=d,p=p,q=q)
#	return HttpResponse(html)
	
	#使用template
#	t = template.Template('''
#<html>
#	sum = {{s}}<br>
#	dif = {{d}}<br>
#	pro = {{p}}<br>
#	quo = {{q}}
#</html>''')
#	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
#	return HttpResponse(t.render(c))

	#template分離
		#手動載入templates
#	with open('templates/math.html','r') as reader:
#		t = template.Template(reader.read())
#	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
#	return HttpResponse(t.render(c))

		#自動載入(failed)	
#	t = get_template('math.html')
#	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
#	return HttpResponse(t.render(c))

		#get_template 
	return render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q})
