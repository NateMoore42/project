from django.shortcuts import render
from django.conf import settings
from django import forms, template
from django.shortcuts import (
    render, redirect, render_to_response, resolve_url, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView, UpdateView
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.utils import timezone

from character.forms import *
from character.models import *
from Auth.models import User
from elfsyndicate.settings import LOGIN_URL

@login_required(login_url=LOGIN_URL)
def character_create(request):
    user = request.user
    if request.method == 'POST':
        form = CreationForm(data=request.POST)
        if form.is_valid():
            player = user
            character = form.save(commit=False)
            character.player = player
            character.save()
            form.save_m2m()
            return redirect('/characters/character/%s' % character.pk)
    else:
        form = CreationForm()
    return render(request, 'character/create.html', {
        'form': form, 'user': user,
    })

def character_detail(request, pk):
    try:
        char = Character.objects.get(pk=pk)
        inv = Inventory.objects.get(character=char)
    except Character.DoesNotExist:
        char = None
        inv = None
        return redirect('/404/')
    return render(request, 'character/character-detail.html', {
        'char': char,
        'inv': inv
    })

@login_required(login_url=LOGIN_URL)
def character_edit(request, c_name, pk):
    c_name = Character.objects.get(c_name__iexact=c_name)
    user = request.user
    char = Character.objects.get(pk=pk)
    if request.user.username == user.username:
        if request.method == 'POST':
            inv = Inventory.objects.get(character=char)
            cform = CharEditForm(request.POST, instance=char)
            iform = InvEditForm(request.POST, instance=char.inventory)
            if cform.is_valid() and iform.is_valid():
                cform.save()
                iform.save()
                cform.save_m2m()
                iform.save_m2m()
        else:
            cform = CharEditForm(instance=char)
            iform = InvEditForm(instance=char.inventory)
        return render(request, 'character/character-edit.html', {
            'cform': cform,
            'iform': iform
        })
    else:
        return redirect('/characters/character/%s' % char.c_name)
    return redirect(request, '/characters/character/edit/%s' % char.c_name)

def handler404(request):
    response = render_to_response('404.html', {},
                context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                context_instance=RequestContext(request))
    response.status_code = 500
    return response
