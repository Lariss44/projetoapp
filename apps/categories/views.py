from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer
from .forms import CategoryForm



# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def add_category(request):
    template_name = 'categories/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)