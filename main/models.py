from django.db import models

# Create your models here.


class ToDoList(models.Model):
    # We have to define what type is it
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # Since the toDoList is connected with the last class
    # So it will be deleted when you delete the list
    text = models.CharField(max_length=300)
    # Since the Todo list isn't defined by Django we got to define it
    complete = models.BooleanField()
    # this one will tell us if we have completed our task.

    def __str__(self):
        return self.text
