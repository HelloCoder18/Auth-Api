from django.urls import path
from . import views
urlpatterns = [
    path('',views.GetRecipe.as_view(),name='recipes'), 
    path('add',views.AddRecipe.as_view(),name='newrecipe'),
    path('delete',views.RemoveRecipe.as_view(),name='deleterecipe'),
    path('<str:author>/<int:id>',views.RemoveRecipe.as_view(),name='deleterecipe'),
    path('<str:author>/',views.FindRecipe.as_view(),name='recipe'),
]
