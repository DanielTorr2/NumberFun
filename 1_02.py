import numpy



#Goal: Multiply 3^{3}, 9^{3}, 27^{3}

def cube(a):
  return a**3

def multiplyCubes(a, b, c):
  return cube(a)*cube(b)*cube(c)

print(multiplyCubes(3, 9, 27))


#70% of 4mill, 300/month, * 12

def insuranceProfit():
  rate = 300
  pop = 4000000
  insured_pop = pop * 0.7

  profit = insured_pop * rate
  return profit

def yearlyInsuranceProfit():
  return insuranceProfit()*12


print(f"{yearlyInsuranceProfit():,}")
