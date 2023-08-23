import os
os.chdir('C:\\Users\\91914\\Desktop\ML\\pantech_sol\\AI_internship\\12_image_classification\\Code\\images\\Joker')
i=1
for file in os.listdir():
    src=file
    dst="0"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

