x <- 5
5+5
5 -> x
x
print (x)
iris
head (iris) #lets you see the beginning couple of lines
tail (iris) #lets you see the last couple of lines
data <- iris #looks like modifiable csv file
iris$Sepal.Length #the $ function takes the column variables and outputs as a list
sl <- iris$Sepal.Length
sl
summary(iris)
summary(iris$Sepal.Length)
#giving a dataframe a csv file: mydata <- read.csv("myfile.csv"), sep = ",", header = T)
#you can even save a dataframe into a csv file: write.csv(iris, "iris_data.csv")
# R by default is in home directory
getwd()
setwd("~/developer/repos/eeb-c177-project")
#how to install packages for homework
# script is reproduceable so want to install packages in console
library(dplyr)
library(ggplot2)
p <- ggplot(data = iris, aes(x=Sepal.Length, y=Sepal.Width))+
  
#pdf("mycoolplot.pdf")
#p
#dev.off()
