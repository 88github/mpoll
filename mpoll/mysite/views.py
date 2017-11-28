#coding=utf-8
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import RequestContext
from django.core.mail import EmailMessage
from django import forms
from mysite import models, forms
from django.shortcuts import redirect

# Create your views here.

def index(request):
    polls = models.Poll.objects.all()

    template = get_template('index.html')
    message = '测试'
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)

def poll(request, pollid):
    try:
        poll = models.Poll.objects.get(id=pollid)
    except:
        poll = None
    if poll is not None:
        pollitems = models.Pollitem.objects.filter(poll=poll).order_by('-vote')

    template = get_template('poll.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def vote(request, pollid, pollitemid):
    try :
        pollitem = models.Pollitem.objects.get(id=pollitemid)
    except:
        pollitem = None
    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()
    target_url = '/poll/' + pollid
    return redirect(target_url)

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感谢您的来信，我们会尽快处理您的宝贵意见。"
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']

            mail_body = u'''
            您的姓名：{}
            电子邮件：{}
            您的意见：{}
            '''.format(user_name, user_email, user_message)
            email = EmailMessage('来自【趣投网】网站的网友意见',
                                 mail_body,
                                 user_email,
                                 ['1712127445@qq.com'])
            email.send()
        else:
            message = "请检查您输入的信息是否正确"
    else:
        form = forms.ContactForm()

    template = get_template('contact.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)
