# Some variables
st = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
coordinates = [(0, -2), (3, 7), (1, 8)]
numbers = [1, 6, 2, 9, 3, 4, 11]
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
st_numbers = ['43141', '32441', '431', '4154', '43121']
lst = [[11.9, 12.2, 12.9],
       [15.3, 15.1, 15.1],
       [16.3, 16.5, 16.5],
       [17.7, 17.5, 18.1]]
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

# Solutions

task1 = [i for i in range(1, 1001) if i % 17 == 0]

task2 = [i for i in range(1, 1001) if "2" in str(i)]

task3 = [i for i in range(1, 10001) if str(i) == str(i)[::-1]]

task4 = st.count(" ")

task5 = ''.join([letter for letter in st if letter.lower() not in "aeiouy"])

task6 = [el for el in st.split() if len(el) <= 5]

task7 = dict(zip(st.split(), [len(el) for el in st.split()]))

task8 = set(x for x in st if x.isalpha())

task9 = list(map(lambda x: x ** 2, numbers))

task10 = dict(zip([x for x in coordinates if x[1] - 5 * x[0] + 2 == 0],
                  map(lambda x: (x[0] ** 2 + x[1] ** 2) ** (1 / 2),
                      [x for x in coordinates if x[1] - 5 * x[0] + 2 == 0])))

task11 = list(map(lambda x: x ** 2, [i for i in range(2, 28) if i % 2 == 0]))

task12 = max(
    list(map(lambda x: (x[0] ** 2 + x[1] ** 2) ** (1 / 2), [el for el in coordinates if el[0] >= 0 and el[1] >= 0])))

task13 = [(nums_first[i] + nums_second[i], nums_first[i] - nums_second[i]) for i in range(len(nums_first))]

task14 = [str(x) for x in map(lambda x: int(x) ** 2, st_numbers) if x % 2 == 0]

# task15
splitted = [x.split(',') for x in input_str.split('\n')]
task15 = [dict(zip(list(zip(*splitted))[0], list(zip(*splitted))[i])) for i in range(1, len(splitted))]

task16 = [sum(x) for x in zip(*lst)]