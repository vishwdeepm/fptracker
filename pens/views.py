import contextlib
from django.shortcuts import render, redirect
from .models import Pen, PenForm, Ink, InkForm


# Create your views here.

def index(request):

    all_pens = Pen.objects.all()
    all_inks = Ink.objects.all()

    context = {
        'pen_list': all_pens,
        'ink_list': all_inks,
        'page_title': "Fountain Pen Collection",
    }

    return render(request, "index.html", context)



def edit_pen(request, pen_id=None):
    if request.method == 'POST':

        if pen_id is not None:
            pen = Pen.objects.get(id=pen_id)
            form = PenForm(request.POST, instance=pen)

        else:
            form = PenForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(index)

    else:
        if pen_id is not None:
            pen = Pen.objects.get(id=pen_id)
            form = PenForm(instance=pen)
        else:
            form = PenForm()

    context = {
        'form': form,
        'pen_id': pen_id,
    }

    return render(request, "edit_pen.html", context)


def delete_pen(request, pen_id):
    pen = Pen.objects.get(id=pen_id)

    pen.delete()
    return redirect(index)



def edit_ink(request, ink_id=None):
    if request.method == 'POST':
        if ink_id is not None:
            ink = Ink.objects.get(id=ink_id)
            form = InkForm(request.POST, instance=ink)
        else:
            form = InkForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(index)

    else:
        if ink_id is not None:
            ink = Ink.objects.get(id=ink_id)
            form = InkForm(instance=ink)
        else:
            form = InkForm()

    contaxt = {
        'form': form,
        'ink_id': ink_id,
    }

    return render(request, 'edit_pen.html', contaxt)
