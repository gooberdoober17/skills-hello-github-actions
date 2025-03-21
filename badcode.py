# This is intentionally bad Python code for scanning purposes

# Global variables everywhere
a = 1
b = 2
c = 3

def foo():
  # No proper naming, poor formatting and no error handling
  x = a+b+c
  for i in range(5):
    if i % 2 == 0:
      x = x + i
    else:
      x = x - i
  print("foo result:", x)

def bar():
  # Repeating code and using bare except
  for j in range(1, 5):
    try:
      # Division by j might be problematic if j is zero (though it's not here)
      r = 100 / j
      print("Result is", r)
    except Exception as e:
      print("Error:", e)

def baz():
  # Very bad style: mixing indentation, no docstring, hardcoding magic numbers
  x=0
  while x<10:
    if x==5:
      print("Halfway there!")
      # unnecessarily complex: reassigning x inside loop
      x = x+2
    else:
      x = x+1
    print("x now", x)
  return x

# Call functions in a messy order
foo()
bar()
y = baz()
print("Final value:", y)

# Unused variables and dead code
z = [i for i in range(10)]
z = sorted(z, reverse=True)
print("Sorted in reverse (unused further):", z)

def unused_function():
  # This function does nothing useful
  for k in range(3):
    print("Loop", k)
  return None

# Forgot to call unused_function(), so it never runs.
