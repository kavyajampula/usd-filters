from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'Hai HoW ARe you'}
    return render(request,'filters.html',d)
