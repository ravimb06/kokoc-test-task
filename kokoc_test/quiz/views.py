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
    number_of_questions = len(questions)
    correct_answers = 0
    correct_user_answers = request.session.get('correct_user_answers', [])
    context = {'questions': questions,
               'page_obj': page_obj,
               'correct_answers': correct_answers,
               'number_of_questions': number_of_questions,
               'correct_user_answers':correct_user_answers,
    }
    

    if request.method == 'GET':
        if int(request.GET.get('page', '1')) > number_of_questions:
            return render(request, 'quiz/results.html', context)
        request.session['previous_page'] = (
            request.path_info + "?page=" + str(int(request.GET.get('page', '1')) + 1)
        )
        return render(request, 'quiz/quiz.html', context)
        
    
    if request.method == 'POST':
        user_answers = request.session.get('correct_user_answers')
        option = request.POST.get('option')
        print(user_answers)
        if not option:
            messages.error(request, 'Сначала выберите ответ.')
            return redirect(request.session['previous_page'])
        if not user_answers:
            request.session['correct_user_answers'] = []
        user_answer = request.POST['option']
        correct_answer = request.POST.get('answerLabel')
        if user_answer == correct_answer:
            user_answers.append(user_answer)
            request.session['correct_user_answers'] = user_answers
            #correct_answers += 1
            return HttpResponseRedirect(request.session['previous_page'])
        else:
            messages.warning(request, f'Неправильный ответ ! Правильный ответ: {correct_answer}')
            return HttpResponseRedirect(request.session['previous_page'])
