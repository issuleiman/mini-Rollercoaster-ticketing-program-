print("""""
               .__                                  __             __  .__                                                
__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|  |__   ____                                      
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |  \_/ __ \                                     
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |   Y  \  ___/                                     
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |___|  /\___  >                                    
             \/          \/            \/     \/                            \/     \/                                     
             .__                  __________       .__  .__                                             __                
  ________ __|  |   ____ ___  ___ \______   \ ____ |  | |  |   ___________   ____  _________    _______/  |_  ___________ 
 /  ___/  |  \  | _/ __ \\  \/  /  |       _//  _ \|  | |  | _/ __ \_  __ \_/ ___\/  _ \__  \  /  ___/\   __\/ __ \_  __ \
 \___ \|  |  /  |_\  ___/ >    <   |    |   (  <_> )  |_|  |_\  ___/|  | \/\  \__(  <_> ) __ \_\___ \  |  | \  ___/|  | \/
/____  >____/|____/\___  >__/\_ \  |____|_  /\____/|____/____/\___  >__|    \___  >____(____  /____  > |__|  \___  >__|   
     \/                \/      \/         \/                      \/            \/          \/     \/            \/       
""")
height= float(input("what is your height in cm ?:"))

bill=0


if height >= 120:
    print("You can ride")
    age = int(input("What is your age ? :"))
    if age <=12:
        bill=5
        print(f"child tickets are ${bill}")
    elif age <=18:
        bill=8
        print(f"youth ticket are ${bill}")
    else:
        bill=12
        print(f"Adult ticket are ${bill}")

    pic = input("Will your like a picuture?, Y OR N: ")
    if pic == 'Y':
        print(f"Your total Bill is: ${bill + 3}")


    print(f"Your total Bill is ${bill} , you pay normal price without picture")


else:
    print("Sorry your are not eligible to buy a ticket")





