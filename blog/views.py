from django.shortcuts import render
def post_list(request):
    return render(request, 'my-first-blog/templates/blog/post_list.html', {})
