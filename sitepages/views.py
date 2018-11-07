from django.shortcuts import render, get_object_or_404


def about(request):
    return render(request, 'sitepages/about.html')


def contact(request):
    return render(request, 'sitepages/contact.html')

