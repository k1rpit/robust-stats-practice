
import random

data_packages_list_SYN = [i+random.randint(10,100) for i in range(50,100)]

def func_to_detect_gap_in_packet_count(*,list_packages: list):
    return max(list_packages) - min(list_packages)


def func_new_clear_list_pack():
    data_packages_clear_SYN = []
    for i in data_packages_list_SYN:
        if i <= 100:
            data_packages_clear_SYN.append(i)
        else:
            continue
    return data_packages_clear_SYN

def func_logging_of_a_new_strict_list(*,new_list):
    print('-'*50)
    print(f'среди списка пакетов/s был найдена угроза DDOS')
    print(f'размах был более 110п/с и было приянто решения очисть список подключений на новый где все будед более безопаснее')
    print('_'*30)
    print(f'список раньше:\t{data_packages_list_SYN}')
    print('='*20)
    print(f'список сейчас(безопаснее):\t{new_list}')
    print('-'*50)

range_min_max = func_to_detect_gap_in_packet_count(list_packages=data_packages_list_SYN)

if range_min_max > 110:
    data_packages_clear_SYN=func_new_clear_list_pack()
    func_logging_of_a_new_strict_list(new_list=data_packages_clear_SYN)