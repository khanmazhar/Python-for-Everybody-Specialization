# Python-for-Everybody-Specialization😎😎

### Course 1: Week 7 Assignment on Loops and Iterations✔✔
#### The block of code take a series of inputs until the user enters done, and returs the maximum and minimum value👏
```python
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    try:
        c_num = int(num)
    except:
        print("Invalid input")
    
    if largest is None:
        largest = c_num
    elif largest < c_num:
        largest = c_num
        
    if smallest is None:
        smallest = c_num
    elif smallest > c_num:
        smallest = c_num

print("Maximum is", largest)
print("Minimum is", smallest)
```
# Course 1 Completed🎇🎇🎇🎉✨
## [Certificate](https://www.coursera.org/account/accomplishments/certificate/749P7DJBSVTZ)
