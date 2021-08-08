import os  
def rename_files():  
   #C:\Users\user\Downloads\Home _ My Site_files
   for count, filename in enumerate(os.listdir(r"C:\Users\user\Downloads\Web_site\iPortfolio\assets\img\portfolio")):  
        ex=filename.split(".")[-1]
        name=''
        if ex !="py":
            name=f"portfolio-{count}."+ex
            dst ="C:\\Users\\user\\Downloads\\Web_site\\iPortfolio\\assets\\img\\portfolio\\" +name
            src ="C:\\Users\\user\\Downloads\\Web_site\\iPortfolio\\assets\\img\\portfolio\\" +filename
            try:
                os.rename(src, dst)
            except FileExistsError:
                print("alreadyy present")
            print("[+]",dst,"\n",src,"\n\t",name,"\n\n\n",)
if __name__ == '__main__':  
    rename_files() 


#portfolio-9.jpg
