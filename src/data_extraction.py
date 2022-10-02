from clearml import Dataset
from config.config import AppConfig 
import pandas as pd 

def main_actions(config: AppConfig):
    
    
    id, _version  = Dataset._get_dataset_id(dataset_project=config.dataset_project, 
                                            dataset_name=config.dataset_name)

    path = Dataset\
        .get(dataset_id=id)\
        .get_mutable_local_copy(config.dateset_local_path)
    # breakpoint()

    #pd.read_csv()

def main():
    config = AppConfig.parse_raw()
    main_actions(config=config)


if __name__=='__main__':
    main()




