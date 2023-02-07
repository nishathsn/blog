import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from blog.models import Blog


def home_view(request, id=None, *args, **kwargs):

    print(id)
    name = "sunny"
    random_id = random.randint(1,3)

    blog_obj = Blog.objects.get(id=random_id)
    blog_quaryset = Blog.objects.all()


    context = {
        "object_list": blog_quaryset,
        "object": blog_obj,
        "title": blog_obj.title,
        "id": blog_obj.id,
        "content": blog_obj.content,

    }

    HTML_STRING = render_to_string("home-view.html",
    context=context)
    #HTML_STRING = """
    #<h1> Hello {title} (id: {id})! </h1>
    #<p> Hello {content} ! </p>
    #""".format(**context)

    return HttpResponse(HTML_STRING)