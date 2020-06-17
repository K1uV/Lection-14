my_list = ['pepsi', 'BMW']
def stop_words(func, words:my_list):
    def wrapper():
        func()
        for my_list in create_slogan():
            pass  
    return wrapper


@stop_words
def create_slogan():
    name = input('Input your name: ')
    print(f'{name} drinks pepsi in his new BMW')

create_slogan()