import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from products.models import Product  # Импортируем вашу модель Product
from rest_framework import status

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(APIView):
    @swagger_auto_schema(
        operation_description="Create a Stripe Checkout Session",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'product_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the product"),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Quantity of the product"),
            },
            required=['product_id', 'quantity']
        ),
        responses={
            200: openapi.Response(
                description="Checkout Session ID",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING, description="Stripe Checkout Session ID")
                    }
                )
            ),
            400: openapi.Response(description="Error occurred"),
        }
    )
    def post(self, request, *args, **kwargs):
        """
        Create a Stripe Checkout Session for a product.
        """
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        try:
            data = request.data
            product_id = data.get('product_id')
            quantity = data.get('quantity', 1)

            # Проверяем существование и активность продукта
            try:
                product = Product.objects.get(pk=product_id, is_active=True)
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product not found or is not active'}, status=status.HTTP_404_NOT_FOUND)

            # Создаем сессию Stripe Checkout
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': product.name,
                                'description': product.description if product.description else "No description",
                            },
                            'unit_amount': int(product.price * 100),  # Цена в центах
                        },
                        'quantity': quantity,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
