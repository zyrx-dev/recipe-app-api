# from django.shortcuts import render

# # Create your views here.

"""
Views for the Recipe APIs.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View to manage recipe APIs."""

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Overrides default behavior and retrieves
        recipes only for the authenticated user.
        """

        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """
        Overrides default behavior and retrieves
        the serializer class specific to a request.
        """

        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """
        Overrides the behaviour of saving a model in a view set,
        it creates a new recipe and sets the correct user for it.
        """

        serializer.save(user=self.request.user)
