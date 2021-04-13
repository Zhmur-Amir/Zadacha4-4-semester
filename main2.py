from PIL import Image
from numpy import array
def main(fin,fout):
    try:
        img=Image.open(fin)
    except FileNotFoundError:
        print("Error! Cannot find file...")
        return
    if img.mode!='RGB':
        print("Error! Wrong file format: ",img.mode)
        return
    if img.get_format_mimetype() !='image/bmp':
        print("Error! Wrong file type: ",img.get_format_mimetype())
        return
    
    arr1=array(img)
    print("Old picture shape: ")
    print(arr1.shape)
    res=[]
    res1=[]
    res2=[]
    res3=[]
    for i in range(arr1.shape[0]):
        for j in range(arr1.shape[1]):
            for k in range(3):
                if arr1[i][j][k]!=0:
                    res.append(i)
                    res3.append(arr1[i][j][k]) 
        
    for i in range(arr1.shape[1]):
        for j in range(arr1.shape[0]):
            for k in range(3):
                if arr1[j][i][k]!=0:
                    res2.append(i)
                    res1.append(arr1[j][i][k]) 
    
    print("First right non-zero pixel is ",res1[0]," in column ",res2[0])
    print("First top non-zero pixel is ",res3[0]," in line ",res[0])      
    print("Last left non-zero pixel is ",res1[len(res2)-1]," in column ",res2[len(res2)-1])
    print("Last down non-zero pixel is ",res3[len(res)-1]," in line ",res[len(res)-1])  
    arr2=arr1[res[0]:res[len(res)-1],res2[0]:res2[len(res2)-1]]
    print("New picture shape: ")
    print(arr2.shape)
    img2=Image.fromarray(arr2,img.mode)
    img2.save(fout,format='bmp')
    
    
    
print("Write down input file:")
file1=input()
print("Write down output file:")
file2=input()
main(file1,file2)