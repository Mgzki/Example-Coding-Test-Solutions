def fizzBuzz(n):
    # Solution to the fizzbuzz problem
    # Write a program that outputs the string representation of numbers from 1 to n.
    # But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
    for i in range(1,n+1):
        if (not (i/3).is_integer() and not (i/5).is_integer()):
            print(i)
            continue
        elif ((i/5).is_integer() or (i/3).is_integer()):
            if not (i/3).is_integer():
                print('Buzz')
                continue
            elif not (i/5).is_integer():
                print('Fizz')
                continue
            else:
                print('FizzBuzz')
                continue
        
         
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
