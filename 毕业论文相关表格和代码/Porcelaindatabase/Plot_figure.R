rm(list=ls())
setwd("H:/Other_Work/ZXY")
library(RColorBrewer)
library(dplyr)
library(graphics)

Data <- read.table('clipboard')
df <- data.frame(Data)
colnames(df) <- c('group','value')
df <- arrange(df,desc(value))
df <- df[c(2:nrow(df),1),]
df$color <- rev(brewer.pal(nrow(df),'Spectral'))
labs <- paste0(df$group," (",df$value," ",round(df$value/sum(df$value)*100,2),"%)")
pie(df$value,labels = labs,init.angle = 90,col = df$color,border = "black")

rm(list=ls())
library(scatterpie)
Data <- read.table('clipboard')
df <- as.data.frame(lapply(Data[2:nrow(Data),],as.numeric))
colnames(df) <- Data[1,]
radius <- sqrt(df$SUM/pi)
Max_radius<-max(radius)
Bubble_Scale<-0.1
df$radius <- Bubble_Scale * radius/Max_radius

mydata<-df[,c(2:11)]  #数据集构造
Col_Mean<-apply(mydata,2,mean)
Col_Sort<-sort(Col_Mean,index.return=TRUE,decreasing = TRUE)
mydata<-mydata[,c(Col_Sort$ix[2:10],Col_Sort$ix[1])]
x <- c(1,1.5,2,2.2,2.8,3,3.3)
y <- c(1,1.5,2,2.5,3,3.5,4)
mydata2<-data.frame(x,y,radius=df$radius)
mydata2<-cbind(mydata2,mydata)
Legnd_label<-colnames(mydata2)[4:13]
colnames(mydata2)[4:13]<-LETTERS[1:10]

ggplot() + 
  geom_scatterpie(aes(x=x, y=y,r=radius*4), data=mydata2, cols=colnames(mydata2)[4:13],alpha=0.9,size=0.5) +
  scale_fill_manual(values=colorRampPalette(brewer.pal(10,'Spectral'))(10),labels=Legnd_label)+
  geom_scatterpie_legend(mydata2$radius, x=4, y=1, n=10,
                         labeller=function(x) round((4*x* Max_radius/ Bubble_Scale)^2*pi))+
  scale_x_continuous(limits = c(0.5,4.5))+
  scale_y_continuous(limits = c(0.5,4.5))+
  theme(
    axis.title=element_text(size=15,face="plain",color="black"),
    axis.text = element_text(size=13,face="plain",color="black"),
    legend.title=element_text(size=15,face="plain",color="black"),
    legend.text = element_text(size=14,face="plain",color="black")
  )

rm(list=ls())
library(ggplot2)
library(RColorBrewer)
library(reshape2)  
library(plyr)      

Data <- read.table('clipboard')
df <- as.data.frame(lapply(Data[2:nrow(Data),2:ncol(Data)],as.numeric))
df$segment <- Data[2:nrow(Data),1]
colnames(df) <- Data[1,c(2:ncol(Data),1)]

melt_df<-melt(df,id="segment")
segpct<-rowSums(df[,1:6])
for (i in 1:nrow(df)){
  for (j in 1:6){
    df[i,j]<-df[i,j]/segpct[i]*100 
  }
}

segpct<-segpct/sum(segpct)*100
df$xmax <- cumsum(segpct)
df$xmin <- (df$xmax - segpct)

dfm <- melt(df, id = c("segment", "xmin", "xmax"),value.name="percentage")
colnames(dfm)[ncol(dfm)]<-"percentage"

dfm1 <- ddply(dfm, .(segment), transform, ymax = cumsum(percentage))
dfm1 <- ddply(dfm1, .(segment), transform,ymin = ymax - percentage)
dfm1$xtext <- with(dfm1, xmin + (xmax - xmin)/2)
dfm1$ytext <- with(dfm1, ymin + (ymax - ymin)/2)

dfm2<-join(melt_df, dfm1, by = c("segment", "variable"), type = "left", match = "all")

ggplot()+
  geom_rect(aes(ymin = ymin, ymax = ymax, xmin = xmin, xmax = xmax, fill = variable),dfm2,colour = "black") +
  geom_text(aes(x = xtext, y = ytext,  label = value),dfm2 ,size = 4)+
  scale_x_continuous(breaks=seq(0,100,25),limits=c(0,110))+
  theme(panel.background=element_rect(fill="white",colour=NA),
        panel.grid.major = element_line(colour = "grey60",size=.25,linetype ="dotted" ),
        panel.grid.minor = element_line(colour = "grey60",size=.25,linetype ="dotted" ),
        text=element_text(size=15),
        legend.position="none")

rm(list=ls())
library(ggplot2)
Data <- read.table('clipboard')
df <- as.data.frame(lapply(Data[2:nrow(Data),2:ncol(Data)],as.numeric))
df$name <- Data[2:nrow(Data),1]
colnames(df) <- Data[1,c(2:ncol(Data),1)]
df$level <- as.character(df$level)

ggplot(df, aes(x = level, y = value, fill = name, alpha = level)) +
  geom_col(width = 1, color = 'gray90', size = 0.25, position = position_stack()) +
  geom_text(aes(label = name), size = 2.5, position = position_stack(vjust = 0.5)) +
  coord_polar(theta = 'y') +
  scale_alpha_manual(values = c('0' = 0, '1' = 1, '2' = 0.7,'3' = 0.5), guide = F) +
  scale_x_discrete(breaks = NULL) +
  scale_y_continuous(breaks = NULL) +
  labs(x = NULL, y = NULL) +
  theme_minimal()
