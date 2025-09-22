# credit_default_prediction
A credit default prediction project using scikit-learn

## Resources
- Interactive Python Notebook
- Jupyter Notebook
- scikit-learn
- Python
- CSV
- Pickle File

## Problem Statement:
Given a set of user data including Sex, Age, Payments, and Bill Amounts, determine if a client will default on their loan.</br>
Link to dataset: https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset?resource=download 

## ML Results
Once the data is loaded, the notebook creates a histogram and boxplot, checking for any outliers or extremities we may have in our data. Next our code runs the data through a preprocessor to prepare our data for our model before splitting our data in parts we want to train with. The code then builds our ML model with what we received from our preprocessor and uses a RandomForestClassifier to determine if someone would default on their payment next month. I used a RandomForestClassifier since it is best suited for handling tabular data and reduces overfitting compared to a single decision tree. Finally the notebook evaluates our model and we can see the overall results of the models predictions.

> Accuracy: 81.67% </br>
> Precision: 64.57% </br>
> Recall: 35.95% </br>
> F1 Score: 46.18% </br>
> Confusion Matrix: </br>
 > [[4428  259] </br>
 > [ 841  472]] </br>

 ## Conclusion 

 With an Accuracy of 81% but a Recall of 35% the model is good but does not catch most clients that will actually default. 

 ### Next Steps
 - Balance out the dataset (oversampling vs undersampling)
 - Tune the RandomForest class weights to look more closely at clients that defaulted. 
 - Use other metrics such as ROC-AUC to help balance out the data.


#### -Israel Medina 09.22.2025