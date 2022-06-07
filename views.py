from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def testimonials(request):
    return render(request, 'blog/testimonials.html', {'title': 'Testimonials'})

def services(request):
    return render(request, 'blog/services.html', {'title': 'Services'})

def references(request):
    return render(request, 'blog/references.html', {'title': 'References'})

def pay_invoice(request):
    return render(request, 'blog/pay_invoice.html', {'title': 'Pay invoice'})
