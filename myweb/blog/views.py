from blog.models import Blog
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
	blog_list = Blog.objects.all()
	return render_to_response('index.html',{'blogs':blog_list},context_instance=RequestContext(request))
	
#登录处理	
def  login(request):
	blog_list = Blog.objects.all()
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	users_ = [username]
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user) # 验证登录
		response = HttpResponseRedirect('/login_ok/')
		request.session['username'] = users_
		return response
	else:
		return render_to_response('index.html',{'error':'username or passworderror!','blogs':blog_list},context_instance=RequestContext(request))

		
		
# 登录成功
@login_required
def login_ok(request):
	blog_list = Blog.objects.all()
	#username = request.COOKIES.get('username','') # 读取浏览器 cookie
	username = request.session.get('username', '') # 读取用户 session
	user = username[0]
	return render_to_response('login_ok.html',{'user': user, 'blog_list':blog_list})
	
# 退出登录
@login_required
def logout(request):
	response = HttpResponseRedirect('/index/') # 返回首页
	#response.delete_cookie('username') # 清理 cookie 里保存 username
	del request.session['username'] # 清理用户 session
	return response

	
# 学生表
def student(request):
	book = Book.objects.all()
	student = {
				'jack': [22, 'boy', 'Programmer'],
				'alen': [27, 'boy', 'Designer'],
				'una': [23, 'girl', 'Tester'],
				'Brant': [23, 'girl', 'Tester'],
				'David': [23, 'boy', 'Tester']
			}
	return render_to_response('student.html', {'student_list': student,'book_list':book})


def  page(request):
	file_list = Book.objects.all()
	paginator = Paginator(file_list, 2) # Show 2 contacts per page
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render_to_response('book.html', {'pages': contacts})
	
	
# 上传文件页面
def upload(request):
	return render_to_response('upload.html')
	
# 执行文件上传
def upload_save(request):
	filename = request.POST.get('filename', '') # 获得表单文件说明
	fileing = request.FILES.get('fileing', '') # 获得文件
	if filename == '' or fileing == '':
		error = '文件与文件描述不能为空'
		#return render_to_response('upload.html', {'error': error},context_instance=RequestContext(request))
		return render_to_response('upload.html', {'error': error})
	else:
		upload = File() # 将文件名和文件路径存放到 File 表中
		upload.filename = filename
		upload.fileway = fileing
		upload.save()
		#return render_to_response('upload.html',{'upload_success':'upload successfully'},context_instance=RequestContext(request))
		return render_to_response('upload.html',{'upload_success':'upload successfully'})







