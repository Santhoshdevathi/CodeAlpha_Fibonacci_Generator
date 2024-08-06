from django.shortcuts import render

# Create your views here.


def Fibonacci_Gen(request):
    if request.method == 'POST':
        fib = int(request.POST['fib'])
        num1 = 0
        num2 = 1
        series = ''
        for i in range(fib):
            if i == fib-1:
                series = series + (str(num1) + ' ')
            else:    
                series = series + (str(num1) + ', ')
                temp = num1
                num1 = num2
                num2 = temp + num2
        return render(request,'Fibonacci_Generator/Fibonacci_Gen.html',{'series':series})    
    return render(request,'Fibonacci_Generator/Fibonacci_Gen.html',{'series':False})