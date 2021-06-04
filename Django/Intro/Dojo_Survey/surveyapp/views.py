from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # this is the route that shows the form
    return render(request,"index.html")

def result(request):
    # this is the route that processes the form
    name_form = request.POST['name']
    location_form = request.POST['location']
    language_form = request.POST['language']
    comment_form = request.POST['comment']
    gender_form = request.POST['gender']
    context = {
    	"name_on_template" : name_form,
    	"location_on_template" : location_form,
    	"language_on_template" : language_form,
    	"comment_on_template" : comment_form,
    	"gender_on_template" : gender_form
    }
    return render(request,"result.html", context)