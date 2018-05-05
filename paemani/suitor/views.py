from django.http import HttpResponse,HttpResponseRedirect
from  suitor.models  import Suitor,Aprnc
from django.shortcuts import get_object_or_404,render
from .forms import SuitorForm,AprncForm
from .choices import *
from django.contrib import messages
from django.urls import reverse

def homepage(request):
    suitors = Suitor.objects.all()
    return render(request, 'homepage.html', {'suitors' : suitors})


def create_suitor(request):
    if request.method == 'POST':
        s_form=SuitorForm(request.POST or None)
        a_form=AprncForm(request.POST or None)
        if s_form.is_valid() and a_form.is_valid():
            s = s_form.save()
            a = a_form.save(commit=False)
            a.suitor_id = s
            a.save()
            messages.success(request,'Record Created')
            return HttpResponseRedirect('/suitor/')
        else:
            return HttpResponseRedirect(request.path_info)
    else:
        s_form=SuitorForm()
        a_form=AprncForm()
        context = {
                    's_form' : s_form,
                    'a_form' : a_form
                    }
        return render(request, 'suitor_form.html', context)

def edit_suitor(request, suitor_id):
    s_inst = get_object_or_404(Suitor,pk=suitor_id)
    a_inst = get_object_or_404(Aprnc,pk=suitor_id)

    if request.method=='POST':
        s_form=SuitorForm(request.POST or None, instance=s_inst)
        a_form=AprncForm(request.POST or None, instance=a_inst or None)
        if s_form.is_valid() and a_form.is_valid():
            s_form.save()
            a_form.save()
            return HttpResponseRedirect('/suitor/')
        else:
            return HttpResponseRedirect(request.path_info)
    else:
        s_form =SuitorForm(instance=s_inst)
        a_form=AprncForm(instance=a_inst or None)
        context = {
                    's_form' : s_form,
                    'a_form' : a_form,
                    }
        return render(request, 'suitor_form.html',context)

def view_suitor(request,suitor_id):
    s_inst = get_object_or_404(Suitor,pk=suitor_id)
    a_inst = get_object_or_404(Aprnc,pk=suitor_id)
    context = {
                'suitor' : s_inst,
                'aprnc'  : a_inst,
                }
    return render(request, 'suitor_view.html',context)
