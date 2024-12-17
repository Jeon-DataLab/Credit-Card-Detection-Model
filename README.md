# Credit-Card-Detection-Model
This repository contain Credit Card Fraud Model using the dataset from Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud. It contains transaction information made in September 2013 by European Cardholders where 492 are deemed fradulent out of 284,807 transactions. 

The dataset has been applied with PCA transformation. It allows for faster processing with low diemntionality. In this repository, two things are included. A jupyter notebook that creates and analyze the model, and the other, for deployment of the model. The model applied are isolation forest, linear regression, XGBoost, Random Forest, Neural Network and more. Each models were analyzed, computed for accuracy and model performance metrics. While some models show a good recall rate, the precision should be at cost and vice versa. In all considerations, the notebook conclude Neural Network to be the best performer in detecting fraudulet and legitimate cases. 

Summary of the result:
![](https://github.com/Jeon-DataLab/Credit-Card-Detection-Model/blob/main/Github%20CreditCard%20model.png)
