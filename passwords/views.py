from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from passwords.models import StoredPassword
from passwords.forms import AddPasswordForm

class PasswordsView(LoginRequiredMixin, TemplateView):
    template_name = 'passwords/passwords.html'

    def get(self, request):
        form = AddPasswordForm(request.POST or None)
        queryset = StoredPassword.objects.filter(user=request.user)
        context = {'form': form, 'object_list': queryset}
        return render(request, 'passwords.html', context) 

    def post(self, request):
        storedpassword = StoredPassword(user = request.user)
        form = AddPasswordForm(request.POST, instance=storedpassword)
        if form.is_valid():
            form.save()
        queryset = StoredPassword.objects.filter(user=request.user)
        context = {'form': form, 'object_list': queryset}
        return render(request, 'passwords.html', context)

@login_required
def deletePasswordView(request):
    pk = request.POST.get('instance_pk')
    if pk: 
        pk = int(pk)
        StoredPassword.objects.filter(pk = pk).delete()
        return redirect('/home/')
# Create your views here.
