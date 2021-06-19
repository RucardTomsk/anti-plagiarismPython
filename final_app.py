def finel(origcoef,trynum,frequency, masName,masLab):
    totaldecency = 0.5              #started decency for everyone
    if origcoef <= 0.5:
        totaldecency = totaldecency - (((origcoef*10*frequency)/trynum)/100)
    else:
        totaldecency = totaldecency + (((origcoef*trynum)/frequency)/100)
    #/////////////////////////////////////////////////////////////////////
    if totaldecency >= 0 and totaldecency < 0.25:
        print("Списал",masName,masLab)
    else:
        if totaldecency >= 0.25 and totaldecency < 0.50:
            print ("Скорее всего списал",masName,masLab)
        else:
            if totaldecency >= 0.50 and totaldecency < 0.75:
                print("Скорее всего не списал",masName,masLab)
            else:
                print("Не списал")
    #///////////////////////////////////////////////////////////////////////
    print(totaldecency)