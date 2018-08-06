from multiprocessing import Pool
import os

def copyFileTask(name,oldFolderName,newFolderName):
    fr = open(oldFolderName+'/'+name)
    fw = open(newFolderName+'/'+name,"w")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()

def main():
    oldFolderName = input("请输入文件夹的名字：")
    newFolderName=oldFolderName+"-复件"
    os.mkdir(newFolderName)
    fileNames = os.listdir(oldFolderName)
    pool=Pool(5)
    queue=Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName))
    num = 0
    allNum = len(fileNames)
    while True:
        queue.get()
        num+=1
        copyrate=num/allNum
        print('进度是%.2f%%'%(copyrate*100),end='')
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()