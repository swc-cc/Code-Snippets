import py

# Fix the output and make it work
print(py.parseJson('{"name":"bob","age":10},{"name": "john", age: "12"}', 'age'))
