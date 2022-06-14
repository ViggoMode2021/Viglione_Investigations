from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def testimonials(request):
    return render(request, 'blog/testimonials.html', {'title': 'Testimonials'})

def services(request):
    return render(request, 'blog/services.html', {'title': 'Services'})

def references(request):
    return render(request, 'blog/references.html', {'title': 'References'})

#Spanish pages
def home_spanish(request):
    return render(request, 'blog/home_spanish.html', {'title': 'Home - Spanish'})
