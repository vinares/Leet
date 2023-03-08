C = 523
wudu = [C] * 8
for i in range(3):
    wudu[i + 4] = round(wudu[i] * (3/2))
    wudu[i + 1] = round(wudu[i + 4] * (3/4))
wudu[7] = 2 * wudu[0]
wudu[3] = round(wudu[7] * (2/3))
twelve = [C for _ in range(13)]
for i in range(1,13):
    twelve[i] = round(((2 ** (1/12)) ** i) * twelve[0])
twelve8 = [twelve[0],twelve[2],twelve[4],twelve[5],twelve[7],twelve[9],twelve[11],twelve[12]]
print(wudu)
print(twelve8)

import winsound
for i in range(8):
    winsound.Beep(wudu[i],500)
for i in range(8):
    winsound.Beep(twelve8[i],500)