from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from profiles.models import Profile

from .models import Category, Question


def index_page(request):
    """Функция отображения главной страницы"""
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "quiz/index.html", context)


def best_users(request):
    """Функция отображени списка лучших пользователей."""
    profiles = Profile.objects.all().order_by("scores")
    context = {"profiles": profiles}
    return render(request, "quiz/best_users.html", context)


def results(request):
    """Функция отображения результатов теста."""
    all_answers = request.session.pop("user_answers", 0)
    correct_answers = request.session.pop("correct_user_answers", 0)
    if correct_answers and all_answers:
        percentages = int((correct_answers / all_answers) * 100)
        score = percentages * correct_answers
        coins = int(percentages / 10 * correct_answers)
        result = "Тест пройден" if percentages > 70 else "Тест не пройден"
        if percentages > 70:
            Profile.objects.filter(id=request.user.id).update(coins=F("coins") + coins)
            Profile.objects.filter(id=request.user.id).update(
                tests_taken=F("tests_taken") + 1
            )
        context = {
            "all_answers": all_answers,
            "percentages": percentages,
            "correct_answers": correct_answers,
            "coins": coins,
            "score": score,
            "result": result,
        }
    else:
        context = {"percentages": 0}
    return render(request, "quiz/results.html", context)


@login_required()
def take_quiz(request, pk):
    """Функция процесса тестирования."""
    questions = Question.objects.filter(choice=pk).order_by("-created_at")
    paginator = Paginator(questions, 1)
    page_number = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_number)
    number_of_questions = len(questions)
    user_answers = request.session.get("user_answers", 0)
    correct_user_answers = request.session.get("correct_user_answers", 0)
    context = {
        "questions": questions,
        "page_obj": page_obj,
        "number_of_questions": number_of_questions,
        "correct_user_answers": correct_user_answers,
    }

    if request.method == "GET":
        if int(request.GET.get("page", "1")) > number_of_questions:
            return results(request)
        request.session["next_page"] = (
            request.path_info + "?page=" + str(int(request.GET.get("page", "1")) + 1)
        )
        return render(request, "quiz/quiz.html", context)

    if request.method == "POST":
        option = request.POST.get("option")
        if not option:
            messages.error(request, "Сначала выберите ответ.")
            return redirect(request.session["previous_page"])
        user_answer = request.POST["option"]
        correct_answer = request.POST.get("answerLabel")
        user_answers += 1
        request.session["user_answers"] = user_answers
        if user_answer == correct_answer:
            correct_user_answers += 1
            request.session["correct_user_answers"] = correct_user_answers
            return HttpResponseRedirect(request.session["next_page"])
        else:
            return HttpResponseRedirect(request.session["next_page"])
