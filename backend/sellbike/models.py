from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])  # Only POST requests are allowed
def bike_valuation(request):
    data = request.data
    brand = data.get("brand")
    model = data.get("model")
    variant = data.get("variant")
    year = int(data.get("year", 2023))
    kms = int(data.get("kms", 0))
    owner = data.get("owner", "1st Owner")

    # Example price calculation
    base_price = 100000
    depreciation = (2025 - year) * 5000
    kms_factor = kms * 1
    owner_factor = 0 if owner == "1st Owner" else 5000 * (int(owner[0]) - 1)
    estimated_price = max(base_price - depreciation - kms_factor - owner_factor, 5000)

    return Response({"price": estimated_price})
