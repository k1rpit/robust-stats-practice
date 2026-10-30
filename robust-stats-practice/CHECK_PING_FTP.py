import random
import uuid

id_FTP = uuid.uuid4()

data_ping_FTP = [i+random.randint(55,1000) for i in range(10,120,5)]


def func_information_preparation(*,pings: list) -> tuple:
    max_ping_abnormal = max(pings)
    min_ping_abnormal = min(pings)
    clear_ping_data_FTP = []

    for p in pings:
        if p != max_ping_abnormal and  p != min_ping_abnormal:
            clear_ping_data_FTP.append(p)
        else:
            continue
    return clear_ping_data_FTP,min_ping_abnormal,max_ping_abnormal


data_FTP,min_ping_abnormal,max_ping_abnormal = func_information_preparation(pings=data_ping_FTP)


def func_Single_level_Trimmed_Mean_ping(*,list_: list) ->float:
    return sum(list_) / len(list_)


def func_export_final_telemetry(*,max_data=max_ping_abnormal,min_data=min_ping_abnormal,data=func_Single_level_Trimmed_Mean_ping(list_=data_FTP)):
    print('='*55)
    print('')
    print(f'max ping:\t{max_data=};',end='')
    print(f'min ping:\t{min_data=}.')
    print('')
    print(f'average ping:\t{data:.1f}')
    print('')
    print('')
    print(f'id log:\t{id_FTP}')
    print('='*55)
func_export_final_telemetry()