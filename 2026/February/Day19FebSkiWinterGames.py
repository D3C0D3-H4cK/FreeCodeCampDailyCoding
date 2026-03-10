def avalanche_risk(snow_depth, slope):
    if slope != "Gentle" and snow_depth != "Shallow":
        return "Risk"
    else:
        return "Safe"
