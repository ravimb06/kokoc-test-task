from django.shortcuts import render, redirect
from .models import Category, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


#@login_required(login_url='/login/')
def index_page(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'quiz/index.html', context)

#@login_required(login_url='/login/')
def take_quiz(request, pk):
    questions = Question.objects.filter(choice=pk).order_by('-created_at')
    paginator = Paginator(questions,1)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    correct_answers = 0
    context = {'questions': questions, 'page_obj': page_obj,}
    

    if request.method == 'GET':
        if isinstance(request.GET.get('page'), str):
            if int(request.GET.get("page")) > len(questions):
                return render(request, 'quiz/index.html', context)
            request.session['previous_page'] = request.path_info + "?page=" + str(int(request.GET.get("page")) + 1)
            return render(request, 'quiz/quiz.html', context)
        else:
            request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '2')
            return render(request, 'quiz/quiz.html', context)
    
    if request.method == 'POST':
        correct_user_answers = []
        option = request.POST.get('option')
        if not option:
            messages.error(request, 'Сначала выберите ответ.')
            return redirect(request.session['previous_page'])
        user_answer = request.POST['option']
        correct_answer = request.POST.get('answerLabel')
        print('correct answer ',correct_answer)
        print('user answer: ', user_answer)
        if user_answer == correct_answer:
            correct_user_answers.append(user_answer)
            print(request.session['previous_page'])
            return HttpResponseRedirect(request.session['previous_page'])
        else:
            messages.warning(request, f'Неправильный ответ ! Правильный ответ: {correct_answer}')
            return HttpResponseRedirect(request.session['previous_page'])
