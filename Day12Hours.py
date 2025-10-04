def too_much_screen_time(hours):

    for i in hours:
        if i > 10: 
            return True
    for i in range(len(hours)):
        subList = hours[i:i+3]
        if sum(subList) <= 8:
            return True
        
    if sum(hours) / len(hours) >= 6:
        return True
                
    
        
                        
    return False
                    
            
        
        
        

too_much_screen_time([3, 3, 5, 8, 8, 9, 4])