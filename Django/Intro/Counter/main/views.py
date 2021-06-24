from typing import Counter
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += int(1)
    else:
        request.session['counter'] = int(0)
    return render(request,"index.html")

def clear(request):
    del request.session['counter']	# clears a specific key
    return redirect('/')