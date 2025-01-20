
# Customer Segmentation Using RFM Analysis and Clustering

The goal of this project is to segment customers based on their purchasing behavior using the RFM (Recency, Frequency, Monetary) framework. By applying clustering techniques such as K-Means and Hierarchical Clustering, the project identifies distinct customer groups to aid in targeted marketing strategies and personalized customer experiences.




## Data

The dataset contains transactional data with the following key attributes:

- CustomerID: Unique identifier for customers.

- InvoiceNo: Invoice number associated with a transaction.

- Date of Purchase: Date when the transaction occurred.

- Price: Transaction value.
## Project Workflow

### 1. **Data Cleaning and Preprocessing**
- Checked for missing values and handled them appropriately.
- Dropped unnecessary columns and duplicates.
- Formatted the date column and ensured data consistency.

### 2. **RFM Feature Engineering**
- Aggregated the data to compute Recency, Frequency, and Monetary values for each customer.
- Transformed skewed data for better clustering performance:
  - Log transformation for `Recency` and `Frequency`.
  - Applied PowerTransformer, cube root, and fourth root transformations to handle outliers in `Monetary`.

### 3. **Scaling the Data**
- Used `RobustScaler` to normalize the transformed RFM features and reduce the influence of outliers.

### 4. **Clustering**
- **Elbow Method and Silhouette Analysis**:
  - Identified the optimal number of clusters using Within-Cluster Sum of Squares (WCSS) and silhouette scores.
- **K-Means Clustering**:
  - Implemented K-Means clustering with the optimal number of clusters (k=3).
- **Hierarchical Clustering**:
  - Visualized customer groups using a dendrogram based on Ward's method.

### 5. **Results and Interpretation**
- Assigned customers to clusters based on RFM scores.
- Analyzed cluster characteristics to understand customer segments:
  - High-value customers with frequent transactions and recent activity.
  - Moderate-value customers with average transaction patterns.
  - Low-value customers with infrequent purchases and lower monetary contributions.

### 6. **Visualization**
- Created boxplots to visualize the distribution of `Recency`, `Frequency`, and `Monetary` before and after transformations.
- Used a dendrogram to illustrate hierarchical clustering results.
- Visualized WCSS and silhouette scores to select the optimal number of clusters.

![image](https://github.com/user-attachments/assets/dff02738-7d64-4fec-9a5d-0a44a8f8269a)


## Conclusion

This project successfully segmented customers using RFM analysis and clustering methods, providing actionable insights for data-driven marketing strategies.
