
from config.config import AppConfig
from clearml import Task, TaskTypes, Dataset
from pathlib import Path
from src.model_training import main_actions

def main(config: AppConfig):
    task:Task = Task.init(project_name=config.project_name,
                            task_name=config.training_task, 
                            task_type=TaskTypes.training)

    id, _version  = Dataset._get_dataset_id(dataset_project=config.dataset_project, 
                                            dataset_name=config.dataset_name)
    path = Dataset\
        .get(dataset_id=id)\
        .get_local_copy(config.dateset_local_path)
    config.dateset_local_path = path

    task.connect(config)

    main_actions(config=config)

if __name__ == "__main__":
    config = AppConfig.parse_raw()
    main(config)