from django.shortcuts import render
def mileage(request):
    km = int(request.POST.get('Range', 0))
    lit = int(request.POST.get('Petrol', 0))
    mileage = km / lit if request.method == 'POST' else 0
    print("Range=",km)
    print("Petrol=",lit)
    print("Mileage=",mileage)
    return render(request, 'mathapp/math.html', {'km': km, 'lit': lit, 'mileage': mileage})
