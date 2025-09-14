from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('supplier', 'Supplier'),
        ('vendor', 'Vendor'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    pincode = forms.CharField(max_length=10, required=True)
    state = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "role", "phone_number", "address", "pincode", "state", "password1", "password2"]

from django import forms
from .models import Order

class AcceptOrderForm(forms.ModelForm):
    expected_delivery_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    delivery_notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        help_text="Add any delivery instructions for the vendor"
    )

    class Meta:
        model = Order
        fields = ['expected_delivery_date', 'delivery_notes']