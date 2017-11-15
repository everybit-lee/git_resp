library("igraph")

rootpath = "E:\\TeamAnalyse\\data2\\en\\5\\"
files = list.files(rootpath) 
for(i in 1:length(files)){
  filename = paste(rootpath,files[i],sep="")
  mydata = read.table(filename,header = FALSE,sep = "\t")
  
  g1 = graph.data.frame(mydata,directed = FALSE)
  
  ##获得
  gnc= walktrap.community(g1,weights =mydata[,3],steps=3) 
  
  #表示形式，显示每一个成员属于的团队
  #freList 按顺序1,2,3.. show the fre of the team
  freList = table(gnc$membership)
  len = length(V(g1))
  
##  filter   
  for(i in 1:len){
    
    group = gnc$membership[i]
    if(freList[group]<=5){
      #ve = as.character(V(g1)$name[i])
      ve = as.numeric(V(g1)$name[i])
      tempc=NULL
      remove1= which(mydata[,1]==ve)
      remove2= which(mydata[,2]==ve)
      tempc=c(remove1,remove2)
      
      if(length(tempc)>0){
        mydata = mydata[-tempc,]
      }
      
    }
  }
## filter end
  
  g1 = graph.data.frame(mydata,directed = FALSE)
  gnc= walktrap.community(g1,weights =mydata[,3],steps=3) 
  
  ## 生成文件 
  newpath=gsub(pattern = ".txt", replacement = "", x = filename)
  
  dir.create(newpath)
  
  degreePath=paste(newpath,"\\degree.txt",sep="")
  membershipPath=paste(newpath,"\\membership.txt",sep="")
  write.table(degree(g1),file=degreePath)
  write.table(gnc$membership,file=membershipPath)
  
}
