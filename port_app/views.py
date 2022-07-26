from django.shortcuts import redirect, render
from .forms import message_form

# Create your views here.

def index(request):
    form = message_form()
    if request.method == 'POST':
        check_form = message_form(request.POST)
        if check_form.is_valid():
            check_form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'index.html', context)
