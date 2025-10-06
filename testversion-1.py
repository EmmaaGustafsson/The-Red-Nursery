import matplotlib.pyplot as plt, time

def budget_planner():
    salary = float(input('Min månadslön är: '))
    print('\nHur mycket vill du spara denna månad?')
    save_goal = float(input('Önskad sparmängd: '))

    print('\nHär kan du ange dina inkomster per månad!')

    food = float(input('Ange utgifter för mat: '))
    rent = float(input('Ange utgifter för hyra: '))
    bills = float(input('Ange utgifter för räkningar: '))
    entertainment = float(input('Ange utgifter för nöje: '))
    transport = float(input('Ange utgifter för transport: '))

    total_expenses = (food + rent + bills + entertainment  + transport)

    print(f'\nDina totala utkomster är {total_expenses}.')

    if total_expenses < salary:
        print(f'\nDu har sparat {salary - total_expenses} denna månad!')
    else:
        print('\nDu har överskridit din inkomst denna månad, anpassa dina utgifter för att kunna spara')

    print('\nHar du nått ditt sparmål denna månad?')
    print('\nHämtar data...')
    time.sleep(3)

    if (salary - total_expenses) >= save_goal:
        print('\nDu har nått ditt mål denna månad, bra jobbat!')
    elif (salary - total_expenses) < save_goal:
        print('\nDu har inte nått ditt mål denna månad, anpassa dina utgifter.')

    print('\nHämtar diagram...')
    time.sleep(3)

    categories = ['Mat', 'Hyra', 'Räkningar', 'Nöje', 'Transport']
    values = [food, rent, bills, entertainment, transport]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title('Här är en visuell fördelning av månadens utgifter')
    plt.show()



budget_planner()