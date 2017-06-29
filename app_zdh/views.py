#coding:utf-8
from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
import os
import sys
from app_zdh.models import DbServersMysql,AdminUser



#def index(request):
#	return HttpResponse(u"数据库自动化系统")

def login(request):
	return render(request,'login.html')
def login2(request):
	user=request.GET.get('username')
	password=request.GET.get('password')
	passwd = AdminUser.objects.filter(username=user).all()[0].password
        if passwd == password:
                return render(request,'home.html')
        else:
                return render(request,'login.html')

	

def servers_list(request):
	servers = DbServersMysql.objects.order_by('host').values('host','port','username','is_delete','create_time')
	return render_to_response('servers_list.html',{'servers':servers})

def servers_fiter(request):
	name=request.GET.get('name')
	servers = DbServersMysql.objects.filter(host=name)
	return render_to_response('servers_list.html',{'servers':servers})

def add_server(request):
	return render(request,'add_server.html')

def add(request):
        if request.method == 'GET':
                host=request.GET.get('host')
                port=request.GET.get('port')
                username=request.GET.get('username')
                password=request.GET.get('password')
                tags=request.GET.get('tags')
                DbServersMysql.objects.create(host=host,port=port,username=username,password=password,tags=tags)
                return render(request,'add_success.html')

        else :
                return render(request,'add_server.html') 

def grant_user(request):
	return render(request,'grant_user.html')

def grant_user2(request):
	if request.method == 'GET':
                host=request.GET.get('host')
                port=request.GET.get('port')
                username=request.GET.get('username')
                password=request.GET.get('password')
                user=request.GET.get('user')
                passwd=request.GET.get('passwd')
                priv=request.GET.get('priv')
                objects=request.GET.get('objects')
                ranges=request.GET.get('range')
		sql="grant %s on %s to '%s'@'%s' identified by '%s';"%(priv,objects,user,ranges,passwd)
		execone="python /zdh/zdh/app_zdh/include/mysql_fun.py \\\"%s\\\" \\\"%s\\\" \\\"%s\\\" \\\"%s\\\" \\\"%s\\\""%(host,port,username,password,sql)
		os.system("/usr/bin/ansible \"%s\" -m shell -a \"%s\""%(host,execone))
		exectwo="python /zdh/zdh/app_zdh/include/mysql_fun.py \\\"%s\\\" \\\"%s\\\" \\\"%s\\\" \\\"%s\\\" \\\"flush privileges\\\""%(host,port,username,password)
		os.system("/usr/bin/ansible \"%s\" -m shell -a \"%s\""%(host,exectwo))
	else :
		return host

# Create your views here
