#!/usr/bin/env python
# coding: utf-8

# # Project: Python Fundamentals
# 
# You're appointed as a Software Developer at a new Development agency, 
# 
# In this project, you'll create software to give your clients financial advice.

# ***
# *** CODE OF CONDUCT: ***
# 
# - You may use online resources for help, but you may not directly copy and paste any answers that are not your own.
# - You may not submit anyone else's work, but your own.
# - Every project will be sent through plagiarism detection software, and compared with every other project in the class.  If you are suspected of plagiarism you will receive zero for the assignment, together with a first disciplinary warning.
# 
# ***
# *** PROJECT RULES: ***
# 
# - You may not import any external packages - all of the functions need to be solved ***WITHOUT THE USE OF EXTERNAL MODULES***.
# - ***Most importantly:*** your functions need to **`return`** the answer (not just print it out).
# - ***Do not add or remove any cells from this notebook***.  Use another notebook to experiment in (or in which to do your workings), but your submission may not have any additional cells or functions. 
# - Only fill in code where the **`#YOUR CODE`**  tags appear. No code outside these areas (or outside the given functions) will be marked.
# 
# 

# ## Function 1:  Savings Calculator
# 
# Build a function **`savings_calculator(PMT, n, i)`**` that calculates your customer's savings at retirement, if they:
# - invest an amount, **`PMT`** at the end of every year (with the first payment in exactly one year's time from now),
# - for **`n` whole years**
# - at an interest rate of **`i`**% per year, compounded annually.

# In[1]:


### START FUNCTION 1

def savings_calculator(PMT, n, i):
    
    ### BEGIN SOLUTION

    # Start by setting the investment_balance equal to zero. We'll increase investment_balance in the for-loop
    investment_balance = 0

    for j in range(n):

        # add the interest earned on our investment account
        interest =  investment_balance * i
        investment_balance = investment_balance + interest

        # at the end of the year we add our bonus to the investment
        investment_balance = investment_balance + PMT

    FV = investment_balance

    ### END SOLUTION

    # Remember to round your answer to 2 decimal places:
    FV = round(FV, 2)

    return FV

### END FUNCTION 1


# ***IMPORTANT***: <br>
# Your function needs to **`return`** an `float` value ***rounded to 2 decimal places***.
# 
# If your answer is not rounded correctly to 2 decimal places, you will receive 0 for the question.
# 
# Make sure that the following tests all give a `True` result:

# In[2]:


savings_calculator(20000, 15, 0.1) == 635449.63


# In[3]:


### BEGIN HIDDEN TESTS
assert(savings_calculator(10000, 20, 0.1) >= 572740)
assert(savings_calculator(10000, 20, 0.1) <= 572755)

assert(savings_calculator(20000, 10, 0.104) >= 324920)
assert(savings_calculator(20000, 10, 0.104) <= 324930)
### END HIDDEN TESTS
savings_calculator(10000, 20, 0.1) == 572749.99


# ## Function 2:  Retirement Savings Calculator
# 
# Build a function **`retirement_savings(PMT, i, start_age, end_age)`** that calculates your customer's savings at retirement, if they:
# - invest an amount, **`PMT`** at the end of every year (with the first payment made in exactly one year's time from now),
# - at an interest rate of **`i`**% per year, compounded annually.
# - They just turned **`start_age`** years old, and 
# - they want to retire at the age of **`end_age`**
# 
# <br><br>
# 
# ***IMPORTANT***: <br>
# Your function **may not call any of the other functions you've defined in this project** (i.e. you may not call `savings_calculator(PMT, n, i)` inside this function)
# 
# You can assume that `start_age` < `end_age`, and both are positive integers.

# In[26]:


### START FUNCTION 2

def retirement_savings(PMT, i, start_age, end_age):

    ### BEGIN SOLUTION

    # Start by setting the investment_balance equal to zero. We'll increase investment_balance in the for-loop
    investment_balance = 0

    for j in range(end_age - start_age):

        # add the interest earned on our investment account
        interest =  investment_balance * i
        investment_balance = investment_balance + interest

        # at the end of the year we add our payment to the investment
        investment_balance = investment_balance + PMT

    FV = investment_balance

    ### END SOLUTION

    # Remember to round your answer to 2 decimal places:
    FV = round(FV, 2)

    return FV

