# from math import sqrt

# def triange_ineq(k):
#     def inner(a, b, c):
#         if a+b>c and a+c>b and b+c>a:
#             return k(a, b, c)
#         else: 
#             raise ValueError('З таких сторін побудувати трикутник не вдас')
#     return inner

# def check(q):
#     def inner(a,b,c):
#         if c>0 and b>0 and a>0:
#             function(a,b,c)
#         else: return "Check Error"
#     return inner


# a = check(input('Уведіть сторону а: '))
# b = check(input('Тепер сторону b: '))
# c = check(input('Та сторону с: '))


# @triange_ineq
# def area(a, b, c):
#     p=(a+b+c)/2
#     area=sqrt(p*(p-a)*(p-b)*(p-c))
#     return area
# print(f'Площа трикутника з вашими сторонаи: {area(a,b,c)}')

water_is_wet = True
def decorating(func):
    def check():
        while water_is_wet == True:
            try:
                pages = int(input("\nКількість сторінок має бути кратна 16 та не перевищувати числа 1280. Введіть своє число:  "))
                if pages%16!=0 or pages>1280:
                    print('\nСпробуйте ще раз')
                    continue
                else:
                    reh = func(pages)
                    for number in range(int(pages/16)):
                        print(f'Номери сторінки {number+1}: \n{next(reh)}')
                        choose = False
            except ValueError:
                print("Ще раз")
                continue    
        return 
    return check

@decorating
def pages_sequence(n=0):
    reh_s = int(n/16)
    for fut in range(1, reh_s+1):
        end = int(16*(fut))
        if fut==1:
           start=1
        else:
           start=int((16*(fut-1)) + 1)
        sequence=[]


        for i in range(0,8,2):
            sequence+=[str(end-i),str(start+i)]
            sequence+=[str(start+i+1),str(end-i-1)]       
        yield ', '.join(sequence)

print(pages_sequence())      