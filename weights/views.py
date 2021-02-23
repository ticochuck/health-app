from django.shortcuts import render

data = [
    {
        'user': 'Chuck',
        'weight': '170',
    },
    {
        'user': 'Laura',
        'weight': '140',
    }
]
def home(request):
    context = {
        'data': data
    }
    return render(request, 'weights/home.html', context)


def about(request):
    return render(request, 'weights/about.html')
