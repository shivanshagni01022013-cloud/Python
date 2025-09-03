# Welcome to Goofy Tech Support Part 2
# This program provides sarcastic or serious tech support in a goofy manner
import time
import os

# Ask user if they want to start the service
start_or_not = input("We appreciate for using our services but do you want to start or not (y/n only) as it costs 10000$: ").lower()

if start_or_not == "y":
    # Ask for username
    username = input("Enter your username: ").lower()

    # Easter egg: if username is 'thanos', simulate the snap
    if username == "thanos":
        print("SNAP! 💥 Half your devices are gone...")
        quit()
    else:
        # Ask for mobile number and validate
        mobile_number = input("Enter your mobile number for future needs: ")
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            print("I see what you are doing. 💀")
            quit()
        else:
            # Ask for credit card number and validate
            credit_card = input("We respectfully ask you to give us your credit card number or else!: ")
            if not credit_card.isdigit() or len(credit_card) != 16:
                print("You think we got no brains, huh!")
                quit()
            else:
                # Ask for mode: sarcastic or serious
                mode = input("Enter which mode you want (sarcastic/serious) Sarcastic is mostly recommended: ").lower()
                
                # --- Sarcastic Mode ---
                if mode == "sarcastic":
                    # Ask which device the user wants support for
                    device = input("Great, perfect choice! Which device do you want (laptop, phone, gaming computer, router, television): ").lower()

                    # Laptop section
                    if device == "laptop":
                        suspicious_details = input("Alrighty! but before we need you to tell your cvv number: ")

                        # CVV validation
                        if not suspicious_details.isdigit() or len(suspicious_details) != 3:
                            print("Like we won't notice it. :(")
                        else:
                            # Ask laptop problem
                            print("Great we totally won't do malicious things! Now to solve laptop's problem we have to ask you what problem you have->")
                            problem_laptop = input("What problem do you have (a-It's not working/b-It's having a virus/c-Or it's broken): ").lower()
                            if problem_laptop == "a":
                                print(f"Well {username}, You can do what is to throw it from a 7th floor and it would fix it, since the laptop wouldn't want it to happen again")
                            elif problem_laptop == "b":
                                print(f"Well {username}, It's quite simple. Like in covid-19 we used sanitizers, you could do the same.")
                            elif problem_laptop == "c":
                                # Dramatic delay effect
                                print(f"Well {username}, What you could do is ...")
                                time.sleep(2)
                                print("...SYSTEM ERROR")
                                time.sleep(1)
                                print("...YOU ARE GOING TO GET HACKED NOW! 💀")
                                time.sleep(1)
                                print("BYE,BYE! 😈")
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print("COME ON, JUST TYPE THE LETTERS IN THE BRACKET!!!")
                                quit()
                        
                    # Phone section
                    elif device == "phone":
                        suspicious_details = input("Alrighty! but before, we need you to tell your cvv number: ")

                        if not suspicious_details.isdigit() or len(suspicious_details) != 3:
                            print("Like we won't notice it. :(")
                        else:
                            # Ask phone problem
                            print("Great we totally won't do malicious things! Now to solve phone's problem we have to ask you what problem you have->")
                            problem_phone = input("What problem are you having? (a-It's not opening;b-It's not charging): ").lower()
                            if problem_phone == "a":
                                print(f"So {username}, It's the most common issue and to fix it, we have to hammer the phone.")
                            elif problem_phone == "b":
                                print(f"Sir {username}, you can just buy a new charger.")
                            else:
                                print("I give up after telling so many times!")
                                quit()
                    
                    # Gaming computer section
                    elif device == "gaming computer":
                        suspicious_details = input("Alrighty! but before, we need you to tell your cvv number: ")

                        if not suspicious_details.isdigit() or len(suspicious_details) != 3:
                            print("Like we won't notice it. :(")
                        else:
                            print("Great we totally won't do malicious things! Now to solve gaming computer's problem we have to ask you what problem you have->")
                            problem_computer = input("What problem are you facing? (a-It's overheating/b-unexpected shutdowns/c-lagging): ").lower()
                            if problem_computer == "a":
                                print(f"Well {username}, these are rookie problems, you can just put it in a fridge.")
                            elif problem_computer == "b":
                                print(f"Well {username}, It's actually good, since it is a time limit so you don't overuse the computer.")
                            elif problem_computer == "c":
                                print("Hey man, sometimes, you just have to deal with it, OK!")
                            else:
                                print("GET OUT NOW! I say to type in the exact phrase in the brackets! >:(")

                    # Router section
                    elif device == "router":
                        suspicious_details = input("Alrighty! but before, we need you to tell your cvv number: ")

                        if not suspicious_details.isdigit() or len(suspicious_details) != 3:
                            print("Like we won't notice it. :(")
                        else:
                            print("Great we totally won't do malicious things! Now to solve router's problem we have to ask you what problem you have->")
                            problem_router = input("What problem do you hav......")
                            quit()

                    # Television section
                    elif device == "television":
                        suspicious_details = input("Alrighty! but before, we need you to tell your cvv number: ")

                        if not suspicious_details.isdigit() or len(suspicious_details) != 3:
                            print("Like we won't notice it. :(")
                        else:
                            print("Great we totally won't do malicious things! Now to solve television's problem we have to ask you what problem you have->")
                            problem_television = input("What problem do you have? (a-It's not opening/b-It's not opening/c-It's not opening): ").lower()
                            if problem_television in ["a", "b", "c"]:
                                print(f"Well {username}, have you tried putting it in rice? :)")
                            else:
                                print("GET OUT NOW! I say to type in the exact phrase in the brackets! >:(")

                    else:
                        print("You have to type the exact device as it is written in the brackets, The capitalization doesn't matter.")

                # --- Serious Mode ---
                elif mode == "serious":
                    # Ask which device for serious support
                    device_serious = input("Not the best, but okay! Which device do you want (laptop, phone, gaming computer, router): ").lower()

                    # Laptop serious support
                    if device_serious == "laptop":
                        print("What problem are you facing")
                        problem_laptop_serious = input("a->It's not opening; b->Display damage; c->Keyboard problems; d->overheating; e->Not charging; f->virus: ").lower()
                        if problem_laptop_serious == "a":
                            print("STEP-1 ->Ensure it is charged. \nSTEP-2 ->Hold power button for atleast 10 seconds. \nSTEP-3 ->If it still doesn't work then please seek authorized advice")
                        elif problem_laptop_serious == "b":
                            print("Don't use it and bring it straight to repair center to avoid further damage")
                        elif problem_laptop_serious == "c":
                            print("STEP-1 ->Restart your computer. \nSTEP-2 ->Check if Num. lock and fn lock is on. \nSTEP-3 ->Check for any water spills and take it to the repair center")
                        elif problem_laptop_serious == "d":
                            print("Common causes: \n-Dust blocking ventilation. \n-Faulty fans. \n-Heavy Background processes. \n-Check for high CPU usage. ")
                        elif problem_laptop_serious == "e":
                            print("See if-> \n-Is the charger plugged to the charging port. \n-Try a different charger. \n-Inspect the charging port for dust or bent pins")
                        elif problem_laptop_serious == "f":
                            print("Running antivirus softwares if the best solution")
                        else:
                            print("We currently only support these many problems with solutions, Sorry!")

                    # Phone serious support
                    elif device_serious == "phone":
                        print("What problem are you facing")
                        problem_phone_serious = input("a->It's not opening; b->Display damage; c->Slow performance; d->overheating; e->Touchscreen not responding; f->Fast battery drain; g->SIM not detected: ").lower()
                        if problem_phone_serious == "a":
                            print("Solution-> \n-Try long pressing the power button. If no response, then seek repair center.")
                        elif problem_phone_serious == "b":
                            print("You can-> \n-Replace the screen. \n-Don't use DIY methods unless if you have an experience. \n-Seek help from repair center.")
                        elif problem_phone_serious == "c":
                            print("Very common-> \n-Clear cache. \nUninstalled used apps. \nRestart Device. \nFactory reset as last report.")
                        elif problem_phone_serious == "d":
                            print("Solution-> \n-Close the background apps. \n-Avoid gaming while charging. \n-Remove case during heat builup. \n-Update software.")
                        elif problem_phone_serious == "e":
                            print("One of the most common problems-> \n-Clean screen with microfiber cloth. \n-Force restart phone. \n-Remove screen protector only if it is causing issues.")
                        elif problem_phone_serious == "f":
                            print("You can-> \n-Check battery usage in settings. \n-Lower screen brightness. \nReplace battery")
                        elif problem_phone_serious == "g":
                            print("Troubleshoot this by-> \n-Removing and reinserting the SIM. \n-Try SIM in another phone. \n-Reset network settings")
                        else:
                            print("We currently only support these many problems with solutions, Sorry!")

                    # Gaming computer serious support
                    elif device_serious == "gaming computer":
                        print("What problem are you facing")
                        problem_gaming_serious = input("a->It's not opening; b->FPS drops and stuttering; c->Slow performance; d->overheating: ").lower()
                        if problem_gaming_serious == "a":
                            print("1. Check your cables. \n2. Test all components.: ")
                        elif problem_gaming_serious == "b":
                            print("1. Check the graphics card. \n2. Repair/Update the drivers. \n3. Close background softwares")
                        elif problem_gaming_serious == "c":
                            print("1. Optimize settings. \n2. Update drivers and hardware. \n3. Check for malware")
                        elif problem_gaming_serious == "d":
                            print("1. Check the cooling system (fan or liquid). \n2. Clean your pc because of dust")
                        else:
                            print("We currently support only these many problems. :(")

                    # Router serious support
                    elif device_serious == "router":
                        print("What problem are you facing")
                        problem_router_serious = input("a->Connectivity issues; b->Security Vulnerabilities; c->Overheating: ").lower()
                        if problem_router_serious == "a":
                            print("1. Restart modem and router. \n2. Ensure device is connected to Wi-fi network.")
                        elif problem_router_serious == "b":
                            print("1. Change default credentials. \n2. Update router firmware. \n3. Enable WPA3 encryption")
                        elif problem_router_serious == "c":
                            print("Ensure proper ventilation, check for dust buildup, and consider firmware updates")
                        else:
                            print("We currently support only these many problems. :(")
                else:
                    # User did not pick a valid mode
                    print("You know you have to pay lifetime's worth of money to use this program. SO TAKE IT SERIOUSLY. >:(")
                    quit()

# User said no to starting
elif start_or_not == "n":
    print("Well, you missed the fun :(")
    quit()

# Invalid input for starting
else:
    print("We kindly suggest to take it seriously as you have to pay again to use it, you have to type 'y' or 'n'")
