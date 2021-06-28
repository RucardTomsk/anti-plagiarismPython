def finel(origcoef,trynum,frequency, masName,masLab,masLE):
    #print(origcoef,trynum,frequency)
    frequency2 = 1 - frequency
    #print(frequency2)
    totaldecency = origcoef-(origcoef*frequency2)
    #totaldecency = 0.5              #started decency for everyone
    #if origcoef <= 0.5:
     #   totaldecency = totaldecency - (((origcoef*10*frequency)/trynum)/100)
    #else:
     #   totaldecency = totaldecency + (((origcoef*trynum)/frequency)/100)
    #/////////////////////////////////////////////////////////////////////

    if origcoef >= 0 and origcoef < 0.25:
        print("Списал",masName,masLab)
        for i in range(0,len(masName)):
            print("Возможные строки списанные у " + masName[i] + " в файле " + masLab[i])
            for g in masLE[i]:
                print(g)
    else:
        if origcoef >= 0.25 and origcoef < 0.65:
            print ("Скорее всего списал",masName,masLab)
            for i in range(0,len(masName)):
                print("Возможные строки списанные у " + masName[i] + " в файле " + masLab[i])
                for g in masLE[i]:
                    print(g)
        else:
            if origcoef >= 0.65 and origcoef < 0.75:
                print("Скорее всего не списал",masName,masLab)
                for i in range(0,len(masName)):
                    print("Возможные строки списанные у " + masName[i] + " в файле " + masLab[i])
                    for g in masLE[i]:
                        print(g)
            else:
                print("Не списал")

    #///////////////////////////////////////////////////////////////////////
    print(origcoef)
    print(totaldecency)