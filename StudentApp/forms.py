# from django import forms
# from .models import Subject, combined, CustomUser
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError  

# # ------------------------------------------------------------------------------------------------
# class UpdateSubject(forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = ['Subject_name']

# class UpdateStudent(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name']

# class combineform(forms.ModelForm):
#     class Meta:
#         model = combined
#         fields = ['student','subject','marks']
#         widgets = {
#         'student':forms.Select(attrs={'class':'form-control'}),
#         'subject':forms.Select(attrs={'class':'form-control'}),
#         'marks':forms.TextInput(attrs={'class':'form-control'}),
#         }

# class SubjectForm(forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = ['Subject_name']
#         labels = {'Subject_name':'SubjectName'}

#         widgets = {'Subject_name':forms.TextInput(attrs={'class':'form-control'}),
#         }        
# # --------------------------------------- For Adding Admin User --------------------------------------------------------
# class customuser(forms.ModelForm):  
#     class Meta:
#         model = CustomUser
#         fields = ['role','username','username','email','password']
#         widgets = {
#         'role':forms.Select(attrs={'class':'form-control'}),
#         'username':forms.Select(attrs={'class':'form-control'}),
#         'email':forms.TextInput(attrs={'class':'form-control'}),
#         'password':forms.TextInput(attrs={'class':'form-control'}),
#         }
#     # username = forms.CharField(label='UserName',min_length=5, max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))  
#     # firstname = forms.CharField(label='FirstName',widget=forms.TextInput(attrs={'class':'form-control'}))
#     # lastname = forms.CharField(label='LastName',widget=forms.TextInput(attrs={'class':'form-control'}))  
#     # email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
#     # password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))  
#     # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  

#     # def username_clean(self):  
#     #     username = self.cleaned_data['UserName'].lower()  
#     #     new = User.objects.filter(username = username)  
#     #     if new.count():  
#     #         raise ValidationError("User Already Exist")  
#     #     return username  

#     # def firstname_clean(self):  
#     #     firstname = self.cleaned_data['FirstName'].lower()  
#     #     return firstname  
    
#     # def lastname_clean(self):  
#     #     lastname = self.cleaned_data['LastName'].lower()  
#     #     return lastname  

#     # def email_clean(self):  
#     #     email = self.cleaned_data['Email'].lower()  
#     #     new = User.objects.filter(email=email)  
#     #     if new.count():  
#     #         raise ValidationError(" Email Already Exist")  
#     #     return email  
  
#     # def clean_password2(self):  
#     #     password1 = self.cleaned_data['password1']  
#     #     password2 = self.cleaned_data['password2']  
#     #     if password1 and password2 and password1 != password2:  
#     #         raise ValidationError("Password don't match")  
#     #     return password2  
  
#     # def save(self, commit = True):  
#     #     user = User.objects.create_user(  
#     #         self.cleaned_data['username'],
#     #         first_name=self.cleaned_data['firstname'],
#     #         last_name=self.cleaned_data['lastname'],
#     #         email=self.cleaned_data['email'],
#     #         password = self.cleaned_data['password1'],  
#     #     )  
#     #     return user  

# # --------------------------------- Login for admin ----------------------------------------

# class UserLogin(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
#     password = forms.CharField(label=('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    
# class StudentLogin(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
#     password = forms.CharField(label=('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))