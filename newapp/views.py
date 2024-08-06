from django.shortcuts import redirect, render
from .models import Member

def index(request):
    """
    View function to display all members.

    Retrieves all member records from the database and renders the 'index.html' template.
    The template is provided with the list of members.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'index.html' template with the list of members.
    """
    mem = Member.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add(request):
    """
    View function to render the 'add.html' template.

    Renders the template for adding a new member.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'add.html' template.
    """
    return render(request, 'add.html')

def addrec(request):
    """
    View function to handle adding a new member.

    Retrieves data from the POST request, creates a new Member object, saves it to the database,
    and redirects to the index view.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the index view.
    """
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member(firstname=x, lastname=y, country=z)
    mem.save()
    return redirect("/")

def delete(request, id):
    """
    View function to delete a member.

    Retrieves the member by ID, deletes it from the database, and redirects to the index view.

    Args:
        request: The HTTP request object.
        id: The ID of the member to delete.

    Returns:
        HttpResponseRedirect: Redirects to the index view.
    """
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    """
    View function to render the 'update.html' template.

    Retrieves the member by ID and renders the template for updating the member.

    Args:
        request: The HTTP request object.
        id: The ID of the member to update.

    Returns:
        HttpResponse: The rendered 'update.html' template with the member's current data.
    """
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    """
    View function to handle updating a member's information.

    Retrieves data from the POST request, updates the member's information, saves it to the database,
    and redirects to the index view.

    Args:
        request: The HTTP request object.
        id: The ID of the member to update.

    Returns:
        HttpResponseRedirect: Redirects to the index view.
    """
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member.objects.get(id=id)
    mem.firstname = x
    mem.lastname = y
    mem.country = z
    mem.save()
    return redirect("/")
