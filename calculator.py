import sys

def calculator(income):
    start_point = 5000
    social_insurance_point =0.08 + 0.02 + 0.005 + 0.06
    tax_part = income*(1-social_insurance_point)-start_point
    if tax_part <= 0:
        tax = 0
    elif 0 < tax_part <= 3000:
         tax = tax_part * 0.03
    elif 3000 < tax_part <=12000:
         tax = tax_part * 0.10 -210
    elif 12000 < tax_part <=25000:
         tax = tax_part *0.20 -1410
    elif 25000 < tax_part <=35000:
         tax = tax_part *0.25-2660
    elif 35000 < tax_part <=55000:
         tax = tax_part *0.30 - 4410
    elif 55000 < tax_part <=8000:
         tax = tax_part*0.35 -7160
    else:
         tax = tax_part*0.4 - 15160
    salary = income*(1-social_insurance_point) - tax
    return '{:.2f}'.format(salary)
def main():
    """对命令行传入的每一个用户，一次调用计算器计算纳税额"""
    for item in sys.argv[1:]:
        ID, income = item.split(':')
        try:
            income = int(income)
        except valueError:
            print('请在薪资的位置输入数字')
            continue
        print('{}:{}'.format(ID,calculator(income)))
if __name__=='__main__':
    main()
