from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка отправления! Попробуте еще раз!')
    else:
        form = OrderForm()
    return render(request, 'main/index.html', {'form': form})
