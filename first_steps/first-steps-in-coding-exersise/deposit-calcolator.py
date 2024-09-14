deposit_sum=float(input())
time_to=int(input())
year_persent=float(input())
lihva=deposit_sum*(year_persent/100)
lihva_month = lihva/12
suma=deposit_sum+time_to*lihva_month
print(suma)