#11 __name__(ASpecialVariable) inPython

#File1.py
print("File1 __name__ = %s" %__name__)

if __name__ == "__main__":
    print("File1 being run directly")
else:
    print("File1 being imported")
    

# File2.py
# import File1

print("File2 __name__ = %s" %__name__)

if __name__ == "__main__":
    print("File2 being run directly")
else:
    print("File2 being imported")