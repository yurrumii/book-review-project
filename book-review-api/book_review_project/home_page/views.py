import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout


def some_view(request):
    return render(request, 'home_page/index.html')


def book_list(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api/books/')
        if response.status_code == 200:
            books = response.json()
        else:
            books = []
    except:
        books = []

    return render(request, 'home_page/book_list.html', {'books': books})


def book_detail(request, pk):
    try:
        book_response = requests.get(f'http://127.0.0.1:8000/api/books/{pk}/')
        if book_response.status_code == 200:
            book = book_response.json()
        else:
            book = None

        reviews_response = requests.get(f'http://127.0.0.1:8000/api/books/{pk}/reviews/')
        if reviews_response.status_code == 200:
            reviews = reviews_response.json()
        else:
            reviews = []
    except:
        book = None
        reviews = []

    user_reviewed = False
    if request.user.is_authenticated:
        for review in reviews:
            if review.get('user') == request.user.id:
                user_reviewed = True
                break

    return render(request, 'home_page/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'user_reviewed': user_reviewed
    })


def add_book(request):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
            'description': request.POST.get('description')
        }

        response = requests.post(
            'http://127.0.0.1:8000/api/books/',
            data=data
        )
        if response.status_code == 201:
            return redirect('/books/')

    return render(request, 'home_page/add_book.html')


def add_review(request, book_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Только авторизованные пользователи могут добавлять рецензии.')
        return redirect('login')

    reviews_response = requests.get(f'http://127.0.0.1:8000/api/books/{book_id}/reviews/')
    user_reviewed = False
    if reviews_response.status_code == 200:
        reviews = reviews_response.json()
        for review in reviews:
            if review.get('user') == request.user.id:
                user_reviewed = True
                break
    else:
        reviews = []

    if user_reviewed:
        messages.error(request, 'Вы уже оставляли рецензию на эту книгу.')
        return redirect('book_detail', pk=book_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        if not rating or not text:
            messages.error(request, 'Пожалуйста, заполните все поля!')
            return redirect('book_detail', pk=book_id)
        data = {
            'user': request.user.id,
            'rating': rating,
            'text': text
        }

        headers = {
            'X-CSRFToken': request.META.get('CSRF_COOKIE', ''),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(
            f'http://127.0.0.1:8000/api/books/{book_id}/reviews/',
            data=data,
            headers=headers
        )
        if response.status_code == 201:
            messages.success(request, 'Рецензия успешно добавлена')
        else:
            messages.error(request, f'Ошибка при добавлении рецензии, Статус: {response.status_code}')
        return redirect('book_detail', pk=book_id)

    return redirect('book_detail', pk=book_id)


def logout_view(request):
    logout(request)
    return redirect('/login/')
