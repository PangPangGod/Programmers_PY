N = int(input())
M = int(input())
lights = list(map(int,input().split()))

if len(lights) == 1:
    height = max(lights[0], N - lights[0])

else:
    height = lights[0]
    for i in range(len(lights)):
        if i == (len(lights) - 1):
            tmp = N - lights[-1]
        else:
            tmp2 = lights[i+1]-lights[i]
            if tmp2 % 2: 
                tmp = (tmp2//2)+1
            else:
                tmp = tmp2//2

        height = max(height, tmp)


print(height)

