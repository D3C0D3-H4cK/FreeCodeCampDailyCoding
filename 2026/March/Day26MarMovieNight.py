def get_movie_night_cost(day, showtime, number_of_tickets):
    ticket = 0
    hora = int(showtime.split(":")[0])
    minutos_parte = showtime.split(":")[1]
    if "pm" in minutos_parte and hora != 12:
        hora += 12
    elif "am" in minutos_parte and hora == 12:
        hora = 0

    if day in ["Friday", "Saturday", "Sunday"]:
        ticket = 12.00
    elif day in ["Monday", "Wednesday", "Thursday"]:
            ticket = 10.00
    else:
        ticket = 5.00
        
        
    if hora < 17 and day != "Tuesday":
        ticket -= 2
    total = ticket * number_of_tickets    

    print(f"{total:.2f}")
    
get_movie_night_cost("Wednesday", "5:40pm", 3)