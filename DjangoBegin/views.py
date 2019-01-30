from django.shortcuts import redirect, render


# def redirect_to_blog(request):
#     return redirect('post_list_url', permanent=True)


def home(request):
    return render(request, 'home_page.html', context={})
