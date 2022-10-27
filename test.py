def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
a = 'h'
print(is_number(a))