from django.shortcuts import render
from django.views import View
from .forms import LibraryMemberForm
from .models import User, Member
from django.db import IntegrityError
from django.http import JsonResponse

# Create your views here.
class MemberView(View):
    form_class = LibraryMemberForm
    template_name = "library_member.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
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
            return
        else:
            return
        
    def get(self, request):
        members = Member.objects.all()
        context = {}
        context['members'] = members
        return render(request, self.template_name, context)
    
    def put(self,request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                member = Member.objects.get(id=pk)
                member.account.email = form['email']
                member.account.full_name = form['full_name']
                member.account.date_of_birth = form['date_of_birth']
                member.account.save()
            except IntegrityError as e: 
                error_message =  f"The email address {form['email']} is already in use."
                context = {}
                context['error'] = error_message
                return render(request, self.template_name, context)
            
        error_message =  f"The email address {form['email']} is already in use."
        context = {}
        context['error'] = error_message
        return render(request, self.template_name, context)


    def delete(self, request, pk):
        member = Member.objects.get(id=pk)
        member.delete()



def memberDelete(request, pk):
    """"
        HTTP Request for deleting an instance of the given primary key.

        Input:
            Request: HTTP Object
            pk: int - Primary Key

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

