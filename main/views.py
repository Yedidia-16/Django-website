from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CraeteNewList


# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():
        if response.method == "POST":
            # if the type of the information that was sent is POST
            print(response.POST)
            if response.POST.get('save'):
                # if the user wants to save (let say he just complete a task) -
                # he will click the Done button and the information will be saved.
                for item in ls.item_set.all():
                    if response.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()
            elif response.POST.get('newItem'):
                txt = response.POST.get('new')
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print('Invalid input.')
                    # in order to create new task the name should be longer than 2 characters

        return render(response, 'main/list.html', {'ls': ls})
    return render(response, "main/view.html", {})
    # if name=name stores the list that has id of "id"

    # when:
    # def index(response, name):
    #     ls = ToDoList.objects.get(name=name)  # stores the list that has id of "id"
    #     item = ls.item_set.get(id=1)
    #     return HttpResponse('<center><h1>%s</h1></center><br></br><p>%s</p>' % (ls.name, str(item.text)))
    # Than it will:
    # print the name of the list that has the same name.
    # also it will show the item (meaning: the task) that is under this particular list.


def home(response):
    # This will send the user to the home page
    # (that its html code is in home.html file)
    return render(response, 'main/home.html', {})


def create(response):
    if response.method == "POST":
        form = CraeteNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            # By that we clean the information and getting only the value of name.
            t = ToDoList(name=n)
            t.save()
            # When we are getting a post type of info we will create a list with the name that was given
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
        # after creating new list - this will direct us to the new list page
    else:
        form = CraeteNewList()

    return render(response, 'main/create.html', {"form": form})


def view(response):
    return render(response, 'main/view.html', {})