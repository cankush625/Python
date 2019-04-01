class object_counter :
    no_of_objects = 0

    def __init__(self):
        object_counter.no_of_objects+=1

    @staticmethod
    def display_count():
        print(object_counter.no_of_objects)

o1 = object_counter()
o2 = object_counter()

object_counter.display_count()