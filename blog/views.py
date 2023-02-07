from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import BlogForm
from .models import Blog
# Create your views here.

def blog_search_view(request):
    #print(dir(request))
    #print(request.GET)
    query_dict = request.GET #this is a dictionary
    #query =query_dict.get("q") #<input type="text" name="q" />
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    blog_obj = None
    if query is not None:
        blog_obj = Blog.objects.get(id=query)
    context = {
        "object": blog_obj
    }
    return render(request, "blog/search.html", context=context)

@login_required

def blog_create_view(request):
    #print(request.POST)
    form = BlogForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        blog_object = form.save()
        context['form'] = BlogForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # blog_object = Blog.objects.create(title=title, content=content)
        # context['object'] = blog_object
         #context['created'] = True
    return render(request, "blog/create.html",
                  context=context)


# def blog_create_view(request):
#     #print(request.POST)
#     form = BlogForm()
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = BlogForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             blog_object = Blog.objects.create(title=title, content=content)
#             context['object'] = blog_object
#             context['created'] = True
#     return render(request, "blog/create.html",
#                   context=context)

def blog_detail_view(request, id=None):
    blog_obj = None
    if id is not None:
        blog_obj = Blog.objects.get(id=id)
    context = {
        "object": blog_obj,
    }

    return render(request, "blog/detail.html",
                  context=context)