### END FUNCTION 2


# ***IMPORTANT***: <br>
# Your function needs to **`return`** an `float` value ***rounded to 2 decimal places***.
# 
# If your answer is not rounded correctly to 2 decimal places, you will receive 0 for the question.
# 
# Make sure that the following tests all give a `True` result:

# In[27]:


retirement_savings(20000, 0.1, 20, 35) == 635449.63


# In[28]:


### BEGIN HIDDEN TESTS
assert(retirement_savings(20000, 0.1, 20, 35) >= 635445)
assert(retirement_savings(20000, 0.1, 20, 35) <= 635500)

assert(retirement_savings(10000, 0.1, 40, 60) >= 572740)
assert(retirement_savings(10000, 0.1, 40, 60) <= 572760)
### END HIDDEN TESTS
retirement_savings(10000, 0.1, 40, 60) == 572749.99


# ## Function 3:  Retirement Age Calculator
# 
# Build a function **`retirement_age(PMT, i, FV, start_age)`** that calculates the (whole) age at which your customer can retire, if they:
# - invest an amount, **`PMT`** at the END of every YEAR (with the first payment made exactly one year from now),
# - at an interest rate of **`i`**% per year, compounded annually.
# - They require an amount of AT LEAST **`FV`** in order to be able to afford retirement.
# - They just turned **`start_age`** years old.
# 
# <br><br>
# 
# ***IMPORTANT***: <br>
# Your function **may not call any of the other functions you've defined in this project** (i.e. you may not call `savings_calculator(PMT, n, i)` or `retirement_savings(PMT, i, start_age, end_age)` inside this function)
# 
# You can assume that `start_age` is a positive integer.

# In[29]:


### START FUNCTION 3

def retirement_age(PMT, i, FV, start_age):
  
    ### BEGIN SOLUTION

    # Start by setting the investment_balance equal to zero. We'll increase investment_balance in the for-loop
    investment_balance = 0

    age = start_age

    # Stop looping if the balance of the investment fund is more than the funds they require, FV:
    while investment_balance < FV:

        # add the interest earned on our investment account
        interest =  investment_balance * i
        investment_balance = investment_balance + interest

        # at the end of the year we add our payment to the investment
        investment_balance = investment_balance + PMT

        age = age + 1

    ### END SOLUTION

    return int(age)

### END FUNCTION 3


# ***IMPORTANT***: <br>
# Your function needs to **`return`** an **`int`** value ***rounded to 2 decimal places***.
# 
# If your answer is not rounded correctly to 2 decimal places, you will receive 0 for the question.
# 
# Make sure that the following tests all give a `True` result:

# In[30]:


retirement_age(20000, 0.1, 635339.63, 20) == 35


# In[9]:


### BEGIN HIDDEN TESTS
assert(retirement_age(20000, 0.1, 635339.63, 20) == 35)
assert(retirement_age(10000, 0.001, 5.63, 20) == 21)
### END HIDDEN TESTS
retirement_age(10000, 0.1, 572749.99, 40) == 60


# ## Function 4:  Home Loan Affordability Calculator
# 
# Build a function **`maximum_home_loan(PMT, i, n)`** that calculates the maximum home loan that your customer can afford, if they:
# - can afford to pay an amount, **`PMT`** at the END of every YEAR (with the first payment made exactly one year from now),
# - at an interest rate of **`i`**% per year, compounded annually, and
# - pay off the home over a term of **`n`** years.
# 
# <br><br>
# 
# ***IMPORTANT***: <br>
# Your function **may not call any of the other functions you've defined in this project** 
# 
# Calculate the loan as the **present value of the future down-payments on the loan, discounted at an interest rate of i% per year**. (Use the present value of an annuity formula, a.k.a. discounted cash flow valuation - https://www.investopedia.com/walkthrough/corporate-finance/3/discounted-cash-flow/introduction.aspx)

