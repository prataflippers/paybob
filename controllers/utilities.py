import math

'''
  isReceiving returns true if a transaction was a return
  Integer transactionAmount
'''
def isReceiving(transactionAmount):
  if transactionAmount == 0:
    return None # should not happen
  else: 
    return transactionAmount > 0

'''
  isPaying returns true is a transaction was a payment
  Integer transactionAmount
'''
def isPaying(transactionAmount):
  if transactionAmount == 0:
    return None # should not happen
  return transactionAmount < 0

'''
  getAbsoluteAmount returns the absolute value of a relative transaction amount
  Integer transactionAmount
'''
def getAbsoluteAmount(transactionAmount):
  return math.fabs(transactionAmount)

'''
  tests
'''
def main():
  print(isPaying(-1), isPaying(1), isReceiving(-1), isReceiving(1), getAbsoluteAmount(-1), getAbsoluteAmount(-1))


if __name__ == '__main__':
    main()
