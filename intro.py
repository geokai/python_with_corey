
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

#student_info('Math', 'Art', name='John', age=22)
student_info(*courses, **info)

