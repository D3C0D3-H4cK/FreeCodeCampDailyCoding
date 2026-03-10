def is_valid_trick(trick_name):
    PrimeraPalabra = ["Misty","Ghost","Thunder","Solar","Sky","Phantom","Frozen","Polar"]
    SegundaPalabra =["Twister","Icequake","Avalanche","Vortex","Snowstorm","Frostbite","Blizzard","Shadow"]
    texto = trick_name.split()
    if texto[0] in PrimeraPalabra and texto[1] in SegundaPalabra:
        return True
    else:
        return False

is_valid_trick("Polar Vortex")