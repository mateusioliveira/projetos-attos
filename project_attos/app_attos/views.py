from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "app_attos/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "app_attos/detail.html", {"question": question})


def instagram_button(request):
    if request.method == 'POST':
        instagram_link = request.POST.get('instagram_link')
        return render(request, 'app_attos/instagram_button.html', {'instagram_link': instagram_link})
    return render(request, 'app_attos/instagram_form.html')


