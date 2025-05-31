from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
def home(request):
    form=ItemForm()
    message =''
    if request.method=='POST':
        form= ItemForm(request.POST)
        if form.is_valid():
            item_name=form.cleaned_data['name']
            if Item.objects.filter(name=item_name).exists():
                message='Item already exists!'
            else:
                form.save()
                message ="Item added successfully!"
                form = ItemForm()  # reset form
    return render(request,'inventory/home.html', {'form': form, 'message': message} )

def monthly_list(request):
    return render(request, 'inventory/monthly_list.html')