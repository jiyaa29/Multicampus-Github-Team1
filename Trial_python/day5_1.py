#get two numbers not a minus, max number's square minus min number's square return the difference between them make a def
def square_diff(a,b):
    if a < 0 or b < 0:
        return "Error"
    else:
        return (max(a,b)**2 - min(a,b)**2)

print(square_diff(8,10))
