# Irrigation analysis
#Buthaina 
# 01.10.2020
#  A small case study 

#

library(tidyverse)
# Begin with wide "messy" format 
irrigation <- read_csv("irrigation_wide.csv")
irrigation
# Examine the data 
glimpse(irrigation)

# what is the total area under irrigation in each year?
irrigation %>% 
  filter(year == 2007) %>% 
  select(ends_with("erica")) %>% 
  sum()
# or select("N. America", "S. America")
irrigation_t

# tidy data
irrigation_t <- irrigation %>% 
pivot_longer(-year, names_to = "region")

# sum by year
irrigation_t %>% 
  group_by(year) %>% 
  summarise(total = sum(value))

irrigation_t %>% 
  group_by(region) %>% 
  summarise(diff = value[year == 2007] - value[year == 1980]) %>% 
arrange(-diff) %>% 
  slice(1)

# proprtional of the differnce between the values of years 
irrigation_t <- irrigation_t %>% 
  arrange(region) %>% 
  group_by(region) %>%
  mutate(rate = c(0, diff(value)/ value[-length(value)]))

#where is it the lowest and highest   

irrigation_t[which.max(irrigation_t$rate),]
irrigation_t[which.min(irrigation_t$rate),]


#with tidyverse the lowest and highest

irrigation_t %>%
  ungroup() %>% 
  slice_max(rate, n = 1)
  
irrigation_t %>%
  ungroup() %>% 
  slice_min(rate, n = 1)

# Data visualisation 
irrigation <- read_csv("irrigation_long.csv")

ggplot(irrigation, aes(x= region, y = area)) +
  geom_point()
  
  
  
