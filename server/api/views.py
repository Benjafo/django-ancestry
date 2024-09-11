from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Person, Tree

# Create your views here.
def index(request):
    trees = Tree.objects.order_by("-created_date")[:5]
    context = { 'trees': trees }
    return render(request, 'api/index.html', context)

def tree(request, tree_id):
    tree = get_object_or_404(Tree, pk=tree_id)
    members = tree.members.all()
    context = {
        'tree': tree,
        'members': members
    }
    return render(request, 'api/tree.html', context)

def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    context = {
        'person': person
    }
    return render(request, 'api/person.html', context)