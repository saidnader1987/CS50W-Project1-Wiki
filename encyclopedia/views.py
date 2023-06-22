from tkinter import Widget
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
import random
# import markdown2
from markdown2 import Markdown


from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label ="Title", widget=forms.TextInput (attrs={'class':'form-title'}))
    content = forms.CharField(label = "Content", widget=forms.Textarea (attrs={'class':'form-content'}))

class EditEntryForm(forms.Form):
    content = forms.CharField(label = "Content", widget=forms.Textarea (attrs={'class':'form-content'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, entry):
    # if content := util.get_entry(title):
    #     return render(request, "encyclopedia/entry.html", {
    #         "title": title,
    #         "content": content
    #     })
    # else:
    #     return render(request, "encyclopedia/error.html")    
    content = util.get_entry(entry)
    markdowner = Markdown()
    content = markdowner.convert(content)
    # content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "entry": entry if content else "Not found",
        "content": content if content else "Requested page not found"
    })

def search(request):
    if request.method == "GET":
        requested_entry = request.GET.get("q", "")
        entries = [entry.lower() for entry in util.list_entries()]
        # if requested page exists
        if requested_entry.lower() in entries:
            content = util.get_entry(requested_entry)
            return HttpResponseRedirect(reverse("wiki", args=(requested_entry,)))
        else:
            matches = []
            for entry in entries:
                if requested_entry in entry:
                    matches.append(entry.capitalize())
            # if there are matches, i.e. requested page is a substring of a page
            if len(matches) != 0:
            #     return render(request, "encyclopedia/search.html", {
            #         "matches": matches
            # })
                return render(request, "encyclopedia/index.html", {
                    "entries": matches
                })
            else:
                # requested page not found and not substring of any page
                return HttpResponseRedirect(reverse("wiki", args=(requested_entry,)))

def add(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            entries = [entry.lower() for entry in util.list_entries()]
            # title does not exist
            if not title.lower() in entries:
                util.save_entry(title.capitalize(), content)
                return HttpResponseRedirect(reverse("wiki", args=(title,)))
                # markdowner = Markdown()
                # content = markdowner.convert(content)
                # return render(request, "encyclopedia/entry.html", {
                #     "entry": title,
                #     "content": content
                # })
            # title exists
            else:
                return render(request, "encyclopedia/add.html", {
                    "form": form,
                    "message": "Page already exists"
                })
        # Form not valid
        else:
            return render(request, "encyclopedia/add.html", {
                "form": form
            })

    return render(request, "encyclopedia/add.html", {
        "form": NewEntryForm()
    })
        # return HttpResponse("HELLO WORLD")

def edit(request, entry):
    if request.method == "GET":
        content = util.get_entry(entry)
        form = EditEntryForm({"content":content})
        return render(request, "encyclopedia/edit.html", {
            "form": form,
            "entry": entry
        })
    else:
        form = EditEntryForm(request.POST)
        if form.is_valid():
            title = entry
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki", args=(entry,)))
        else:
            return render(request, "encyclopedia/edit.html", {
                "form": form
            })

def random_entry(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return HttpResponseRedirect(reverse("wiki", args=(entry,)))
    # content = util.get_entry(entry)
    # markdowner = Markdown()
    # content = markdowner.convert(content)
    # return render(request, "encyclopedia/entry.html", {
    #     "entry": entry,
    #     "content": content
    # })

                