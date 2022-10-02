from clearml import Task, TaskTypes, Dataset
from config.config import AppConfig
from src.data_validation import main_actions
from clearml import Dataset
from config.config import AppConfig 


def main(config: AppConfig):
    task:Task = Task.init(project_name=config.project_name,
                            task_name=config.training_task, 
                            task_type=TaskTypes.training)

    task.connect(config)
    
    id, _version  = Dataset._get_dataset_id(dataset_project=config.dataset_project, 
                                            dataset_name=config.dataset_name)

    path = Dataset\
        .get(dataset_id=id)\
        .get_mutable_local_copy(config.dateset_local_path)

    main_actions(config=config)


if __name__ == "__main__":
    config = AppConfig.parse_raw()
    main(config)