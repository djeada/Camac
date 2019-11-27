import random


expected_result = 'lezy jerzy na wiezy'
random_string = ' '*len(expected_result)

trial = 0
while random_string != expected_result:
    for i in range(len(random_string)):
        if random.randint(1,2) % 2 == 0:
            random_string = random_string[:i]+chr(random.randint(65,90))+random_string[i+1:]
        else:
            random_string = random_string[:i]+chr(random.randint(97,122))+random_string[i+1:]

        trial += 1
        print('Trial number: ', trial)
        print(random_string)
