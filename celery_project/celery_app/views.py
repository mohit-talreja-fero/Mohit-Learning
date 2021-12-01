from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts



class GenerateRandomUserView(FormView):
    template_name = 'celery_app/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')

    

def show_users(request):
    users = User.objects.all()
    template = 'celery_app/users_list.html'
    context = {
        'users': users,
    }
    return render(request, template, context)