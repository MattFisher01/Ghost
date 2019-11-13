from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from name_picker.models import ghost_user, ghost_names
from .forms import LoginForm, name_picker_form

# Create your views here.

def overview_page(request, logged='false'):

    # Get list of ghost names from database, including names of those who have already picked a name
    # On django template, display link to name picker
    # If user already has a ghost name, display link that says to pick another name instead
    all_names = ghost_names.objects.all()
    # print('All names: ', all_names)
    context = {'all_names': all_names, 'logged_in': logged}
    return render(request, 'overview.html', context)


def ghost_name_form(request):
    import random

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = name_picker_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            # redirect to a new URL:
            return HttpResponseRedirect('true')

    # if a GET (or any other method) create a blank form
    else:
        available_names = ghost_names.objects.filter(person__isnull=True)
        print('Number of available names: ', len(available_names))
        r = random.sample(range(0, len(available_names)), 3)
        print(r)
        for i in r:
            print(available_names[i])
        form = name_picker_form('1', '2', '3')
        form._c1 = 'New Value'
    return render(request, 'ghost_picker.html', {'form': form})


def login(request):
    from .models import ghost_user

    # if this is a POST request process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.data['first_name'])
            users = ghost_user.objects.filter(first_name=form.data['first_name'], last_name=form.data['last_name'])
            if users:
                print('Already in database')
                return HttpResponseRedirect('true')
            else:
                return HttpResponseRedirect('false')


            # redirect to a new URL:
            return HttpResponseRedirect('true')

    # if a GET (or any other method) create a blank form
    else:
        form = LoginForm()
    return render(request, 'loginform.html', {'form': form})




