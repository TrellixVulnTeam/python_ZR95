# def my_tab(a, b=3, c=1):
#     print(a+b+c)
#
# my_tab(1,1,1)
# my_tab(a=2, b=2)
# my_tab(a=2, b=2, c=2)
# my_tab(1)
#
# -------------------------------------------16-apr-2017------------------------Try It Yourself -8-3

# def make_shirt(size, msg):
#     print('the size of shit'+size+'and message sis '+msg)
#
# size = input('input size')
# msg = input('input message')
#
# make_shirt(size, msg)
# make_shirt(msg=msg, size=size)


--------------------------------------------------------------------------------------8.12


def fun_list(*persons):
        print('persons list is')
        # print(persons)
        for person in  persons:
            print(person)

fun_list('taha', 'khan', 'amir')
fun_list('one', 'two', 'three')
fun_list('three', 'two', 'one' )