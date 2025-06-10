from django.shortcuts import render

# Create your views here.
def footer_detail(request):
    return render(request, 'footer/footer-detail.html')