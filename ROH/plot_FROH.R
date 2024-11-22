library(ggplot2)
library(tidyverse)

##load table
data <- read.table("FROH.txt", header=T)
data

plot<-ggplot(data,aes(ind, ROH, fill=pop)) +
  geom_bar(stat = "identity", position = "dodge") +
  theme_classic() +
  xlab("Pops") +
  ylab("FROH") +
  coord_flip(ylim=c(0,100))

plot
