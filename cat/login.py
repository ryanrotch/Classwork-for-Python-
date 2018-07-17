def log(username,password):
    print("Enter the login details ",username,password)
    return
print("USERNAME:")
username=str(input())
print("PASSWORD")
password=str(input())

if len(password)<8:
    print("the PASSWORD is too short")
    print("please add more characters")
else:
    print("login successful")
