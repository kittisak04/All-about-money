 # give total loan
principal = input('principal(float) : ')
# give annual percent interest
percent_interest = input('interest % (float) : ')
# calculate monthly interest rate
monthly_interest = percent_interest/(100 * 12)
# give length of mortgage
years = input('year : ')
# calculate total number of payments
payment_number = years * 12

monthly_payment = principal * ( monthly_interest / (1 - (1 + monthly_interest) ** (- payment_number)))

print "Total loan = $%0.2f" % principal
print "Interest   = %0.2f%s" % (percent_interest, "%")
print "Years      = %0.f" % years
print "Number of payments = %0.f" % payment_number
print "Payment amount     = $%0.2f" % monthly_payment

print "-"*60

print "Total cost     = $%0.2f" % (payment_number * monthly_payment)
print "Total interest = $%0.2f" % (payment_number * monthly_payment - principal)

print "-"*60

# give payments made
payments = 100

rem_principal = principal * (1 - ((1 + monthly_interest) ** payments - 1) / ((1 + monthly_interest) ** payment_number - 1))

print "The outstanding principal after %d payments is $%0.2f" % (payments, rem_principal)
print "At this point you have paid a total of $%0.2f" % (monthly_payment * payments)
