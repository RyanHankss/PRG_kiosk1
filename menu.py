# Creating menu with different options for customer


customer = 0
while customer >= 0:
    print '========================='
    print '1. Returning Customer'
    print '2. New Customer'
    print '3. Guest'
    print '========================= \n'

    customer = int(raw_input('Please Select Your Customer Type:  \n'))

    def rcus():
        print '\033[1m' + '\033[4m' + "Here is your information...\n" + '\033[0m'


    def ncus():
        print '\033[1m' + '\033[4m' + "Enter your information...\n" + '\033[0m'


    def guest():
        print '\033[1m' + '\033[4m\n\n' + "          Enjoy the Coffee Kiosk's Complimentary Guest Accommodations \n          and let us know if you have any further questions.\n\n\n" + '\033[0m'


    try:
        if customer < 1 or customer > 3:
            customer = int(raw_input('Please Select Your Customer Type Number 1, 2, or 3:  '))
        elif customer == 1:
            print 'Welcome Back, Returning Customer\n'
            print rcus()
            customer = -1
        elif customer == 2:
            print 'Welcome to the Coffee Kiosk New Customer\n'
            print ncus()
            customer = -1
        elif customer == 3:
            print 'Welcome to the Coffee Kiosk Guest User\n'
            print guest()
            customer = -1
        else:
            print 'Enter Your Customer Type Number, 1, 2, or 3'
    except ValueError:
        print 'Enter Your Customer Type Number, 1, 2, or 3'
