from clearml import Task, TaskTypes, Dataset
from config.config import AppConfig
from src.data_validation import main_actions
from config.config import AppConfig 


def main(config: AppConfig):
    task:Task = Task.init(project_name=config.project_name,
                            task_name=config.prep_task, 
                            task_type=TaskTypes.data_processing)
    
    id, _version  = Dataset._get_dataset_id(dataset_project=config.dataset_project, 
                                            dataset_name=config.dataset_name)

    path = Dataset\
        .get(dataset_id=id)\
        .get_local_copy(config.dateset_local_path)
    config.dateset_local_path = path

    task.connect(config)

    main_actions(config=config)

    id, _version  = Dataset._get_dataset_id(dataset_project=config.dataset_project, 
                                            dataset_name=config.dataset_name_prep)

    dataset = Dataset.create(dataset_project=config.dataset_project,
                            parent_datasets=[id],
                            dataset_name=config.dataset_name_prep,
                            description='my main dataset')

    dataset.add_files('/app/data_prep')
    dataset.upload(verbose=True)
    dataset.finalize()


if __name__ == "__main__":
    config = AppConfig.parse_raw()
    main(config)
