from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from submissions.models import Submission
from submissions.forms import AddSubmission, AddMarksForm

# Create your views here.

@login_required
def dashboard(request):
    submissions = Submission.objects.all()
    args = {
        'submissions': submissions,
    }
    if request.user.is_superuser:
        return render(request, 'submissions/admin_dashboard.html', args)
    else:
        submission = Submission.objects.filter(user=request.user).first()
        args = {
            'submission': submission,
        }
        return render(request, 'submissions/student_dashboard.html', args)

def scoreboard(request):
    submissions = Submission.objects.all().order_by('-marks')
    args = {
        'submissions': submissions,
    }
    return render(request, 'submissions/scoreboard.html', args)

def view_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    args = {
        'submission': submission,
    }
    return render(request, 'submissions/view_submission.html', args)

def add_submission(request):
    if request.method == 'POST':
        form = AddSubmission(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = User.objects.get(id=request.user.id)
            submission.save()
            messages.success(request, "Submission Saved Successfully")
            return redirect('dashboard')
    else:
        form = AddSubmission()
    args = {
        'form': form,
    }
    return render(request, 'submissions/add_submission.html', args)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Registered")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    args = {
        'form': form,
    }
    return render(request, 'submissions/register.html', args)

def add_marks(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        form = AddMarksForm(request.POST)
        if form.is_valid():
            s = form.save(commit=False)
            submission.marks = s.marks
            submission.save()
            messages.success(request, "Added marks")
            return redirect('dashboard')
    else:
        form = AddMarksForm()
    args = {
        'form': AddMarksForm,
        'submission': submission,
    }
    return render(request, 'submissions/add_marks.html', args)
