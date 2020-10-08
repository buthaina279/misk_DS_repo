# Diamond Analysis test
# Buthaina Alshareef
# 1.10.2020

library(tidyverse)

jems2 <- read_csv("data/diamonds.csv")
jems2

summary(jems2)
str(jems2)
glimpse(jems2)
dim(jems2)
names(jems2)
rownames(jems2)
nrow(jems2)

jems2 %>% 
head(5)

jems2 %>% 
  tail(5)
#How many diamonds with a clarity of category “IF” are present in the data-set?
jems2 %>% 
  filter(clarity == "IF") -> clarity_IF
clarity_IF
#What fraction of the total do they represent?
nrow(clarity_IF)/ nrow(jems2)
  
#What proportion of the whole is made up of each category of clarity?
jems2 %>% 
  group_by(clarity) %>% 
  summarise(mean(price))
#What is the cheapest diamond price overall? 

min(jems2$price)

# What is the range of diamond prices?
range(jems2$price)
#What is the average diamond price in each category of cut and color?
jems2 %>% 
  group_by(cut, color) %>% 
  summarise(mean(price))
#Make a scatter plot that shows the price of a diamond as described by another continous variable, like the carat.
#
ggplot(jems2, aes(x= carat, y=price)) + 
  geom_point()
#using the functions we discuss earlier, and in class, apply a log10 transformation to both the price and carat. 

jems3 <- jems2 %>%
  mutate(log10_price = log10(price),
         log10_carat = log10(carat))
ggplot(jems3, aes(x= log10_carat, y=log10_price)) +
  geom_point() +
  geom_smooth(method = "lm")

#remove a column ??
jems2 %>% 
select(-log_price)
jems2$log10_carat
#Make a scatter plot that shows the price of a diamond as described by another continous variable, like the carat.
ggplot(jems2, aes(x= log10_carat, y=log10_price)) + 
  geom_point()

#to recreate a model that describes the relatioship shown in the plot?
jems2_lm <- lm(log10_price  ~  log10_carat, data= jems2)
#Now that we’ve described the diamond price given a single variable, can you display that on the plot? Tryto use the geom_smooth() function to add this new layer.
ggplot(jems2, aes(x= log10_carat, y=log10_price)) + 
  geom_point() +
  geom_smooth(method = "lm")


