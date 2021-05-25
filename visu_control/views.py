from django.shortcuts import render


def home_view(request):

    context = {

    }
    return render(request, 'upload.html', context)


def eda_view(request):

    context = {

    }
    return render(request, 'EDA.html', context)
