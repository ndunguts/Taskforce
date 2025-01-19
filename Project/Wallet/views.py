from django.shortcuts import render, redirect

from .models import Budget ,income,outcome,accounts
from django.utils.timezone import now 
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')
 # Ensure you import your model here

def make_budget(request):
    
    return render(request, 'make_budget.html')
def save(request):
    if request.method == 'POST':
        # Retrieve form data
        time_period = request.POST['time_period']
        money_used = request.POST['money_used']
        account_names = request.POST.getlist('account_names[]')  # Get list of account names

        # Join account names into a comma-separated string
        account_names_str = ', '.join(account_names)

        # Create a new Budget instance
        budget = Budget(time_period=time_period, money_used=money_used, account_names=account_names_str)

        # Save the instance to the database
        budget.save()

        # Redirect to the budget page (or another page)
        return redirect("income")
    
  
def incomes(request):
    current_datetime = datetime.now()
    budgets = Budget.objects.all()

    # Collecting all account names and making sure they are unique
    all_account_names = set()
    for budget in budgets:
        if budget.account_names:
            account_names_list = budget.account_names.split(', ')
            all_account_names.update(account_names_list)

    return render(request, 'income.html', {'budgets': budgets, 'all_account_names': all_account_names ,'current_datetime':current_datetime})

def deletbudget(request):
    return render(request, 'needdeletbudget.html')
def checkbudget(request):
    number_budget=Budget.objects.all().count()
    if number_budget >=1:
        return redirect('deletbudget')
    return redirect('budget')





def saveincome(request):
    if request.method == 'POST':
        amasaha = request.POST['amasaha']
        money = request.POST['money']  # Ensure that money is treated as a number
        selected = request.POST['account']
        impavu = request.POST['impa']
        
        # Fetch the account based on 'selected'
        try:
            account = accounts.objects.get(account_name=selected)  # Get account by name
        except accounts.DoesNotExist:  # Corrected to accounts.DoesNotExist
            # Account doesn't exist, create new income entry and account
            keep = income(amasaha=amasaha, money=money, account=selected, impavu=impavu)
            keep.save()
            zero=0
            
            # Create the account if it doesn't exist
            keep2 = accounts(account_name=selected, money_save=str(money), money_out=zero, money_total=money)
            keep2.save()
            
            return redirect('income')  # Redirect to income page or wherever you want

        # Account exists, process the income
        if account:
            # Create the income entry for the existing account
            keep = income(amasaha=amasaha, money=money, account=account, impavu=impavu)
            keep.save()

            # Calculate the sum of all money_save entries (if it's a list of values)
            
            saved=account.money_save
            saved=int(saved)
            saved += int(money)  # Add the new money value

            # Update account money totals
            total = account.money_total
            totalreal = int(total) + int(money)

            # Update the account's money_save and money_total
            account.money_save = str(saved)
            account.money_total = str(totalreal)
            account.save()

            return redirect('income')  # Redirect to income page or wherever you want
        else:
            return HttpResponse("Account does not exist", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)

def outcomes(request):
    current_datetime = datetime.now()
    budgets = Budget.objects.all()

    # Collecting all account names and making sure they are unique
    all_account_names = set()
    for budget in budgets:
        if budget.account_names:
            account_names_list = budget.account_names.split(', ')
            all_account_names.update(account_names_list)

    return render(request, 'outcome.html', {'budgets': budgets, 'all_account_names': all_account_names ,'current_datetime':current_datetime})

def saveoutcome(request):
    if request.method == 'POST':
        # Get the list of money_used from all Budget entries and sum them up
        table = Budget.objects.all()
        money_saved = sum(budget.money_used for budget in table)  # Sum the 'money_used' values
        
        # Retrieve the POST data
        amasaha = request.POST['amasaha']
        money = int(request.POST['money'])  # Ensure 'money' is treated as a float or decimal
        selected = request.POST['account']
        impavu = request.POST['impa']
        
        # Check if there's enough money saved to cover the expense
        if money_saved >= money:  # This comparison should now work correctly
            change = money_saved - money  # Calculate the remaining money
            
            try:
               account = accounts.objects.get(account_name=selected)  # Get account by name
            except accounts.DoesNotExist:
            # Save the outcome record
               keep = outcome(amasaha=amasaha, money=money, account=selected, impavu=impavu)
               keep.save()
               zero=0
               money=int(money)
               totalfirst=int(zero) - int(money)
               
               
               
               keep2 = accounts(account_name=selected, money_save=zero, money_out=str(money), money_total=totalfirst)
               keep2.save()

            # Update the Budget record (assuming you want to update one specific entry)
               budget_to_update = Budget.objects.first()  # Modify as needed to select the correct Budget object
               budget_to_update.money_used = change
               budget_to_update.save()
               return redirect('success')
            if account:
                keep = outcome(amasaha=amasaha, money=money, account=selected, impavu=impavu)
                keep.save()
                
                
                out=account.money_out
                out=int(out)
                out += int(money)
                
                total = account.money_total
                totalreal = int(total) - int(money)

            # Update the account's money_save and money_total
                account.money_out = str(out)
                account.money_total = str(totalreal)
                account.save()

                return redirect('success')
            
            
        
            


        else:
            return redirect('lostbudget')
            
    
        
def success(request):
    table = Budget.objects.all()
    money_saved = sum(budget.money_used for budget in table)  # Sum the 'money_used' values
    
    return render(request, 'success.html',{'money_saved':money_saved})
def lost_budget(request):
    table = Budget.objects.all()
    money_saved = sum(budget.money_used for budget in table)  # Sum the 'money_used' values
    
    return render(request, 'los_budget.html',{'money_saved':money_saved})    
def chart_total_saved(request):
    account=accounts.objects.all()
    return render(request, 'chart.html',{"account":account})
def highest_outcome(request):
    account=accounts.objects.all()
    return render(request, 'chart_out.html',{"account":account})
def highest_income(request):
    account=accounts.objects.all()
    return render(request, 'chart_income.html',{"account":account})
def report(request):
    saved=income.objects.all()
    send=outcome.objects.all()
    return render(request, 'report.html',{"saved":saved ,"send":send})
def deletebudget(request):
    Budget.objects.all().delete()
    return redirect('budget')
    
#GRANT ALL PRIVILEGES ON wallet.* TO 'giteg'@'localhost';
# CREATE USER 'giteg'@'localhost' IDENTIFIED BY '1234';