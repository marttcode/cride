"""Circles Views."""

# Django
from django.http import JsonResponse

# Module
from cride.circles.models import Circle


def list_circles(request):
    """List circles."""
    cirlces = Circle.objects.all()
    public = cirlces.filter(is_public=True)

    data = list()

    for circle in public:
        data.append({
            'name': circle.name,
        })

    return JsonResponse(data, safe=False)
