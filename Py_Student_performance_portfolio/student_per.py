#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# %%
students = pd.read_csv("data/StudentsPerformance.csv")
students.columns = students.columns.str.replace(' ', '_')

#%%
students.head()

# %%
students.columns
# %%
# %%
students_index = students.reset_index() 
students_t = students_index.melt(id_vars= ['index', 'gender', 'race/ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course'], 
              value_vars=['math_score', 'reading_score', 'writing_score'],
              var_name='sbj_name', value_name='scores')

students_t
#%%
students_t.columns
# %%
#test 
students_t.loc[students_t['index'] == 3]

#%%

def group_range_mean(data, g1, g2, col):
    low = min(data.groupby([g1,g2])[col].mean())
    high = max(data.groupby([g1,g2])[col].mean())
    return low, high

#%%

def group_mean_std_median(data, g1, g2, col):
    avg = data.groupby([g1,g2])[col].mean()
    stdv = data.groupby([g1,g2])[col].std()
    med  = students_t.groupby([g1,g2])[col].median()
    
    return avg, stdv, med


#%%
# Descriptive statistics 
students_t.groupby(['gender','sbj_name'])['scores'].describe()



""" 
df['maths_pass']=np.where(df['math score']<40,'Fail','Pass')
df['reading_pass']=np.where(df['reading score']<40,'Fail','Pass')
df['writing_pass']=np.where(df['writing score']<40,'Fail','Pass') """

# %%
# Normal distribution
sns.displot(students_t,x = "scores" ,
hue = "gender",
col = "sbj_name", 
kind = "hist")

#%%
avg, stdv = group_mean_std(students_t, "gender", "sbj_name","scores" )
avg
stdv
#%%
ymin, ymax = group_range_mean(students_t, "gender", "sbj_name","scores" )
ymin
ymax
#%%
sns.set_theme(style="ticks", color_codes=True)

# %%
a_plot = sns.catplot(x="sbj_name", y="scores", hue="gender",
            palette={"male": "g", "female": "m"},
            markers=["^", "o"], linestyles=["-", "--"],
            kind="point", data=students_t)

(a_plot.set(ylim=(ymin, ymax)))





# %%
#Categorical 
students_t.lunch.value_counts(normalize=True)
# %%
students_t.lunch.value_counts(normalize=True).plot.barh()

#%%
students_t.parental_level_of_education.value_counts(normalize=True)
# %%
students_t.parental_level_of_education.value_counts(normalize=True).plot.pie()





#%%
#Continuous 
sns.pairplot(students, vars = ["math_score", "reading_score", "writing_score"])
# %%
students[["math_score", "reading_score", "writing_score"]].corr()
# %%
sns.heatmap(students[["math_score", "reading_score", "writing_score"]].corr(), annot=True, cmap = 'Reds')
# %%
avg, stdv, med = group_mean_std_median(students_t, "gender", "sbj_name","scores" )
avg
stdv
med
my_group = students_t.groupby(['gender','sbj_name'])['scores']
# males's are better than female in math only 
# %%
sns.boxplot(students_t.sbj_name, students_t.scores, hue = students_t.gender)
# %%



#inferential statisics 

#students_t['Score_ZScore'] = (students_t["scores"] - students_t["scores"].mean())/students_t["scores"].std(ddof = 0)
# %%

""" fig, ax = plt.subplots(1, 1)
x = np.linspace(norm.ppf(0.01),
             norm.ppf(0.99), 100)
ax.plot(x, norm.pdf(x),
       'r-', lw=5, alpha=0.6, label='norm pdf') """

""" cutOffPoint = 70
print(1-(scipy.stats.norm(72.5, 8.06807).cdf(70))) """
# %%
st.t.interval(alpha=0.95, df=len(students_t["scores"])-1, loc=np.mean(students_t["scores"]), scale=st.sem(students_t["scores"])) 
# %%

# Create a list
sampled_means = []

# For 1000  times,
for i in range(0,1000):
    # Take a random sample of 100 rows from the population, take the mean of those rows, append to sampled_means
    sampled_means.append(students_t["scores"].sample(n=100).mean())

# %%


pd.Series(sampled_means).hist(bins=100)
# %%
students_t["scores"].mean()
#%%
pd.Series(sampled_means).mean()
# %%
error = students_t["scores"].mean() - pd.Series(sampled_means).mean()
error
# %%
