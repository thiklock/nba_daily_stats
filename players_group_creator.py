# This code explores the NBA players from 2013 - 2014 basketball season, and uses # a machine learning algorithm called kMeans to group them in clusters, this will # show which players are most similar


#import the dependencies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


nba = pd.read_csv('2019-2020_NBA_Player_Stats.csv', error_bad_lines=False, engine="python") # the nba_2013.csv data 

mean_stats = nba.mean()

print(mean_stats)

# sns.pairplot(nba[["AST", "TOV", "STL", "BLK", "PF"]])

plt.show()

correlation = nba[["AST", "TOV", "STL", "BLK", "PF"]].corr()

print(correlation)

sns.heatmap(correlation, annot=True)
plt.show()


print('end')


from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=5, random_state=1)
good_columns = nba._get_numeric_data().dropna(axis=1)
kmeans_model.fit(good_columns)
labels = kmeans_model.labels_
print(labels)


from sklearn.decomposition import PCA
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(good_columns)
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
plt.show()

# Find player LeBron
LeBron = good_columns.loc[ nba['Player'] == 'LeBron James\jamesle01',: ]

#Find player Durant
Durant = good_columns.loc[ nba['Player'] == 'Kevin Durant\duranke01',: ]

#print the players
print(LeBron)
print(Durant)


#Change the dataframes to a list 
Lebron_list = LeBron.values.tolist()
Durant_list = Durant.values.tolist()

#Predict which group LeBron James and Kevin Durant belongs
LeBron_Cluster_Label = kmeans_model.predict(Lebron_list)
Durant_Cluster_Label = kmeans_model.predict(Durant_list)

print(LeBron_Cluster_Label)
print(Durant_Cluster_Label)

all_stats_corr = nba.corr()


print(all_stats_corr)

#######################################################################################

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(nba[['FG']], nba[['AST']], test_size=0.2, random_state=42)

#Create the Linear Regression Model
from sklearn.linear_model import LinearRegression
lr = LinearRegression() # Create the model
lr.fit(x_train, y_train) #Train the model
predictions = lr.predict(x_test) #Make predictions on the test data
print(predictions)
print(y_test)

lr_confidence = lr.score(x_test, y_test)
print("lr confidence (R^2): ", lr_confidence)


from sklearn.metrics import mean_squared_error
print("Mean Squared Error (MSE): ",mean_squared_error(y_test, predictions))