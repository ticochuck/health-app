from django.shortcuts import render
from .models import Post

data = [
    {
        'user': 'Chuck',
        'weight': '170',
        'date_posted': '11/11/2020',
        'notes': 'Hello from Chuck',
    },
    {
        'user': 'Laura',
        'weight': '140',
        'date_posted': '10/1/2019',
        'notes': 'Hello from Lau'
    }
]
def home(request):
    context = {
        # 'data': data
        'data': Post.objects.all()
    }
    return render(request, 'weights/home.html', context)


def about(request):
    return render(request, 'weights/about.html')