# In[10]:


### START FUNCTION 4

def maximum_home_loan(PMT, i, n):

    ### BEGIN SOLUTION

    # Start by setting the investment_balance equal to zero. We'll increase investment_balance in the for-loop
    total_present_value = 0

    for j in range(n):
        present_value_payment = PMT/((1 + i)**(j+1))
        total_present_value = total_present_value + present_value_payment

    ### END SOLUTION
    
    
    PV = round(total_present_value, 2)
    return PV


### END FUNCTION 4


# ***IMPORTANT***: <br>
# Your function needs to **`return`** an `float` value ***correctly rounded to 2 decimal places***.
# 
# If your answer is not rounded correctly to 2 decimal places, you will receive 0 for the question.
# 
# Make sure that the following tests all give a `True` result:

# In[11]:


maximum_home_loan(15000*12, 0.1045, 30) == 1635153.79


# In[12]:


### BEGIN HIDDEN TESTS
assert(maximum_home_loan(100000, 0.1045, 30) >= 908415)
assert(maximum_home_loan(100000, 0.1045, 30) <= 908425)

assert(maximum_home_loan(150, 0.00001, 30) >= 4400)
assert(maximum_home_loan(150, 0.00001, 30) <= 4550)
### END HIDDEN TESTS
maximum_home_loan(15000*12, 0.1045, 25) == 1578934.73


# ## Function 5:  Home Loan Affordability Calculator
# 
# Build a function **`maximum_home_loan_with_age(PMT, i, start_age)`** that calculates the maximum home loan that your customer can afford, if they:
# - can afford to pay an amount, **`PMT`** at the every year on their birthday (starting from their next birthday),
# - at an interest rate of **`i`**% per year, compounded annually, 
# - they just turned **`n`** years old, and they
# - pay off the loan until they turn **`65 years old`**.  I.e. their last payment is on their 65th birthday.
# 
# <br><br>
# 
# ***IMPORTANT***: <br>
# Your function **may not call any of the other functions you've defined in this project**.
# 
# Assume that **`start_age`** is an `int` value, and **`start_age < 65`**.
# 
# 
# Just like in Function 4, calculate the loan as the **present value of the future down-payments on the loan, discounted at an interest rate of i% per year**. (Use the present value of an annuity formula, a.k.a. discounted cash flow valuation - https://www.investopedia.com/walkthrough/corporate-finance/3/discounted-cash-flow/introduction.aspx)

# In[13]:


### START FUNCTION 5

def maximum_home_loan_with_age(PMT, i, start_age):
  
    ### BEGIN SOLUTION
    # Start by setting the investment_balance equal to zero. We'll increase investment_balance in the for-loop
    total_present_value = 0
    n = 65 - start_age
    
    for j in range(n):
        present_value_payment = PMT/((1 + i)**(j+1))
        total_present_value = total_present_value + present_value_payment

    ### END SOLUTION
    
    
    PV = round(total_present_value, 2)
    return PV

### END FUNCTION 5


# ***IMPORTANT***: <br>
# Your function needs to **`return`** an `float` value ***correctly rounded to 2 decimal places***.
# 
# If your answer is not rounded correctly to 2 decimal places, you will receive 0 for the question.
# 
# Make sure that the following tests all give a `True` result:

# In[14]:


maximum_home_loan_with_age(15000*12, 0.1045, 35)  == 1635153.79


# In[15]:


### BEGIN HIDDEN TESTS
assert(maximum_home_loan_with_age(100000, 0.1045, 30) >= 927400)
assert(maximum_home_loan_with_age(100000, 0.1045, 30) <= 927500)

assert(maximum_home_loan_with_age(150, 0.00001, 30) >= 5240)
assert(maximum_home_loan_with_age(150, 0.00001, 30) <= 5260)
### END HIDDEN TESTS
maximum_home_loan_with_age(15000*12, 0.1045, 40) == 1578934.73


