from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse("<h1>HELLO</h1>")
def greet(sd,n):
	return HttpResponse(f"Welcome {n}")
def stdnt(request,m,a,c="vvit"):
	return HttpResponse(f"college name:{c}<br> student name:{m}<br> rollno:{a}")
def ky(request):
	return HttpResponse("<h1>Sanjana</h1>")
def inline(request):
	return HttpResponse("<h1><span style='color:orange'>Hello</span> I'm Sanjana</h1>")
def internal(request,x,y):
	return HttpResponse("<html><head><style>.name{color:orange}.roll{color:red}</style></head>"+f"<div><span class='name'>name:{x}</span><br><span class='roll'>roll no:{y}</span></div></html>")
def jsalert(self,a):
	return HttpResponse(f"<script>alert('hi welcome {a}')</script>")
def info(self,n,b,r,y):
	return HttpResponse(f"<html><head><script>alert('Name:{n}')</script></head><body><div><table border='1'><tr><th>name</th><td>{n}</td></tr><tr><th>rollno</th><td>{r}</td></tr><tr><th>branch</th><td>{b}</td></tr><tr><th>year</th><td>{y}</td></tr></table></div></body></html>")
def np(request):
	return render(request,'sample.html')
def pp(request,n,s,r):
	return render(request,'sample1.html',{'name':n,'salary':s,'role':r})
def dr(request):
	if request.method == 'POST':
		a=request.POST['rn']
		b=request.POST['sn']
		c=request.POST['sy']
		d=request.POST['sb']
		return render(request,'stdata.html',{'x':a,'y':b,'z':c,'w':d})

	return render(request,'std.html')
