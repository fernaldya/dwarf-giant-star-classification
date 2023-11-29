# HACKTIV8 Milestone Project Phase 1
## Full Time Data Science

Name: Fernaldy Aristo Wirjowerdojo
Batch: HCK-009

## Project Information
This programme is created to classify stars as giants, dwarfs, or other special categories by using a predictive model trained on distinctive astrophysical characteristics. Utilising a dataset from [Kaggle](https://www.kaggle.com/datasets/vinesmsuic/star-categorization-giants-and-dwarfs), the model will analyse parameters such as visual magnitude (Vmag), parallax (Plx), B-V color index, and absolute magnitude (Amag) to determine a star’s classification. The primary goal is to enhance our understanding of the night sky, offering astronomers and enthusiasts a sophisticated tool to discern stars. The model created here is deployed to [HuggingFace](https://huggingface.co/spaces/fernaldya/Milestone)

## Approach
1. Create four models: K nearest neighbours (KNN), Support Vector Machine (SVM), Decision Tree and Random Forest
2. Train the models with the data
3. Perform cross validation on all four models to evaluate the trained model
4. Grab the best model with a good balance of `f1_score` between the train and test data
5. Create a boosting model and evaluate the difference between the performance of the boosting model and the best model
6. Choose the final best model between the best model or the boosting model 
7. Perform hyperparameter tuning on the final best model
