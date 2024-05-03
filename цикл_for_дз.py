# д/з

cars_count = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
for i in cars_count:
    print('Я езжу на автомобиле марки ' + i)

cars_count_ = 0

for j in range(len(cars_count)):
    cars_count_ += 10

print("Количество автомобилей увеличено на:", cars_count_)