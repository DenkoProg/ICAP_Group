from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse


class SuperuserRequired(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('login'))


class ProductListCreateView(SuperuserRequired, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(SuperuserRequired, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        offer_of_the_month = self.request.query_params.get('offer_of_the_month', None)
        availability = self.request.query_params.get('availability', None)
        self_pickup = self.request.query_params.get('self_pickup', None)

        if offer_of_the_month is not None:
            queryset = queryset.filter(offer_of_the_month=offer_of_the_month)
        if availability is not None:
            queryset = queryset.filter(availability=availability)
        if self_pickup is not None:
            queryset = queryset.filter(self_pickup=self_pickup)

        return queryset
