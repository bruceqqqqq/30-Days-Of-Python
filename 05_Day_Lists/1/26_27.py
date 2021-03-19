front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
fullstack = front_end.copy()
fullstack.insert(5, 'Python')
fullstack.insert(6, 'SQL')
print(fullstack)