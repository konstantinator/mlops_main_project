

from clearml import Task, TaskTypes, Dataset
from config.config import AppConfig
from src.data_extraction import main_actions
from clearml import Dataset
from config.config import AppConfig 


def main(config: AppConfig):
    task:Task = Task.init(project_name=config.project_name,
                            task_name=config.extracr_task, 
                            task_type=TaskTypes.data_processing)

    task.connect(config)

    main_actions(config=config)


if __name__ == "__main__":
    config = AppConfig.parse_raw()
    main(config)
