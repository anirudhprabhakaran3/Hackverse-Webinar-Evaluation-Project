from django.forms import ModelForm
from submissions.models import Submission

class AddSubmission(ModelForm):
    class Meta:
        model = Submission
        fields = ['submission_url']

class AddMarksForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['marks']