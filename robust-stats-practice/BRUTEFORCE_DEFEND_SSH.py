import random
import statistics


dangerous_values = float(input('введите опасное значения медианы>>>')) 
bool_SSH_activated = True
data_of_erroneous_inputs_SSH = [i-random.randint(0,2) for i in range(random.randint(1,4),random.randint(5,15))]
data_of_erroneous_inputs_SSH = data_of_erroneous_inputs_SSH[::-1]

median_data = statistics.median(data_of_erroneous_inputs_SSH)


if dangerous_values >= median_data:
    bool_SSH_activated = False
else:
    print('все ок')
print(f'{bool_SSH_activated=}')


