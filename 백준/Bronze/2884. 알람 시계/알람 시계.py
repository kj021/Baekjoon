H,M = input().split()
H= int(H)
M= int(M)
if M>=45:
    print(H,M-45)
elif H==0 and M<45:
    print(23,60-abs(M-45))
elif M<45:
    print(H-1,60-abs(M-45))