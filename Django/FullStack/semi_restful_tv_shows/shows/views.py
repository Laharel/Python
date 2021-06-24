from django.shortcuts import redirect, render
from .models import Show
from datetime import datetime

# Create your views here.

# jus redircts to new_show_form()
def index(request):
    return redirect('/shows')

# GET: returns a form for creating new show
def new_show_form(request):
    return render(request, 'new_show.html')

# POST: receives the form from new_show_form() and creates new show
def create_show(request):
    title_ = request.POST['title']
    network_ = request.POST['network']
    release_date_ = request.POST['release-date']
    description_ = request.POST['desc']

    new_show = Show.objects.create(
        title=title_,
        network=network_,
        release_date=release_date_,
        description=description_
    )

    return redirect('/shows/'+str(new_show.id))

# GET: returns a template to display the passed show is in /shows/<id>
def show_details(request,id):
    show = Show.objects.get(id=int(id))
    context={
        'show': show,
    }

    return render(request, 'show_details.html', context)

# GET: returns a template that displays all shows
def shows(request):
    all_shows = Show.objects.all()
    context={
        'all_shows': all_shows,
    }
    return render(request, 'shows.html', context)

# GET: returns a form for editing the passed Show() from show_details() - edit button
def edit_show(request, id):
    show = Show.objects.get(id=int(id))
    datestring = '20121212'
    date = str(show.release_date)

    date = datetime.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y')

    context={
        'show':show,
        'release_date': date,
    }
    return render(request, 'edit_show.html', context)

# POST: receives the form from edit_show() and processes it then redirect to show_details()
def update_show(request, id):

    show = Show.objects.get(id=id)
    title_ = request.POST['title']
    network_ = request.POST['network']
    release_date_ = request.POST['release-date']
    if not release_date_:
        release_date_ = show.release_date

    description_ = request.POST['desc']

    show = Show.objects.get(id=id)
    show.release_date = release_date_
    show.title = title_
    show.network = network_
    show.description = description_
    show.save()

    return redirect('/shows/'+str(show.id))

# POST: receives show id from show_details() or from shows() - delete buttons
def destroy_show(request, id):
    Show.objects.get(id=id).delete()

    return redirect('/shows')