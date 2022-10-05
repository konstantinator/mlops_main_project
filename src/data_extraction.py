from clearml import Dataset
from config.config import AppConfig 
import pandas as pd 
import clearml


def main_actions(config: AppConfig):
    id, _version  = clearml.Dataset._get_dataset_id(dataset_project=config.dataset_project,
                                    dataset_name=config.dataset_name)

    dataset = clearml.Dataset.create(dataset_project=config.dataset_project,
                            parent_datasets=[id],
                            dataset_name= config.dataset_name,
                            description='my main dataset')

    dataset.add_files('/app/data')
    dataset.upload(verbose=True)
    dataset.finalize()


def main():
    config = AppConfig.parse_raw()
    main_actions(config=config)


if __name__=='__main__':
    main()
