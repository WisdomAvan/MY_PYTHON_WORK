phone_model = print("""NOKIA 3310-CONNECTING PEOPLE...
                        

                          MENU \n""")

phone_menu = int(input(""" 
        press 1 Phone book
        Press 2 Messages
        Press 3 Chat
        Press 4 Call register
        Press 5 Tones
        Press 6 Setting 
        Press 7 Call divert
        Press 8 Games
        Press 9 Calculator
        Press 10 Reminders
        press 11 Clock 
        Press 12 Profoles 
        Press 13 SIM services\n 
        """ ))     


match phone_menu:
    case 1:
        print("Phone book")

        phone_book_menu = int(input("""
            
        Press 1 Search 
        Press 2 Service Nos.
        Press 3 Add name
        Press 4 Erase
        Press 5 Edit
        Press 6 Assign tone
        Press 7 Send b'card
        Press 8 Options
        Press 9 Speed dails
        Press 10 Voice tags\n
            """))
        
        match phone_book_menu:
           case 8: 
                print("Options")
                option_menu = int(input("""
                Press 1 Type of view
                Press 2 Memory status\n
                    """
                         ))                                    

    case 2:
        print("Message")

        message_menu = int(input("""
        Press 1 Write messages
        Press 2 Inbox
        Press 3 Outbox
        Press 4 Picture messages
        Press 5 Templates
        Press 6 Smileys
        Press 7 Message settings
        Press 8 Info service
        Press 9 Voice mailbox number
        Press 10 Service command editor\n

            """))
            
        match message_menu:
           case 7:

                print("Message Settings")

                message_settings_menu = int(input("""
                Press 1 Set 1
                Press 2 Common\n
                    """))

                        
            

    






