from typing import Union
from pathlib import Path
from pydantic_yaml import YamlModel


class AppConfig(YamlModel):
    # project
    project_name: str
    # project_version: str

    # clearml dataset
    dataset_project: str
    dataset_name: str
    dataset_name_prep: str
    dateset_local_path: str


    # task_names
    extracr_task:str
    val_task: str
    prep_task: str
    training_task: str

    # model
    random_state: int
    test_size: float
    max_iter: int
    num_iters: int

    # data
    # data_dir: str
    dataset_id: str
    # model training
    # lr: float
    # momentum: float
    # num_epochs: int
    # validation
    # val_acc_threshold: float
    # val_loss_threshold: float

    @classmethod
    def parse_raw(cls, filename: Union[str, Path] = "/app/config/config.yaml", *args, **kwargs):
        with open(filename, 'r') as f:
            data = f.read()
        return super().parse_raw(data, *args, **kwargs)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)