from django.shortcuts import render


# Create your views here.
def home_view(requst, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 12313]
    }
    return render(requst, 'home.html', my_context)
