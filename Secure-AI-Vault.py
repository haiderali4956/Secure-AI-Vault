pin=4956
attempts=0
max_attempt=3
balance=1000
while attempts<max_attempt:
 try:
    password= int(input(' apna 4 digit pin batao :'))
    if  password==pin:
        print (' welcome to vault: ')
        break
    else:
        attempts+=1
        remaining_attempts=max_attempt-attempts
        print('wrong pin entered ❌ remaining attempts',remaining_attempts)
 except:
     print(' enter in numbers not in alphabets')
else:
    print('too much wrong attempts calling police !')
if password==pin:
    while True:
        print('-------------------------------------------------------------------------')
        print('🏦 --- SECURE AI VAULT MAIN MENU ---')
        print('1. Check Balance 💸🔥')
        print('2. Deposit Money 💰')
        print('3. Withdraw Money 💳')
        print('4. Exit Vault 🚪')
        print('-------------------------------------------------------------------------')
        
        choice = int(input('Apna operation select karein (1, 2, 3, ya 4): '))
        if choice == 1:
             print('Aapka Current Balance hai: Rs. ',balance,'💸🔥')
        elif choice ==2:
            deposit = int(input('Kitne paise Deposit karne hain? Rs. '))
            if deposit>0:
                balance=deposit + balance
                print('Aapka Naya Balance hai: Rs.',balance )
            else:
                print('wrong ammount entered')
        elif choice ==3:
            withdraw =int(input('Kitne paise Withdraw karne hain? Rs. '))
            if withdraw<balance:
                balance -=withdraw
                print('✅ Transaction Successful! Remaining Balance hai: Rs. ',balance)
            else:
                print('❌ Insufficient Balance! Bhai, itne paise to hain hi nahi!')
        elif choice ==4:
            print('thank you for vising ATM')
            break
