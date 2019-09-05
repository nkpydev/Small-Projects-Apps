# ---------------------------------------------------------------------------- #
#
# !Python       :   3.7.3
# Author        :   Nitin K (https://github.com/nkpydev)
# Github        :   https://github.com/nkpydev
# Program       :   CreditCardValidator
# Description   :   This is pratical implementation of Luhn's Algorithm,
#                   which is used to validate CreditCards, SSN nos, IMEI nos
#
# ---------------------------------------------------------------------------- #

def validate(cc_no):
    # Logic: Starting from Rightmost Digit, double every second digit,
    #        If the doubled value is greater than 9, add those units + tens values,
    #        Then add every things, if that
    #        total%10 == 0, then valid, else invalid 
    even_index_sum = 0
    odd_index_sum = 0
    for i in range((len(cc_no)-1),0,-1):
        if i%2 == 0:
            even_index_sum  += cc_no[i]
        else:
            odd_index_value = cc_no[i]*2
            if odd_index_value > 9:
                tens, units = str(odd_index_value)
                odd_index_value = int(tens) + int(units)
                odd_index_sum += odd_index_value
    total = even_index_sum + odd_index_sum
    if total%10 == 0:
        return True
    else:
        return False

def convert(list):
    result = int(''.join(map(str,list)))
    return result

def main():
    cc_input = [int(x) for x in input("\nEnter a Credit Card number to verify:\t")]
    ans = validate(cc_input)
    if ans == True:
        print(f'{convert(cc_input)} is a "valid" credit card number!!')
    else:
        print(f'{convert(cc_input)} is an "invalid" credit card number!!')

if __name__ == "__main__":
    main()