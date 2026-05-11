import sys
import os
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import numpy as np
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor_new.pkl')

class DataTransformation:
    def __init__(self):
        self.data_tranformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            numerical_columns = ['reading_score','writing_score']
            categorical_columns = ["gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"]

            num_pipe = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            cat_pipe = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ohe',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )

            logging.info(f'Categorical Columns: {categorical_columns}')
            logging.info(f'Numerical Columns: {numerical_columns}')

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline',num_pipe,numerical_columns),
                    ('cat_pipeline',cat_pipe,categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
         
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read the train and test data")

            logging.info("Obtaining preprocessing object")

            preprocessing_object = self.get_data_transformation_object()

            target_columns = 'math_score'
            X_train = train_df.drop(columns=[target_columns])
            y_train = train_df[target_columns]

            X_test = test_df.drop(columns=[target_columns])
            y_test = test_df[target_columns]

            logging.info('Applying preprocessing object on training and testing dataframe')

            input_train_arr = preprocessing_object.fit_transform(X_train)
            input_test_arr = preprocessing_object.transform(X_test)

            train_arr = np.c_[input_train_arr, np.array(y_train)]
            test_arr = np.c_[input_test_arr, np.array(y_test)]

            logging.info("Saving processing object")

            save_object(
                file_path=self.data_tranformation_config.preprocessor_obj_file_path,
                obj = preprocessing_object
            )

            return(
                train_arr,
                test_arr,
                self.data_tranformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)