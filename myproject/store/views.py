from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Recipe


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    try:
        recipes = Recipe.objects.get(category=pk)
    except Recipe.DoesNotExist:
        recipes = None
    return render(request, 'category.html', {'category': category, 'recipes' : recipes})

def recipe(request, pk):
   
    recipe = get_object_or_404(Recipe, pk=pk)    
    return render(request, 'recipe.html', {'recipe': recipe})


def new_category(request):
   

    if request.method =='POST':
        title= request.POST['title']
        description= request.POST['description']
        
       
        category= Category.objects.create(
            title= title,
            description = description        
        )  

        return redirect('category', pk=category.pk)
    return render(request, 'new_category.html')

    
def new_recipe(request):
    if request.method =='POST':
        title= request.POST['title']
        ingredients= request.POST['ingredients']
        description= request.POST['description']
        category_pk = request.POST['category']
        category =Category.objects.get(pk=int(category_pk))
        

        
        recipe= Recipe.objects.create(
            title= title,
            ingredients= ingredients,
            description = description, 
            category = category
        )        
        return redirect('recipe', pk=recipe.pk)

    
    id = int(request.GET.get('category'))
 
    

    categories = Category.objects.all()
  

    return render(request, 'new_recipe.html', {'categories': categories, 'category_pk': id})
    
