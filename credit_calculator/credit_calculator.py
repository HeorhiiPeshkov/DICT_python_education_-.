# print('Hello user!')
# loan_principal = int(input('Enter the loan principal:\n>'))
# calculation_you_want = input('What do you want to calculate?\ntype "m" – for number of monthly payments,\ntype "p" – for the monthly payment:')
# if calculation_you_want == 'm':
#     monthly_payment = int(input('Enter the monthly payment:\n>'))
#     months_will_take = loan_principal // monthly_payment
#     remaining_amount = loan_principal % monthly_payment
#     if remaining_amount > 0:
#         months_will_take += 1
#     print(f'It will take {months_will_take} months to repay the loan')
# elif calculation_you_want == 'p':
#     monthly_payment = int(input('Enter the monthly payment:\n>'))
#     your_monthly_payment = loan_principal % monthly_payment
#     remaining_amount = loan_principal % monthly_payment
#     if remaining_amount > 0:
#         your_monthly_payment += 1
#     print(f'Your monthly payment = {your_monthly_payment}')

import math
import argparse

def annuity_monthly_payment(principal, periods, interest):
    a = interest / (12 * 100)
    annuity = principal * (a * (1 + a) ** periods) / ((1 + a) ** periods - 1)
    return math.ceil(annuity)


def loan_principal(payment, periods, interest):
    b = interest / (12 * 100)
    principal = payment / ((b * (1 + b) ** periods) / ((1 + b) ** periods - 1))
    return math.floor(principal)


def number_of_month(principal, payment, interest):
    c = interest / (12 * 100)
    d = math.log(payment / (payment - c * principal), 1 + c)
    months = math.ceil(d)
    return months


def differentiated_payments(principal, periods, interest):
    e = interest / (12 * 100)
    total_payment = 0
    for f in range(1, periods + 1):
        diff_payment = math.ceil(principal / periods + e * (principal - principal * (f -1)) / periods)
        print(f'Month {f}: payment is {diff_payment}')
        total_payment += diff_payment
    return total_payment - principal


def main():
    parser = argparse.ArgumentParser(description='Credit Calculator')
    parser.add_argument('--type', choices=['annuity', 'diff'], required = True)
    parser.add_argument('--payment', type=float)
    parser.add_argument('--principal', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float, required=True)
    args = parser.parse_args()
    parameters = [args.payment, args.principal,args.periods, args.interest]
    if any(p is not None and p < 0 for p in parameters):
        print('Incorrect parameters')
        return
    if args.type == 'annuity':
        if args.payment is None:
            payment = annuity_monthly_payment(args.principal, args.periods, args.interest)
            print(f'Your annuity payment = {payment}')
            print(f'Overpayment = {payment * args.periods - args.principal:.0f}')
        elif args.principal is None:
            principal = loan_principal(args.payment, args.periods, args.interest)
            print(f'Your loan principal = {principal}')
            print(f'Overpayment = {args.payment * args.periods - principal:.0f}')
        elif args.periods is None:
            months = number_of_month(args.principal, args.payment, args.interest)
            years, rem_months = divmod(months, 12)
            time_output = []
            if years:
                time_output.append(f"{years} year{'s' if years > 1 else ''}")
            if rem_months:
                time_output.append(f"{rem_months} month{'s' if rem_months > 1 else ''}")
            print(f'It will take {' and '.join(time_output)} to repay this loan')
            print(f'Overpayment = {args.payment * months - args.principal:.0f}')
    elif args.type == 'diff':
        if args.payment is not None:
            print('Incorrect parameters')
            return
        if args.principal is not None and args.periods is not None:
            overpayment = differentiated_payments(args.principal, args.periods, args.interest)
            print(f'Overpayment = {int(overpayment)}')
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')


if __name__ == '__main__':
    main()
