from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
     # return HttpResponse("hello")

def netflix(request):
    return render(request, 'netflix.html')

# Go to homepage
def base(request):
    return render(request, 'home.html')   

def top10(request):
    return render(request, 'top1-10.html')     

def top20(request):
    return render(request,'top11-20.html')

def recommend(request):
    return render(request, 'recommend.html')

def rec11_20(request):
    return render(request, 'rec11-20.html')    

def rec21_30(request):
    return render(request, 'rec21-30.html')      

def rec31_40(request):
    return render(request, 'rec31-40.html')

def rec41_50(request):
    return render(request, 'rec41-50.html')

def rec51_58(request):
    return render(request, 'rec51-58.html')    

def action(request):
    return render(request, 'action.html')      

def adventure(request):
    return render(request, 'adventure.html')    

def comedy(request):
    return render(request, 'comedy.html')      

def horror(request):
    return render(request, 'horror.html')  

def history(request):
    return render(request, 'history.html')      

def documentary(request):
    return render(request, 'documentary.html')    

def drama(request):
    return render(request, 'drama.html')  

def sci_fi(request):
    return render(request, 'sci_fi.html')  