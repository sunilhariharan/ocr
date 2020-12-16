
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os
import cv2
  

PDF_file = sys.argv[1]
  

outfile = sys.argv[2]

output=sys.argv[3]
  

def ocr(PDF_file,outfile,output):
    f = open(outfile, "a")
    pages = convert_from_path(PDF_file, 500)
    
    for page in pages:
      
        
        filename = "page.png"
        page.save(filename, 'JPEG')
        cv_img=cv2.imread(filename,0)
        
        blur = cv2.GaussianBlur(cv_img,(5,5),0)
        ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imwrite('denoised.png',th3)
        text = str(((pytesseract.image_to_string(Image.open('denoised.png')))))
        text = text.replace('-\n', '')
      
        
        f.write(text)
        
       
        
    f.close()


 


    with open(outfile, "r") as f:
        searchlines = f.readlines()


   


    searchlines= list(map(lambda s: s.strip(),searchlines))


    

    for i in searchlines:
        if i=='':
            searchlines.remove(i)


   


    applicant_details=searchlines[searchlines.index("2. Applicant Details"):searchlines.index("2. Applicant Details")+8]


  

    applicant_name=applicant_details[1:4][0].split('Title')[1]+applicant_details[1:4][1].split('First name')[1]+applicant_details[1:4][2].split('Surname')[1]


    


    applicant_name=applicant_name.strip()


    


    applicant_company_name=applicant_details[4].split('Company name')[1]




    applicant_company_name=applicant_company_name.strip()


    

    applicant_address=applicant_details[5].split('Address line 1 ')[1]+applicant_details[6].split('Address line 2')[1]+applicant_details[7].split('Address line 3')[1]


    

    applicant_address=applicant_address.strip()


    
    subs = 'Description of proposed materials and finishes'

    res = [i for i in searchlines if subs in i]


    l1=[i.split(': ') for i in res]


    l2=[]
    for i in l1:
        l2.append(i[1])

    for i in searchlines:
        if i=='':
            searchlines.remove(i)

    l3=[]
    if l2==[]:
        agent_details=searchlines[searchlines.index("3. Agent Details"):searchlines.index("3. Agent Details")+11]
        agent_name=agent_details[1:4][0].split('Title')[1]+agent_details[1:4][1].split('First name')[1]+agent_details[1:4][2].split('Surname')[1]
        agent_name=agent_name.strip()
        agent_company_name=agent_details[7]
        agent_company_name=agent_company_name.strip()
        agent_address=agent_details[8]+','+agent_details[9]+','+agent_details[10].split('Address line 3')[1]
        agent_address=agent_address.strip()
        l3.append(searchlines[searchlines.index("Walls - Materials"):searchlines.index("Walls - Materials")+8])
        l4=[]
        for i in range(len(l3[0])):
            if i%2==1:
                l4.append(l3[0][i])
        f = open(output, "w")
        f.write("1. Applicant details \n"+"Name : "+applicant_name+'\n'+"Company : "+applicant_company_name+'\n'+"Address : "+applicant_address+'\n'+'\n'+"2. Agent details\n"+"Name : "+agent_name+'\n'+"Company : "+agent_company_name+'\n'+"Address : "+agent_address+'\n'+'\n'+"3.Materials : "+l4[0]+","+l4[1]+","+l4[2]+","+l4[3])
        f.close()
    else:
        agent_details=searchlines[searchlines.index("3. Agent Details"):searchlines.index("3. Agent Details")+8]
        agent_name=agent_details[1:4][0].split('Title')[1]+agent_details[1:4][1].split('First name')[1]+agent_details[1:4][2].split('Surname')[1]
        agent_name=agent_name.strip()
        agent_company_name=agent_details[4].split('Company name')[1]
        agent_company_name=agent_company_name.strip()
        agent_address=agent_details[5].split('Address line 1')[1]+','+agent_details[6].split('Address line 2')[1]+','+agent_details[7].split('Address line 3')[1]
        agent_address=agent_address.strip()
        f = open(output, "w")
        f.write("1. Applicant details \n"+"Name : "+applicant_name+'\n'+"Company : "+applicant_company_name+'\n'+"Address : "+applicant_address+'\n'+'\n'+"2. Agent details\n"+"Name : "+agent_name+'\n'+"Company : "+agent_company_name+'\n'+"Address : "+agent_address+'\n'+'\n'+"3.Materials : "+l2[0]+","+l2[1]+","+l2[2]+","+l2[3])
        f.close()




ocr(PDF_file,outfile,output)


