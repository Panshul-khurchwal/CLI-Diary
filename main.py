import os 
import datetime
import json

path_= "D:/Projects/IOC R&D Projects/Diary Application/Data_Store"
path = "D:/Projects/IOC R&D Projects/Diary Application/Data_Store/Storage.json"
f = None


# class Diary :
#     def loadData(path):
#         f = open(path,"r")
#         data = f.read()
#         data = json.loads(data)
#         f.close()
#         return data 
    



if(os.path.exists(path)):
    print("File Storage exists")
    
else:
    print("File Storage doesn't Exist ! Creating one ...")
    f = open(path,"w")
    f.close()
    
x = datetime.datetime.now()
today = datetime.datetime.now().strftime("%d-%B-%Y")

def multi_line_input():
    print("Enter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return '\n'.join(lines)

while True:
    print(f"""
{"CLI Diary!"}\n{today}\n
{"Enter 1 to add today's diary entry."}
{"Enter 2 to view all diary entries."}
{"Enter 3 to read a specific entry."}
{"Enter 4 to edit a specific entry."}
{"Enter 5 to delete a specific entry."}
{"Enter 6 to export a specific diary entry."}
{"Enter 7 to export all."}
{"Enter 8 to delete all."}

    """)

    answ = input().strip()
    f = open(path,"r")
    data = f.read()
    data = json.loads(data)
    f.close()

    match answ:

        case "1": 
            if today in data:
                print("Entry for today already exists !")
            else:
                data[today] = multi_line_input() 
                # print(data['22-May-2024'])        
                f=open(path,"w")
                json.dump(data,f)
                f.close()

        case "2":
            temp_counter= 0
            print("All available diary entries - ")
            if data == None:
                print("0 entries present!")
            else:
                for x in data:
                    temp_counter = temp_counter + 1
                    print(x)
            print("Total : "+str(temp_counter))
        
        case "3":
            Spec_date = input("Enter the specific date!")
            if Spec_date in data:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+Spec_date+"\n")
                print(data[Spec_date]+"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else: 
                print("Entry not present!")

        case "4":
            
            Spec_date = input("Enter the specific date!")
            if Spec_date in data:
                    
                if(input("Enter A for append and anything else for overwrite !") == "A"):

                    data[Spec_date]  = data[Spec_date]+multi_line_input()
                else:
                    data[Spec_date]  = multi_line_input()

                f=open(path,"w")
                json.dump(data,f)
                f.close()
            else: 
                print("No such entry!")



        case"5":
        
            Spec_date = input("Enter the specific date!")
            if Spec_date in data :
                del data[Spec_date]
                f = open(path,"w")
                json.dump(data,f)
                f.close()
            else: 
                print("No such entry!")
        case"6":
            
            Spec_date = input("Enter the specific date!")
            if os.path.exists(path_+Spec_date):
                print("File exists")
            else:
                if Spec_date in data:
                        
                    g = open(path_+Spec_date+".txt","x")       
                    g.write(data[Spec_date]) 
                    print("File saved at "+path_)

                else :
                    print("No such entry ")

        case"7":
            for x in data:
                print(x)
                if os.path.exists(path_+x+".txt"):
                    
                    print(path_+x+".txt " + "Already exists")
                    
                else:    
                    g = open(path_+x+".txt","x")       
                    g.write(data[x]) 
                    print("File saved at "+path_)

        case"8":
            f=open(path,"w")
            json.dump({},f)
            f.close()

    
    if (input("Enter 1 to continue and 0 to exit !")) == '0':
        print("Bye ..")
        break   