# ## Function 6:  Loan Pay-Off Period Calculator
# 
# Write a function **`pay_off_period(PV, PMT, i)`** that calculates the minimum number of years left until a loan is fully paid off, if:
# - the amount owned on the loan is currently equal to **`PV`**,
# - the loan is repaid at an amount, **`PMT`** at the END of every YEAR (with the first payment exactly 1 year from now),
# - at an interest rate of **`i`**% per year, compounded annually.
# 
# <br><br>
# 
# ***IMPORTANT***: <br>
# Your function **may not call any of the other functions you've defined in this project**.
# 
# 
# Just like in Function 4 and 5, calculate the loan as the **present value of the future down-payments on the loan, discounted at an interest rate of i% per year**. (Use the present value of an annuity formula, a.k.a. discounted cash flow valuation - https://www.investopedia.com/walkthrough/corporate-finance/3/discounted-cash-flow/introduction.aspx)

# In[16]:


### START FUNCTION 6

def pay_off_period(PV, PMT, i):
  
    ### BEGIN SOLUTION
    
    # Start by setting the total_present_value equal to zero. We'll increase investment_balance in the for-loop
    total_present_value = 0

    n = 0
    while total_present_value < PV:
        present_value_payment = PMT/((1 + i)**(n + 1))
        total_present_value = total_present_value + present_value_payment

        n = n + 1

    ### END SOLUTION
    
    
    return int(n)

### END FUNCTION 6


# ***IMPORTANT***: <br>
# Your function needs to **`return`** an **`int`**.
# 
# Make sure that the following tests all give a `True` result:

# In[17]:


pay_off_period(1635153, 15000*12, 0.1045) == 30


# In[18]:


### BEGIN HIDDEN TESTS
assert(pay_off_period(1635153, 15000*12, 0.1045) == 30)
assert(pay_off_period(1635153, 15000*12, 0.05) == 13)
assert(pay_off_period(10, 1, 0.05) >= 15)
### END HIDDEN TESTS
pay_off_period(1578934, 15000*12, 0.1045) == 25


# ## Function 7:  Investment Calculator
# 
# Write a function **`investment(PMT, n, i)`** that calculates your customer's savings at some point in the future, if:
# - an amount  is invested at the END of every year, starting with amount of **`PMT`** at the end of this year,
# - at an interest rate of **`i`**% per year, compounded annually,
# - the investment amount **doubles every second year** (cumulatively).
# 
# <br><br>
# 
# ***IMPORTANT***: <br>
# Your function **may not call any of the other functions you've defined in this project**.

# In[19]:


### START FUNCTION 7

def investment(PMT, n, i):
  
    ### BEGIN SOLUTION


    # Start by setting the investment_balance equal to zero. We'll increase investment_balance in the for-loop
    investment_balance = 0

    # Start by setting the current_investment_amount equal to zero. We'll increase current_investment_amount in the for-loop (for every second year)
    current_investment_amount = PMT

    for j in range(n):

        if (j+1) % 2 == 0:
            current_investment_amount = current_investment_amount*2

        # add the interest earned on our investment account
        interest =  investment_balance * i
        investment_balance = investment_balance + interest

        # at the end of the year we add our bonus to the investment
        investment_balance = investment_balance + current_investment_amount


    ### END SOLUTION
    
    
    return round(investment_balance, 2)

### END FUNCTION 7


# ***IMPORTANT***: <br>
# Your function needs to **`return`** an `float` value ***correctly rounded to 2 decimal places***.
# 
# If your answer is not rounded correctly to 2 decimal places, you will receive 0 for the question.
# 
# Make sure that the following tests all give a `True` result:

# In[56]:


investment(15000, 30, 0.1045) == 1954935238.47


# In[22]:


### BEGIN HIDDEN TESTS
assert(investment(10000, 30, 0.1045) >= 1303290100)
assert(investment(10000, 30, 0.1045) <= 1303290200)


assert(investment(20000, 20, 0.05) >= 69417400)
assert(investment(20000, 20, 0.05) <= 69417500)

assert(investment(1, 20, 0.05) >= 3460)
assert(investment(1, 20, 0.05) <= 3480)
### END HIDDEN TESTS
investment(10000, 40, 0.1045) == 41728281751.16


# In[ ]:




