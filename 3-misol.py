# 3-misol
from collections import namedtuple
salom = namedtuple('salom',('name, hours_workd, rate'))

ishchi1 = salom(name='Ali', hours_workd=35, rate=3)
ishchi2 = salom(name='Laylo', hours_workd=20,rate=2)
ishchi3 = salom(name='Sardor',hours_workd=38, rate=4)
ishchi4 = salom(name='Dilshod', hours_workd=45, rate=5)
ishchi5 = salom(name='Zarina', hours_workd=15,rate=1)

ishchilar = [ishchi1,ishchi2,ishchi3,ishchi4,ishchi5]
def royxat(ishchilar):
    for i in ishchilar:
        if  salom.hours_workd < 40:
            print('hours_workd*rate*1.5')
        else:
            print('hours_workd*rate')



royxat(ishchi1)

        


   
