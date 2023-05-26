from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 0
        request.session['count'] = 0
    return render(request, 'index.html')

def clear(request):
    request.session.clear()
    return redirect('/')

def increase(request):
    request.session['count'] += int(request.POST['number'])
    
    return redirect('/')