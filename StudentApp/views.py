# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from .forms import StudentLogin, SubjectForm, combineform, customuser, UserLogin
# from .models import Subject, combined, CustomUser
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.models import Group
# from StudentApp.filters import UserFilter, SubjectFilter
# from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.views import APIView
# # from django.contrib.auth.decorators import login_required
# # from django.contrib.admin.views.decorators import staff_member_required
# # from django.contrib.auth.decorators import user_passes_test
# # from StudentApp.decorators import staff_required
# from django.shortcuts import get_object_or_404
# from StudentApp.serializers import subjectserializer

# def AdminDashboard(request):
#         user_list = CustomUser.objects.all()
#         subject_list = Subject.objects.all()
#         user_filter = UserFilter(request.GET, queryset=user_list)
#         subject_filter = SubjectFilter(request.GET, queryset=subject_list)
#         stu = CustomUser.objects.all()
#         combi_ned = combined.objects.all()
#         # ---------------------------------------------------------------------
#         # Update form:
#         # ---------------------------------------------------------------------
#         return render(request,'dashboard.html',{'stu':stu,'combi_ned':combi_ned,'user_filter': user_filter,'subject_filter':subject_filter})
#     # -------------------------------------------------------------------------------------------------------
#     #                           Admin User register and login
#     # -------------------------------------------------------------------------------------------------------
# # @user_passes_test(lambda u: u.is_superuser)
# # @moderator_login_required
# def User_Login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             fm = UserLogin(request=request,data=request.POST)
#             # groups = Group.objects.get(name='Admin')
#             if fm.is_valid():
#                 uname = fm.cleaned_data['username']
#                 pwd = fm.cleaned_data['password']
#                 user = authenticate(username=uname,password=pwd)
#                 # group = Group.objects.get(name='Admin')
#                 if user is not None: #and request.user.groups.filter(name='Admin').exists():
#                     messages.info(request, f"You are now logged in as {uname}.")
#                     login(request,user)
#                     # role = user.role
#         #             if user_type == '1':
#         #         return redirect('admin_home')
                
#         #     elif user_type == '2':
#         #         # return HttpResponse("Staff Login")
#         #         return redirect('staff_home')
                
#         #     elif user_type == '3':
#         #         # return HttpResponse("Student Login")
#         #         return redirect('student_home')
#         #     else:
#         #         messages.error(request, "Invalid Login!")
#         #         return redirect('login')
#         # else:
#         #     messages.error(request, "Invalid Login Credentials!")
#         #     #return HttpResponseRedirect("/")
#         #     return redirect('login')
#                     return HttpResponseRedirect('')
#                 else:
#                     messages.error(request,"Invalid username or password.")
#             else:
#                 messages.error(request,"Invalid username or password.")
#         fm = UserLogin()
#         return render(request,'login.html',{'form':fm})
#     else:
#         return HttpResponseRedirect('/dashboard/')

# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/')
# # --------------------------------------------------------------------------
# def AddStudent_User(request):
#     # if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = customuser(request.POST)
#             if form.is_valid():
#                 form.save()
#                 # group = Group.objects.get(name="Student")
#                 # user.groups.add(group)
#                 return HttpResponseRedirect('/')
#         else:
#             form = customuser()
#         return render(request,'Addstudent.html',{'form':form})
#     # else:
#     #     return HttpResponseRedirect('/')

# def AddSubject(request):
#     # if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = SubjectForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect('/')
#         else:
#             form = SubjectForm()
#         return render(request,'Addsubject.html',{'form':form})
#     # else:
#     #     return HttpResponseRedirect('/')

# def combine(request):
#     # if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = combineform(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect('/')
#         else:
#             form = combineform()
#         return render(request,'combine.html',{'form':form})

# # -------------------------     UPDATE using API  -------------------------------------

# class UpdateDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'updateapi.html'
    
#     def get(self, request, id):
#         sub = Subject.objects.get(id=id)
#         serializer = subjectserializer(sub)
#         return Response({'serializer': serializer,'sub':sub})

#     def post(self, request, id):
#             subject = get_object_or_404(Subject, id=id)
#             serializer = subjectserializer(subject, data=request.data)
#             if not serializer.is_valid():
#                 return Response({'serializer': serializer, 'subject': subject})
#             serializer.save()
#             return redirect('/')

# # -------------------------------------- student dashboard --------------------------------------------------------------
# def StudentDashboard(request,id=None):
#     # stud = User.objects.filter(id=id) 
#     # print(stud)
#     combine = get_object_or_404(combined, id=id)
#     stuinfo = combined.objects.all()
#     print(combine)
#     template = 'Stu_dashboard.html'
#     return render(request,template,{'combine': combine,'stuinfo':stuinfo,})
    

# # # @user_passes_test(lambda u: u.is_superuser)
# # # @staff_required
# # def student_login(request):
# #     if request.user.is_authenticated:
# #         if request.method == 'POST':
# #                 fm = StudentLogin(request=request,data=request.POST)
# #                 if fm.is_valid():
# #                     uname = fm.cleaned_data['username']
# #                     pwd = fm.cleaned_data['password']
# #                     user = authenticate(username=uname,password=pwd)
# #                     if user is not None:
# #                         messages.info(request, f"You are now logged in as {uname}.")
# #                         login(request,user)
# #                         return HttpResponseRedirect('/studentdash/')
# #                     else:
# #                         messages.error(request,"Invalid username or password.")
# #                 else:
# #                     messages.error(request,"Invalid username or password.")
# #         fm = StudentLogin()
# #         return render(request,'login.html',{'form':fm})
# #     else:
# #         return HttpResponseRedirect('/studentdash/')

# # def student_logout(request):
# #     logout(request)
# #     return HttpResponseRedirect('/')

# # -------------------------     UPDATE   -------------------------------------
# # def UpdateRecord(request,id):
# #     # if request.user.is_authenticated:
# #         if request.method == 'POST':
# #             sub = Subject.objects.get(id=id)
# #             subject_form = SubjectForm(request.POST, instance=sub)
# #             if subject_form.is_valid():
# #                 subject_form.save()
# #                 # student_form.save()
# #                 # sub = subject_form.save(commit=False)
# #                 # sub.student = student
# #                 # sub.save()
# #                 return HttpResponseRedirect('/')
# #         else:
# #             sub = Subject.objects.get(id=id)
# #             subject_form = SubjectForm(instance=sub)
# #         ''' check for subject id properly before hiting url. LAtest sub url 1
# #         '''
# #         return render(request,'update.html',{'subject_form':subject_form})

