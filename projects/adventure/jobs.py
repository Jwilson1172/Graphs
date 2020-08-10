from multiprocessing import Process, Lock
from player import Player

#def display():
#    print('Hi !! I am Python')


# use of recursive methods would allow for fracturing the map into peices
# that are held by the explorers
def display(my_name):
    print('Hi !!!' + " " + my_name)


#    p = Process(target=display, args=('test', ))
#    p.start()
#    p.join()


# basic multiprocessing demo, next up is going to be locking for the main map
# acess
class mult():
    def __init__(self):
        return

    def cube(self, x):
        """Cubes the members of list x
        """
        if isinstance(x, list):
            print([i**3 for i in x])
            return
        else:
            print(x**3)
            return x**3

    def evenno(self, x):
        print([f"{i} is even" for i in x if i % 2 == 0], sep='\n')
        return


if __name__ == '__main__':
    my_numbers = [3, 4, 5, 6, 7, 8]
    m = mult()

    my_process1 = Process(target=m.cube, args=(my_numbers, ))
    my_process2 = Process(target=m.evenno, args=(my_numbers, ))
    my_process1.start()
    my_process2.start()
    my_process1.join()
    my_process2.join()
    print("Done")
