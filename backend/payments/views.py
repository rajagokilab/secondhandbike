# payments/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Payment

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):
    user = request.user
    amount = request.data.get("amount")
    method = request.data.get("method")
    bike_id = request.data.get("bike")

    # basic validation
    if not amount or not bike_id:
        return Response({"error": "Amount and bike ID are required"}, status=400)

    payment = Payment.objects.create(
        user=user,
        bike_id=bike_id,
        amount=amount,
        method=method
    )
    return Response({"success": True, "payment_id": payment.id})
