from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('store/', views.store, name="store"),
	path('add/', views.storeAdd, name="add"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path("login/",views.user_login,name='login'),
    path("singup/",views.user_singup,name='singup'),
    path("logout/",views.user_logout,name='logout'),

]