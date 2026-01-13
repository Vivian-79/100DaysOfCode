def foo(a, b=4, c=6):
    print(a, b, c)

#foo(1) 1 4 6
#foo(4, 9) 4 9 6
#foo(1, 7, 9) 1 7 9
foo(20, c=6) #20 4 6


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


#bar(1, 2)
bar(toast='nah', spam=4, eggs=2)


def test(*args):
    print(args)


test(1, 2, 3, 5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)