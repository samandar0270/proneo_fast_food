from django.urls import path
from api.catalog.views import (ListCategories, OneCategories,
                        ProductView, CategoryView, ListProduct)


urlpatterns = [
    path('category/', ListCategories.as_view()),
    path('category2/', CategoryView.as_view()),
    path('product/', ListProduct.as_view(), name='products'),
    path('category/<int:id>/', OneCategories.as_view()),
]
