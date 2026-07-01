from django import forms
from .models import JobApplication, JobListing  # Add JobListing to the import

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'phone', 'cover_letter', 'resume', 'portfolio_url']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Tell us why you\'re a great fit...'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+1234567890'}),
            'portfolio_url': forms.URLInput(attrs={'placeholder': 'https://github.com/yourusername'}),
        }

# ADD THIS NEW FORM to your existing forms.py
class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'company_name', 'description', 'location', 'salary_range']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-zinc-800 border border-zinc-700 rounded-lg text-white', 'placeholder': 'e.g., Senior Python Developer'}),
            'company_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-zinc-800 border border-zinc-700 rounded-lg text-white', 'placeholder': 'Your Company Name'}),
            'description': forms.Textarea(attrs={'rows': 10, 'class': 'w-full px-4 py-2 bg-zinc-800 border border-zinc-700 rounded-lg text-white', 'placeholder': 'Job description, requirements, benefits...'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-zinc-800 border border-zinc-700 rounded-lg text-white', 'placeholder': 'Remote, New York, London...'}),
            'salary_range': forms.TextInput(attrs={'class': 'w-full px-4 py-2 bg-zinc-800 border border-zinc-700 rounded-lg text-white', 'placeholder': '$50,000 - $80,000'}),
        }

# ============================================================
# NEW EMPLOYER FORMS - Added for authentication & dashboard
# ============================================================

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, EmployerJob, EmployerJobApplication, JobCategory


class CustomUserCreationForm(UserCreationForm):
    """Custom signup form with company name"""
    email = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=200, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'company_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'Choose a username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'your@email.com'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'Create a password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'Confirm your password'
            }),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name']
            )
        return user


class UserProfileForm(forms.ModelForm):
    """Profile edit form for employers"""
    class Meta:
        model = UserProfile
        fields = ['company_name', 'company_website', 'phone', 'bio', 'company_logo']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'Your company name'
            }),
            'company_website': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'https://yourcompany.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': '+1 234 567 890'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'rows': 4,
                'placeholder': 'Tell us about your company...'
            }),
            'company_logo': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-emerald-500 file:text-black file:hover:bg-emerald-600 transition'
            }),
        }


class EmployerJobForm(forms.ModelForm):
    """Form for employers to post jobs"""
    class Meta:
        model = EmployerJob
        fields = [
            'title', 'company_name', 'description', 'location', 
            'salary_range', 'apply_url', 'email_to_receive_applications', 
            'category', 'expires_at'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'e.g., Senior Python Developer'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'Your company name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'rows': 8,
                'placeholder': 'Job description, requirements, benefits...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'Remote, New York, London...'
            }),
            'salary_range': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': '$50,000 - $80,000'
            }),
            'apply_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'https://your-company.com/careers'
            }),
            'email_to_receive_applications': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'hr@yourcompany.com'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500'
            }),
            'expires_at': forms.DateTimeInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition',
                'type': 'datetime-local'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email_to_receive_applications'].required = True
        self.fields['apply_url'].required = False
        self.fields['category'].required = False
        self.fields['expires_at'].required = False


class EmployerJobApplicationForm(forms.ModelForm):
    """Form for applicants to apply to employer jobs"""
    class Meta:
        model = EmployerJobApplication
        fields = [
            'applicant_name', 'applicant_email', 'applicant_phone',
            'cover_letter', 'resume', 'portfolio_url'
        ]
        widgets = {
            'applicant_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'Your full name'
            }),
            'applicant_email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'your@email.com'
            }),
            'applicant_phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': '+1 234 567 890'
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'rows': 6,
                'placeholder': 'Tell us why you\'re a great fit for this role...'
            }),
            'resume': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-emerald-500 file:text-black file:hover:bg-emerald-600 transition'
            }),
            'portfolio_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl text-white focus:outline-none focus:border-emerald-500 transition placeholder-zinc-500',
                'placeholder': 'https://linkedin.com/in/yourprofile'
            }),
        }
