from graph import entry_point, I2N

PROMPT = f'''
What do you want to draw?\n
{''.join(f'{index + 1} - {element}\n' for index,
         element in enumerate(I2N))}
Enter a number:'''

print('''
 __   __                                           __    
|  |_|__.-----.--.--.______.-----.----.---.-.-----|  |--.
|   _|  |     |  |  |______|  _  |   _|  _  |  _  |     |
|____|__|__|__|___  |      |___  |__| |___._|   __|__|__|
              |_____|      |_____|          |__|
''')

index = int(input(PROMPT))
if index < 1 or index > 3:
    raise Exception("Index out of range")


entry_point(index)
