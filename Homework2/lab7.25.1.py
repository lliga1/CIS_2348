#Marianel Liga 
#CIS 2348
#Lab 7.25.1
#Student ID: 1394330

def exact_change(user_total):
    if (user_total <= 0):
        return None
    else:
        num_dollars = user_total // 100
        user_total %= 100

        num_quarters = user_total // 25
        user_total %= 25

        num_dimes = user_total // 10
        user_total %= 10

        num_nickels = user_total // 5
        num_pennies = user_total % 5

        return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)

def main():
    n = int(input())
    res = exact_change(n)
    if(res == None):
        print("no change")
    else:
        num_dollars = res[0]
        num_quarters = res[1]
        num_dimes = res[2]
        num_nickels = res[3]
        num_pennies = res[4]

        if num_dollars > 0:
            if num_dollars == 1:
                print('%d dollar' % num_dollars)
            else:
                print('%d dollars' % num_dollars)

        if num_quarters > 0:
            if num_quarters == 1:
                print('%d quarter' % num_quarters)
            else:
                print('%d quarters' % num_quarters)

        if num_dimes > 0:
            if num_dimes == 1:
                print('%d dime' % num_dimes)
            else:
                print('%d dimes' % num_dimes)

        if num_nickels > 0:
            if num_nickels == 1:
                print('%d nickel' % num_nickels)
            else:
                print('%d nickels' % num_nickels)

        if num_pennies > 0:
            if num_pennies == 1:
                print('%d penny' % num_pennies)
            else:
                print('%d pennies' % num_pennies)

main()