#Problem
problem = input("Hey, sir/ma'am do you have any technical difficulties phone/laptop/wifi: ").lower()

#Totally reliable and serious solutions
if problem == "phone":
    print("So, Sir you can break your phone and then repair it by yourself, 100% working :)")
elif problem == "laptop" or problem == "computer":
    print("Go study! become an engineer, doctor, plumber and solve it by your own!")
elif problem == "wifi":
    print("Your router is probably dirty, so you can put it in some water! Sir/Ma'am this has never failed")
else:
    print("GO and learn to read, this program only supports 3 devices! So versatile right! :)")
print("Thank you sir/ma'am, we know that you are going to come back here for better tips, take care and bye!")


