import json

def main():
    # Input required to calculate loan term later in the document.
    # validation terms: Float for rate. The rest Integers. Last input is an empty line as per challenge document
    while True:
      try:
          Total = int(input("Total amount of loan: "))
          Downpayment = int(input("Total amount of downpayment: "))
          term=int(input('Enter loan term in years: '))
          rate = float(input('input annual interest rate: '))
          input('Please press enter to start')
      except ValueError:
          print("It must be an integer. Please try again.")
          continue
      if Total < Downpayment:
          print("How could the Total be less than the Downpayment? Please input the data again.")
          continue
      if Total < 0 or Downpayment < 0 or rate < 0 or term < 0:
          print("None of the datas must be less than 0. Please input the data again.")
          continue
      else:
          break

    L1 = Loan(Total, Downpayment, rate, term)
    print(L1.totalPayment())

class Loan:
    def __init__(self, total, downpayment, rate, term):
        self.total = total
        self.downpayment = downpayment
        self.rate = rate / (100 * 12)
        self.term = term * 12
        self.principal = self.total - self.downpayment
        self.totalPayment()

    def totalPayment(self):
        # a dictionary is required in order to use json dump later in the file
        payment_json = {}

        monthly_payment = self.principal * ((self.rate * pow(1 + self.rate, self.term)) / (pow(1 + self.rate, self.term) - 1))
        total_payment = monthly_payment * self.term
        total_interest = total_payment - self.principal
        # %.2f rounds the decimal point to the 2 digit.
        payment_json["monthly_payment"] = float('%.2f' % monthly_payment)
        payment_json["total_interest"] = float('%.2f' % total_interest)
        payment_json["total_payment"] = float('%.2f' % total_payment)

        return json.dumps(payment_json)
        
# if the file gets called i.e. python main.py then main will run. Line 3
# otherwise if Loan gets referenced i.e. tests main will not run. Completely bypassing the user inputs
if __name__ == '__main__':
  main()
