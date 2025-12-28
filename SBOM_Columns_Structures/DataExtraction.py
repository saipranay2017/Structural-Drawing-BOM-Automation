from ColumnDetails import ColumnDetails
import InsertIntoExcel

def replace_characters(text):
    text = text.replace(' ','')
    if 'O' in text:
        text = text.replace('O','0')
    if 'o' in text:
        text = text.replace('o','0')
    if 'i' in text:
        text = text.replace('i','1')
    if 'l' in text:
        text = text.replace('l','1')
    if 'x' in text:
        text = text.replace('x','X')
    if 's' in text:
        text = text.replace('s','5')
    return text

def replace_temp_characters(text):
    if 'I' in text:
        text = text.replace('I','1')
    if 'S' in text:
        text = text.replace('S','5')
    return text

def plate_data_formatting(text):
    #print("Text Plate data formatting:",text)
    l = []
    description = ''
    plate_index = text.index("PLATE")
    columndetails = ColumnDetails()
    description = description + text[:plate_index+5]
    #print(description)
    if description[plate_index - 1] != " ":
        description = description[:plate_index] + " " + "PLATE"
    #print(description)
    columndetails.set_description(description)
    text = replace_characters(text)
    thk_start_index = text.index("THK") 
    thk_end_index = thk_start_index + 3
    temp_index = thk_start_index
    while text[temp_index]!="X":
        temp_index = temp_index - 1
    columndetails.set_section(text[temp_index+1:thk_end_index])   
    plate_index_new = text.index("PLATE") + 5
    columndetails.set_length(text[plate_index_new:temp_index]) 
    text = replace_temp_characters(text)
    no_index = text.index("N0")
    while text[thk_end_index].isnumeric()==False:
        thk_end_index = thk_end_index + 1
    columndetails.set_quantity(int(text[thk_end_index:no_index]))
    l.append(columndetails)
    #for k in range(len(l)):
        #print("Description:",l[k].get_description())
        #print("Section:",l[k].get_section())
        #print("Length:",l[k].get_length())
        #print("Quantity:",l[k].get_quantity())
    InsertIntoExcel.insert_cleat_details_into_excel(l)
    return l

def data_formatting(text):
    l = []
    text = replace_characters(text)   
    #print(text)
    temp = ''
    for i in range(len(text)):
        temp = temp + text[i]
        if "WEBCLEAT" in temp:
            columndetails = ColumnDetails()
            columndetails.set_description("WEB CLEAT")
            temp = ''
        if "SEATCLEAT" in temp:
            columndetails = ColumnDetails()
            columndetails.set_description("SEAT CLEAT")
            temp = ''
        if "C0LUMN" in temp:
            columndetails = ColumnDetails()
            columndetails.set_description("COLUMN")
            temp = ''
        if "ISMB" in temp:
            if "N0" in temp or "N0" in temp:
                x_index = temp.index("X")
                columndetails.set_section(temp[:x_index])
                if "LG" in temp:
                    lg_index = temp.index("LG")
                elif "Lg" in temp:
                    lg_index = temp.index("Lg")
                columndetails.set_length(int(temp[x_index+1:lg_index]))
                lg_index = lg_index + 2
                no_index = temp.index("N0")
                temp = replace_temp_characters(temp)
                while temp[lg_index].isnumeric()==False:
                    lg_index = lg_index + 1
                columndetails.set_quantity(int(temp[lg_index:no_index]))
                temp = '' 
                l.append(columndetails)
        if "ISA" in temp:
            if "N0" in temp or "N0" in temp:
                thk_index = temp.index("THK")
                columndetails.set_section(temp[:thk_index])
                if "LG" in temp:
                    lg_index = temp.index("LG")
                elif "Lg" in temp:
                    lg_index = temp.index("Lg")
                thk_index = thk_index + 3
                if temp[thk_index] == "X":
                    thk_index = thk_index + 1
                columndetails.set_length(int(temp[thk_index:lg_index]))
                lg_index = lg_index + 2
                no_index = temp.index("N0")
                temp = replace_temp_characters(temp)
                while temp[lg_index].isnumeric()==False:
                    lg_index = lg_index + 1
                columndetails.set_quantity(int(temp[lg_index:no_index])) 
                l.append(columndetails)
                temp = ''
    #for k in range(len(l)):
        #print("Description:",l[k].get_description())
        #print("Section:",l[k].get_section())
        #print("Length:",l[k].get_length())
        #print("Quantity:",l[k].get_quantity())
    InsertIntoExcel.insert_cleat_details_into_excel(l)
    return l












# WEB CLEATISA 100 X 100 X 8THKX200 LGX 2NOSSEAT CLEATISMB 300 X 250 LG.X 2NOS