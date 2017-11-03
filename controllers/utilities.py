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
 checks if a String represents a Fractional or Integral
'''
def isNumber(str):
    if (str[0] == '.' or str[len(str) - 1] == '.'):
        return False
    foundFloatingPoint = False
    for digit in str:
        if not digit.isdigit():
            if (digit == '.'):
                if (foundFloatingPoint):
                    return False
                else:
                    foundFloatingPoint = True
            else:
                return False
    return True

'''
 accepted characters: A-z (case-insensitive), 0-9 and underscores.
 length: 5-32 characters.
'''
def isValidTelegramUsername(string):
    length = len(string)
    validLength = length >= 5 and length <= 32
    if validLength:
        for char in string:
            if not(char.isalpha() or char.isdigit() or char == '_'):
                return False
        return True
    else:
        return False
'''
  tests
'''
def main():
  print(isPaying(-1), isPaying(1), isReceiving(-1), isReceiving(1), getAbsoluteAmount(-1), getAbsoluteAmount(-1))


if __name__ == '__main__':
    main()
