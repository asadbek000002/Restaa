from django import forms


from .models import OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'