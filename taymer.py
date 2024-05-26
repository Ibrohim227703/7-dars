class ContextManager1:
    def __init__(self, max_value):
        self.max_value = max_value

    def __enter__(self):
        print("Amal boshlandi")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Amal tugadi")

    def calculate_time_taken(self):
        result = 1
        for i in range(1, self.max_value + 1):
            result *= i
        return result

max_value = 100000

with ContextManager1(max_value) as cm:
    time_taken = cm.calculate_time_taken()
    print(f"Ishni bajarish vaqti: {time_taken}")

##########################


class ContextManager2:
    def __init__(self):
        self.data = {}

    def __enter__(self):
        print("Amal boshlandi")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Amal tugadi")

    def insert_data(self, key, value):
        self.data[key] = value

    def retrieve_data(self):
        return self.data


with ContextManager2() as cm:
    # Ma'lumotlarni kiritamiz.
    cm.insert_data("name", "John")
    cm.insert_data("age", 30)
    cm.insert_data("city", "New York")

    print("Ma'lumotlar:", cm.retrieve_data())
