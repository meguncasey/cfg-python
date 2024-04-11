def calculate_omelettes(boxes_of_eggs, eggs_per_box=6, eggs_per_omelette=4):
    total_eggs = boxes_of_eggs * eggs_per_box
    omelettes = total_eggs // eggs_per_omelette
    return omelettes

def main():
    boxes_of_eggs = int(input("Enter the number of boxes of eggs: "))
    omelettes = calculate_omelettes(boxes_of_eggs)
    print(f"You can make {omelettes} omelettes with {boxes_of_eggs} boxes of eggs.")

if __name__ == "__main__":
    main()
    #scrann