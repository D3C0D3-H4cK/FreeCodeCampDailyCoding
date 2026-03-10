import math
def calculate_start_delays(jump_scores):
    record = max(jump_scores)
    delay = []
    for i in jump_scores:
        delaytotal = record - i
        delayMultiply = delaytotal * 1.5
        delay.append(math.ceil(delayMultiply))
    print(delay)

calculate_start_delays([120, 110, 125])