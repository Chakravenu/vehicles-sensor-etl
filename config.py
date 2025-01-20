# config.py

class Config:
    # AWS credentials
    AWS_ACCESS_KEY_ID=""
    AWS_SECRET_ACCESS_KEY=""
    AWS_DEFAULT_REGION=""
    # Bucket name
    BUCKET_NAME = 'vehicles-sensor-data'
    # File key to read
    INPUT_FILE_NAME = 'input-data/sensor_data.csv'
    # Output Files
    OUTPUT_MAINTENANCE_ANALYSIS = 'output-data/maintenance_analysis_output.csv'
    OUTPUT_MODEL_COMPARISION = 'output-data/model_comparision_output.csv'
    OUTPUT_XGBOOST_FEATURE_IMPORTANCE = 'output-data/xgboost_feature_imp_output.csv'
    
    
    # data frame
    RANDOM_INPUT_DATA =None
    SENSOR_INPUT_DF = None
    SENSOR_PROCESSED_DF = None
    MODEL_COMPARISION = None
    XGBOOST_FEATURE_IMPORTANCE= None
    MAINTENANCE_ANALYSIS =  None
    