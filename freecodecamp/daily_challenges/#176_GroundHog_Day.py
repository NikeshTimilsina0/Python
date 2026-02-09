def groundhog_day_prediction(appearance):
    if appearance==True:
        return "Looks like we'll have six more weeks of winter."
    if appearance==False:
        return "It's going to be an early spring."
    if appearance==" ":
         return "No prediction this year."
    if appearance==None:
        return "No prediction this year."
    else:
        return "No prediction this year."
print(groundhog_day_prediction(True))
print(groundhog_day_prediction(False))
print(groundhog_day_prediction(None))
print(groundhog_day_prediction(" "))
print(groundhog_day_prediction("True"))