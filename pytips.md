# Tips on writing better python code

- Use time.perf_counter() instead of time.time() for timing code
- Use the logging module instead of littering code with print statements for debugging
- Check type with `is` and not `==`
- Make mutable default arguments to a function by first setting them to `None` and then checking if they are `None` in order to set to mutable default. Default arguments are created on function definition and not on function call. If the default arg is set to `[]` in the example below, then every call to the function that changes that list will cause subsequent calls to the function to use the new list, i.e. a second call will use `arg2=[0]`. Instead use the syntax below. 
```python
def some_function( arg1, arg2=None):
    if arg2 is None:
        arg2 = []
    arg2.append(0)
    # the rest of the function..
```
- 