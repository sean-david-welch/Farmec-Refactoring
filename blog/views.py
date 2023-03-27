from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . models import Blog, Exhibition
from . forms import BlogForm, ExhibitionForm

models = {
    'blog': Blog,
    'exhibition': Exhibition,
}

forms = {
    'blog': BlogForm,
    'exhibition': ExhibitionForm,
}

#######################################################
#################### Blog Views ######################
#######################################################
def blogs(request):
    blogs = Blog.objects.all()

    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)

def single_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {'blog': blog}
    return render(request, 'blog/single_blog.html', context)

def exhibitions(request):
    exhibitions = Exhibition.objects.all()

    context = {'exhibitions': exhibitions}
    return render(request, 'blog/exhibitions.html', context)

#######################################################
################# Blog Models C.R.U.D. ###############
#######################################################

def create_model_blog(request, model_name):
    form_class = forms[model_name]

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('blogs')
    else:
        form = form_class()

    context = {'form': form, 'model_name': model_name}
    return render(request, 'model_form.html', context)

def edit_model_blog(request, model_name, pk):
    model = models[model_name].objects.get(id=pk)
    form_class = forms[model_name]
    form = form_class(instance=model)

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=model)
        if form.is_valid():
            model = form.save()
            return redirect('single_blog', pk=model.id)
        
    context = {'form': form, 'model_name': model_name}
    return render(request, 'model_form.html', context)

def delete_model_blog(request, model_name, pk):
    model = models[model_name].objects.get(id=pk)

    if request.method == 'POST':
        model.delete()
        return redirect('blogs')

    context = {'object': model}
    return render(request, 'delete_form.html', context)