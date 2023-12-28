from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  if request.method == 'POST':
    if request.POST.get('title') and request.POST.get('content'):
      member = Member(firstname=request.POST.get('title'),lastname=request.POST.get('content'))
      member.save()
                
      return render(request, 'template.html')  
    else:
      return render(request,'template.html')
  return render(request, 'template.html')


def master(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('master.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


