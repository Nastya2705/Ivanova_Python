time = int(input("Enter time in seconds: "))
seconds = time%60
minute = (time//60)-60
hour = (time//60)
print (f"Time:{hour//60}:{minute%60}:{seconds}")

