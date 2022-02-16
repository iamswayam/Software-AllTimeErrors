from django.shortcuts import render, redirect
from . import forms
from .models import allErrors
from django.db.models import Q


def new(request):
    if request.method == 'POST':
        form = forms.allErrorsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('new')

    else:
        form = forms.allErrorsForm()

    return render(request, 'new.html', {'form': form})


def basic(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    allError = allErrors.objects.filter(
        Q(error_type__icontains=search_query) | Q(solution__icontains=search_query))

    return render(request, 'home.html', {'allError': allError, 'search_query': search_query})


# def django(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     allqna = qanda.objects.filter(Q(question__icontains = search_query) | Q(answer__icontains = search_query))
#     return render(request, 'django.html', {'allqna': allqna})


# def python(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     allqna = qanda.objects.filter(Q(question__icontains = search_query) | Q(answer__icontains = search_query))
#     return render(request, 'python.html', {'allqna': allqna})


# def database(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     allqna = qanda.objects.filter(Q(question__icontains = search_query) | Q(answer__icontains = search_query))
#     return render(request, 'database.html', {'allqna': allqna})


# def api(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     allqna = qanda.objects.filter(Q(question__icontains = search_query) | Q(answer__icontains = search_query))
#     return render(request, 'api.html', {'allqna': allqna})


# def aws(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     allqna = qanda.objects.filter(Q(question__icontains = search_query) | Q(answer__icontains = search_query))
#     return render(request, 'aws.html', {'allqna': allqna})


# def frontend(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     allqna = qanda.objects.filter(Q(question__icontains = search_query) | Q(answer__icontains = search_query))
#     return render(request, 'frontend.html', {'allqna': allqna})


# def extra(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     allqna = qanda.objects.filter(Q(question__icontains = search_query) | Q(answer__icontains = search_query))
#     return render(request, 'extra.html', {'allqna': allqna})
