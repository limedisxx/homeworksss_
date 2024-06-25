class InvalidDataException(Exception):
    """Исключение для неверных данных"""
    pass

class ProcessingException(Exception):
    """Исключение для ошибок обработки"""
    pass

def process_data(data):
    if not isinstance(data, (int, float)):
        raise InvalidDataException(f"Неверный тип данных: {type(data)}. Ожидалось int или float.")
    if data < 0:
        raise ProcessingException("Обработка данных невозможна: значение меньше нуля.")
    
    result = data ** 2
    return result

def handle_data(data):
    try:
        result = process_data(data)
        print(f"Результат обработки: {result}")
    except InvalidDataException as e:
        print(f"Ошибка данных: {e}")
        raise  
    except ProcessingException as e:
        print(f"Ошибка обработки: {e}")
        raise  
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        raise  
    else:
        print("Данные обработаны успешно.")
    finally:
        print("Завершение обработки данных.")

data_list = [10, -5, 'abc', 3.5]

for data in data_list:
    try:
        handle_data(data)
    except Exception as e:
        print(f"Ошибка при обработке {data}: {e}")

print("Программа завершена.")