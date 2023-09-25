# Import necessary modules from Django
from django import forms
from .models import BorrowRecord


# Define a form class called BorrowRecordForm that inherits from forms.ModelForm
class BorrowRecordForm(forms.ModelForm):
    class Meta:
        # Specify the model that this form is associated with (BorrowRecord)
        model = BorrowRecord

        # Define which fields from the model should be included in the form
        # In this case, an empty list means no fields are included explicitly,
        # so all fields from the BorrowRecord model will be included by default.
        fields = []


# Define another form class called ReturnBookForm that also inherits from forms.ModelForm
class ReturnBookForm(forms.ModelForm):
    class Meta:
        # Specify the model that this form is associated with (BorrowRecord)
        model = BorrowRecord

        # Define which fields from the model should be included in the form
        # Similar to BorrowRecordForm, an empty list means no fields are included explicitly,
        # so all fields from the BorrowRecord model will be included by default.
        fields = []
