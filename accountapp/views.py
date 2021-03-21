from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm


has_decorator = [login_required, account_ownership_required]


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:main')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


'''
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
'''


@method_decorator(has_decorator, 'get')
@method_decorator(has_decorator, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:main')
    template_name = 'accountapp/update.html'


'''
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
'''


'''
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
'''


@method_decorator(has_decorator, 'get')
@method_decorator(has_decorator, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


'''
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
'''


def success(request):
    return render(request, 'success.html')


@login_required
def main(request):
    return render(request, 'accountapp/main.html')


'''
def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))
'''

