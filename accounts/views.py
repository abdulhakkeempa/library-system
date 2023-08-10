from django.shortcuts import render, redirect
from django.views import View
from .forms import LibraryMemberForm
from .models import User, Member
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_superuser)
def getMembers(request):
    """
        HTTP Request for fetching all the member instances from the database.

        Input: HTTP Request Object

        Return:
            Return Rendered HTML Template

    """
    template_name = "library_members.html"
    members = Member.objects.all()
    context = {}
    context['members'] = members
    return render(request, template_name, context)

@user_passes_test(lambda user: user.is_superuser)
def createMember(request):
    """
        HTTP Request for creating an instance of the Library Member in to the databse.

        Input: HTTP Request Object which contains the POST Data

        Return:
            Return Rendered HTML Template
    """
    form = LibraryMemberForm(request.POST)
    if form.is_valid():
        password = f"{form['full_name'].split()[0].lower()}.{form['date_of_birth'].year}"
        user = User.objects.create_user(email=form['email'], 
                                        full_name=form['full_name'], 
                                        date_of_birth=form['date_of_birth'],
                                        account_type = "Member",
                                        password=password
                                        )
        member = Member.objects.create()
        member.account = user
    else:
        errors = form.errors
        return redirect('library-members', errors=errors)  

    return redirect("library-members", success=True)

@user_passes_test(lambda user: user.is_superuser)
def updateMember(request, pk):
    """"
        HTTP Request for updating an instance of the given primary key along with the url.

        Input:
            Request: HTTP Request Object
            pk: int - Primary Key of the instance to be updated

        Return:
            Return JSON Response
    """
    form = LibraryMemberForm(request.POST)
    if form.is_valid():
        try:
            member = Member.objects.get(id=pk)
            member.account.email = form['email']
            member.account.full_name = form['full_name']
            member.account.date_of_birth = form['date_of_birth']
            member.account.save()
        except IntegrityError as e: 
            error_message =  f"The email address {form['email']} is already in use."
            message = {}
            message['error'] = error_message
            return JsonResponse(message)
        
    message =  f"{member.account.full_name} has been updated successfully."
    message = {}
    message['message'] = error_message
    return JsonResponse(message)

@user_passes_test(lambda user: user.is_superuser)
def deleteMember(request, pk):
    """"
        HTTP Request for deleting an instance of the given primary key along with the url.

        Input:
            Request: HTTP Request Object
            pk: int - Primary Key of the instance to be deleted

        Return:
            Return JSON Response
    """
    member = Member.objects.get(id=pk)
    try:
        member.delete()
    except Exception as error:
        message = {"error": error}
        return JsonResponse(message)
    
    message = {"message": "Member deleted successfully."}
    return JsonResponse(message)

