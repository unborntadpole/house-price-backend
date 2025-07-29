from sklearn.cluster import Birch
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data_for_model.csv")

# Select columns for clustering
clustering_features = ["location1", "buildupArea_sqft", "bedrooms", "bathrooms", "balcony"]

# Preprocessing
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), ["buildupArea_sqft", "bedrooms", "bathrooms", "balcony"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["location1"])
])

X_cluster = preprocessor.fit_transform(df[clustering_features])

# Clustering
birch_model = Birch(n_clusters=5)
clusters = birch_model.fit_predict(X_cluster)

# Add to dataframe
df["cluster"] = clusters

# Visualize cluster distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="cluster", palette="Set2")
plt.title("Cluster Distribution")
plt.show()

# Save cluster-labeled data
df.to_csv("data_with_clusters.csv", index=False)
