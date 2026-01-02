for note in range(0,21):
    if note < 10:
        print(f"Note {note}: Insuffisant")
    elif note >= 10 and note <= 11:
        print(f"Note {note}: Passable")
    elif note >= 12 and note <= 13:
        print(f"Note {note}: Assez bien")
    elif note >= 14 and note <= 15:
        print(f"Note {note}: Bien")
    elif note >= 16:
        print(f"Note {note}: Très bien")
    
    