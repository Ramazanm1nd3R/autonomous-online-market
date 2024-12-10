from django.urls import path
from .views import CreateCheckoutSessionView
from django.views.generic import TemplateView

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('checkout/', TemplateView.as_view(template_name="checkout.html"), name='checkout'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),
    path('cancel/', TemplateView.as_view(template_name="cancel.html"), name='cancel'),
]
