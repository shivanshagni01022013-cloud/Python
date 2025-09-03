correct_answers = int(input("Enter the questions that you got correct out of 10: "))
total_score = correct_answers*2
if correct_answers>10:
    print("Liar! It was out of 10")
elif correct_answers<0:
    print("OMG! So bad even an ant could do better!!")
else:
    print("You got a score of: "+str(total_score))

