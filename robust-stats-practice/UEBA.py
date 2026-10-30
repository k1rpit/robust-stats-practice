import uuid
import random
employee_information = {
    'name': 'alex',
    'id': uuid.uuid4(),
    'list_of_downloaded_file_sizes': [i+random.randint(0,5) for i in range(random.randint(20,25),random.randint(25,30))],
    'blocking': False
}
max_value = 28



def func_UEBA(max_: int,**kwargs,):
    arithmetic_mean_of_downloaded_items = sum(kwargs['list_of_downloaded_file_sizes']) / len(kwargs['list_of_downloaded_file_sizes'])
    if arithmetic_mean_of_downloaded_items >= max_:
        danger = True
    else:
        danger = False
    
    if danger == True:
        kwargs['blocking'] = True
        print('='*50)
        print('айди\t {} \t заблокирован за подозрительную активонсть'.format(kwargs['id']))
        print('='*50)
    return kwargs
func_UEBA(max_=max_value,**employee_information)
