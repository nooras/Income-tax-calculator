from django.shortcuts import render
from .forms import TaxForms
from django.contrib import messages
from django.shortcuts import render 
from .forms import TaxForms

# Create your views here.
def calculate_net(total_income, age, investment_amount):
        if age <= 60:
                if total_income <= 250000:
                        taxable_income = total_income - investment_amount
                        taxable_income = (taxable_income - (taxable_income * .04)) #health and education cess
                        return taxable_income
                # if salary is from Rs.2,50,001 to Rs.5,00,000
                elif total_income >= 250001 and total_income <= 500000:  
                        taxable_income = (total_income - (total_income * .05))  
                        taxable_income = taxable_income - investment_amount  
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income
                # if salary is from Rs.5,00,001 to Rs.10,00,000
                elif total_income >= 500001 and total_income <= 1000000:
                        taxable_income = (total_income - (total_income * .2) - 12500) 
                        taxable_income = taxable_income - investment_amount 
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income
                # if salary if greater that Rs.1000000
                elif total_income > 1000000:
                        taxable_income = (total_income - (total_income * .3) - 112500)  
                        taxable_income = taxable_income - investment_amount 
                        taxable_income = (taxable_income - (taxable_income * .04)) 
                        return taxable_income
        if age > 60 and age <= 80:
                if total_income <= 300000:
                        taxable_income = total_income - investment_amount
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income
                # if salary is from Rs.300001 to Rs.5,00,000
                elif total_income >= 300001 and total_income <= 500000:  
                        taxable_income = (total_income - (total_income * .05))  
                        taxable_income = taxable_income - investment_amount  
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income
                # if salary is from Rs.5,00,001 to Rs.10,00,000
                elif total_income >= 500001 and total_income <= 1000000:
                        taxable_income = (total_income - (total_income * .2) - 10000) 
                        taxable_income = taxable_income - investment_amount 
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income
                # if salary if greater that Rs.1000000
                elif total_income > 1000000:
                        taxable_income = (total_income - (total_income * .3) - 110000)  
                        taxable_income = taxable_income - investment_amount  
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income

        if age > 80:
                if total_income <= 500000:
                        taxable_income = total_income - investment_amount
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income
                # if salary is from Rs.5,00,001 to Rs.10,00,000
                elif total_income >= 500001 and total_income <= 1000000:
                        taxable_income = (total_income - (total_income * .2)) 
                        taxable_income = taxable_income - investment_amount 
                        taxable_income = (taxable_income - (taxable_income * .04))
                        return taxable_income
                # if salary if greater that Rs.1000000
                elif total_income > 1000000:
                        taxable_income = (total_income - (total_income * .3) - 100000)  
                        taxable_income = taxable_income - investment_amount
                        taxable_income = (taxable_income - (taxable_income * .04))  
                        return taxable_income

def tax(income, age):
        if age <= 60:
                if income <= 250000:
                        tax = 0
                        return tax
                # if salary is from Rs.2,50,001 to Rs.5,00,000
                elif income >= 250001 and income <= 500000:  
                        tax = income * .05 
                        return tax
                # if salary is from Rs.5,00,001 to Rs.10,00,000
                elif income >= 500001 and income <= 1000000:
                        tax = (income *  .2) + 12500
                        return tax
                # if salary if greater that Rs.1000000
                elif income > 1000000:
                        tax = (income *  .3) + 112500
                        return tax

        if age > 60 and age <= 80:
                if income <= 300000:
                        tax = 0
                        return tax
                # if salary is from Rs.300001 to Rs.5,00,000
                elif income >= 300001 and income <= 500000:  
                        tax = income * .05
                        return tax

                # if salary is from Rs.5,00,001 to Rs.10,00,000
                elif income >= 500001 and income <= 1000000:
                        tax = income * .2 - 10000
                        return tax
        
                # if salary if greater that Rs.1000000
                elif income > 1000000:
                        tax = income * .3 - 110000
                        return tax

        if age > 80:
                if income <= 500000:
                        tax = 0
                        return tax
                # if salary is from Rs.5,00,001 to Rs.10,00,000
                elif income >= 500001 and income <= 1000000:
                        tax = income * .2
                        return tax
                # if salary if greater that Rs.1000000
                elif income > 1000000:
                        tax = (income * .3 ) - 100000
                        return tax


def tax_view(request):
    form = TaxForms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            income = form.cleaned_data.get("income")
            age = form.cleaned_data.get("age")
            investment_amount = form.cleaned_data.get("investment_amount")
            net_income = calculate_net(int(income), int(age), int(investment_amount))
            #print(net_income)
            taxx = tax(int(income), int(age))
            #print(taxx)
            health_edu = (int(income)-int(investment_amount)) * .04 #health and education cess

            context = {
                    'income' : income,
                    'age' : age,
                    'investment_amount' : investment_amount,
                    'net_income' : net_income,
                    'tax' : taxx,
                    'health_edu' : health_edu,
                    'form' : form
            }
            messages.success(request,f'Tax is calculated')
            return render(request,'home.html',context)

    return render(request,'home.html',{'form': form})

