from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . models import Supplier, Machine, Product, Video
from . forms import SupplierForm, MachineForm, ProductForm, VideoForm


models = {
    'supplier': Supplier,
    'machine': Machine,
    'product': Product,
    'video': Video,
}

forms = {
    'supplier': SupplierForm,
    'machine': MachineForm,
    'product': ProductForm,
    'video': VideoForm,
}

########################################################
#################### Supplier Views ####################
########################################################

def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {'suppliers': suppliers}
    return render(request, 'suppliers/suppliers.html', context)

def supplier_page(request, pk):
    supplier = Supplier.objects.get(id=pk)

    context={'supplier': supplier}
    return render(request, 'suppliers/supplier_page.html', context)

########################################################
################# Supplier Models C.R.U.D. #############
########################################################

def create_model_supplier(request, model_name):
    form_class = forms[model_name]

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('suppliers')
    else:
        form = form_class()

    context = {
        'form': form,
        'model_name': model_name,
    }
    return render(request, 'model_form.html', context)

def edit_model_supplier(request, model_name, pk):
    model = models[model_name].objects.get(id=pk)
    form_class = forms[model_name]
    form = form_class(instance=model)

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=model)
        if form.is_valid():
            model = form.save()
            return redirect('suppliers')

    context = {'form': form, 'model': model}
    return render(request, 'model_form.html', context)

def delete_model_supplier(request, model_name, pk):
    model = models[model_name].objects.get(id=pk)

    if request.method == 'POST':
        model.delete()
        return redirect('suppliers')
 
    context = {'object': model}
    return render(request, 'delete_form.html', context)




