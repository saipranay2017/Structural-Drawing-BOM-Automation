#characters Not to be used in MKD
# N,S,O,I,L

try:
    def check_mkd(mkd):
        i=0
        flag1 = 0
        flag2 = 0
        flag3 = 0
        if "N" in mkd:
            return 0
        if "Lg" in mkd:
            return 0
        if "V1E" in mkd:
            return 0
        if "X" in mkd:
            return 0
        if mkd[i].isnumeric()==True:
            while i<len(mkd) and mkd[i].isnumeric()==True:
                flag1=1
                i = i + 1
                continue
            while i<len(mkd) and mkd[i].isalpha()==True:
                flag2=1
                i = i + 1
                continue
            while i<len(mkd) and mkd[i].isnumeric()==True:
                flag3=1
                i = i + 1
                continue
        if flag1==1 and flag2==1 and flag3==1:
            return 1
        else:
            return 0
   
    def replace_mkd(mkd):
        if ' ' in mkd:
            mkd = mkd.replace(' ','')
        if 'I' in mkd:
            mkd = mkd.replace('I','1')
        if 'i' in mkd:
            mkd = mkd.replace('i','1')
        if 'l' in mkd:
            mkd = mkd.replace('l','1')
        if 'S' in mkd:
            mkd = mkd.replace('S','5')
        if 's' in mkd:
            mkd = mkd.replace('s','5')
        if 'o' in mkd:
            mkd = mkd.replace('o','0')
        if 'O' in mkd:
            mkd = mkd.replace('O','0')
        return mkd
   
    def get_mkd_comma_seperated(mkd,mkd_flag):
        mkd_list = []
        txt = ''
        for i in range(len(mkd)):
            if mkd[i].isalnum()==True:
                txt = txt + mkd[i]
            elif mkd[i]==",":
                txt = replace_mkd(txt)
                mkd_true = check_mkd(txt)
                if mkd_true == 1 or mkd_flag==0:
                    mkd_list.append(txt)
                txt = ''
        txt = replace_mkd(txt)
        mkd_true = check_mkd(txt)
        if mkd_true == 1 or mkd_flag==0:
            mkd_list.append(txt)
        return mkd_list
   
    def get_mkd_to_seperated(mkd,mkd_flag):
        mkd_list = []
        mkd = mkd.replace(' ','')
        mkd = replace_mkd(mkd)
        i = 0
        while mkd[i].isnumeric()==True:
            i = i + 1
        while mkd[i].isalpha()==True:
            i = i + 1
        to_index = mkd.index("T0")
        loop_start_num = int(mkd[i:to_index])
        j = to_index + 2
        while mkd[j].isnumeric()==True:
            j = j + 1
        while mkd[j].isalpha()==True:
            j = j + 1
        loop_end_num = int(mkd[j:])
        for k in range(loop_start_num,loop_end_num+1):
            mkd_list.append(mkd[:i]+str(k))
        return mkd_list
   
    def get_mkd(mkd,mkd_flag):
        mkd_list = []
        mkd = replace_mkd(mkd)
        mkd_true = check_mkd(mkd)
        if mkd_true == 1 or mkd_flag==0:
            mkd_list.append(mkd)
        return mkd_list
   
except Exception as e:
    print("ERROR OCCURED")
    print(e)
    file = open("FileName.txt","r")
    name = file.readline()
    file.close()        
    os.remove(name+'.png')
