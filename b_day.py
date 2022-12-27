from datetime import datetime, timedelta


def create_list(file):
    """Функія приймає текстовий файл, з якого сворюється список словників,
    в якому: кожен словник має ключі - це рядок з ім'ям користувача, а значення - це день народження користувача."""
    users = []
   
    with open(file, "r") as file:
        line = file.readlines()
        for item in line:
            d = {}
            item = item.replace('\n', '').replace(' ', '')            
            d["name"] = item.split(",")[0]            
            d["birthdate"] = item.split(",")[1]
            users.append(d)
            # users.append({"name": item.split(",")[0], "birthdate":item.split(",")[1]})

    return users


def sort_bd(list_user: list, current_date: datetime) -> dict:
    """Функія приймає список словників та поточну дату, та повертає словник з ключем - дата народження 
    і значенням - список користувачів"""
    this_year_bd ={}

    for user in list_user:       
        user_bd = datetime.strptime(user["birthdate"], "%Y-%m-%d").date()
        cur_year_bd = user_bd.replace(year=current_date.year)
        if not this_year_bd.get(cur_year_bd):
            this_year_bd[cur_year_bd] = [user["name"]]
        else:
            this_year_bd[cur_year_bd].append(user["name"])

    return this_year_bd


def l_date(start_period, end_period):
    """Функія приймає поточну дату і кінцеву дату, та повертає список дат без року"""
    list_d =[]
    delta = end_period - start_period 
    if delta.days <= 0:
        print("0 days")
    for i in range(delta.days + 1):
        dat = datetime.strftime((start_period + timedelta(i)), "%m-%d")
        list_d.append(dat)

    return list_d
        

def l_day(this_year_bd, l_date):
    """Функія приймає словник з ключем - дата народження
    і значенням - список користувачів та список дат без року з поточної дати по кінцеву дату, 
    та повертає строки: день народження та ім'я користувача у яких день народження припадає з поточної дати по кінцеву"""
    for k, v in this_year_bd.items():        
        date = datetime.strftime(k, "%m-%d")
        if date in l_date:
            print(f'{k.strftime("%A")} : {" ,".join(v)}')
        

def main():
    """Головна функція скрипта"""

    current_date = datetime.now()

    start_period = current_date - timedelta(days=current_date.weekday()) + timedelta(days=0)

    end_period = start_period + timedelta(days=7)

    file = "list_user.txt"
    users_list = create_list(file)
    this_year_bd = sort_bd(users_list, current_date)
    list_date = l_date(start_period, end_period)
    print(f'From {start_period.date()} to {end_period.date()} birthday:')
    l_day(this_year_bd, list_date)


if __name__ == '__main__':
    main()
