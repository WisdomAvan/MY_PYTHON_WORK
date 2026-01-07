from datetime import datetime




deposits = []

withdrawals = []

transactions = []

actual_balance = 0

while True:

    print("""
                Welcome To Transaction Log App
                
                1. Deposit
                
                2. Withdrawal

                3. Transaction History

                4. Exit
                   """
   )   

    transaction_menu = int(input("Enter Menu Option By Number: "))

    match transaction_menu:
        
        case 1:
          
            while True:
                print("\nDeposit")

                amount_to_deposit = int(input("\nEnter The Amount To Deposit: "))
                                
                actual_balance += amount_to_deposit

                my_current_date_time = datetime.now().strftime("%d/%m/%y  %I:%M %p")

                deposits.append(f"{amount_to_deposit}, {my_current_date_time} ")

                transactions.append({
                            "Date & Time": my_current_date_time,
                            "Category":"Deposit" , 
                            "Amount":amount_to_deposit, 
                            "Balance":actual_balance
                            } )

                print(f"Your Deposit Of {amount_to_deposit} Was Successful! \nYour Balance Is Now: {actual_balance}\n As At This Time And Date: \n {my_current_date_time}\n")
                                    
                deposit_response = input("Do You Want To Continue With Your Deposit? Yes/No ").casefold()
                                    
                if(deposit_response == "no"):
                    break            
        case 2: 
            
            while True:
                print("\nWithdrawal")

                amount_to_withdraw = int(input("\nEnter The Amount To Withdraw: "))

                my_current_date_time = datetime.now().strftime("%d/%m/%y  %I:%M %p")

                if amount_to_withdraw > actual_balance:
                    print(f"Insufficient Account Balance \n This Is The Actual Balance: {actual_balance}")

                
                else: 
                    actual_balance -= amount_to_withdraw
                    withdrawals.append(f"{amount_to_withdraw},{my_current_date_time}")
                    
                    print(f"Your Withdrawal Of {amount_to_withdraw} Was Successful! \n\nAnd Your Balance Is {actual_balance} \n\nAs At This Time And Date: \n {my_current_date_time}\n")

                    transactions.append({
                                "Date & Time" : my_current_date_time,
                                "Category" :  "withdrawal" , 
                                "Amount" : amount_to_withdraw, 
                                "Balance" : actual_balance
                                })


                withdrawal_response = input("Do You Wish To Continue With Your Withdrawal? Yes/No ").casefold()
                                    
                if(withdrawal_response == "no"):
                    break                
             

        case 3:

                print("\nTransaction History")


                print(f"{'No.':<4} \t{'Date & Time':<20} {'Category':<15} {'Amount':<15} {'Balance':<15} ")
                print("=" * 80)

                for count, transaction in enumerate(transactions, start=1):
                    print(
                        f"{count:<4} "
                        f"{transaction['Date & Time']:<25}"
                        f"{transaction['Category']:<14} "
                        f"{transaction['Amount']:<15,} "
                        f"{transaction['Balance']:<,} "
                        
                    )



        case 4:
            
                print("\nExit")

                if transaction_menu == 4:
                    print("Thank You For Using This App!")
                break


