import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from common.permissions import IsAuthenticatedUser

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedUser]

stripe.api_key = settings.STRIPE_SECRET_KEY

# Описание параметров для Swagger
currency_param = openapi.Parameter(
    'currency', openapi.IN_BODY, description="Currency for payment (e.g., 'usd')",
    type=openapi.TYPE_STRING, required=True
)
name_param = openapi.Parameter(
    'name', openapi.IN_BODY, description="Name of the product",
    type=openapi.TYPE_STRING, required=True
)
amount_param = openapi.Parameter(
    'amount', openapi.IN_BODY, description="Amount in cents (e.g., 5000 = $50.00)",
    type=openapi.TYPE_INTEGER, required=True
)
quantity_param = openapi.Parameter(
    'quantity', openapi.IN_BODY, description="Quantity of the product",
    type=openapi.TYPE_INTEGER, required=True
)

class CreateCheckoutSessionView(APIView):
    @swagger_auto_schema(
        operation_description="Create a Stripe Checkout Session",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'currency': openapi.Schema(type=openapi.TYPE_STRING, description="Currency for payment (e.g., 'usd')"),
                'name': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the product"),
                'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description="Amount in cents"),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Quantity of the product"),
            },
            required=['currency', 'name', 'amount', 'quantity']
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
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': data['currency'],
                            'product_data': {
                                'name': data['name'],
                            },
                            'unit_amount': data['amount'],  # Ожидается в центах
                        },
                        'quantity': data['quantity'],
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
