"""Circles Views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Module
from cride.circles.models import Circle


@api_view(['GET'])
def list_circles(request):
    """List circles."""
    pass
    cirlces = Circle.objects.all()
    public = cirlces.filter(is_public=True)

    data = list()

    for circle in public:
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'members_limit': circle.members_limit,
        })

    return Response(data)


@api_view(['POST'])
def create_circle(request):
    """Create circle."""
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')
    circle = Circle.objects.create(
        name=name,
        slug_name=slug_name,
        about=about
    )

    data = {
        'name': circle.name,
        'slug_name': circle.slug_name,
        'rides_taken': circle.rides_taken,
        'members_limit': circle.members_limit,
    }

    return Response(data)
