from django.shortcuts import render


def create(request):

    context = {

    }

    return render(
        request,
        'contact/pages/create.html',
        context
    )
