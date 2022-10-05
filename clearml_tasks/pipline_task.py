from clearml import PipelineController
from config.config import AppConfig


def main(config):

    pipe = PipelineController(
        name="Training pipeline", 
        project=config.project_name, 
        version="0.0.1"
    )

    pipe.add_step(
        name='extraction_data',
        base_task_project=config.project_name,
        base_task_name=config.extracr_task,
    )

    pipe.add_step(
        name='validation_data',
        parents=['extraction_data', ],
        base_task_project=config.project_name,
        base_task_name=config.val_task,
    )

    pipe.add_step(
        name='preparation_data',
        parents=['validation_data', ],
        base_task_project=app_config.project_name,
        base_task_name=config.prep_task,
    )

    pipe.add_step(
        name='model_training_validation_evalution',
        parents=['preparation_data', ],
        base_task_project=config.project_name,
        base_task_name=config.training_task,
    )
 
    pipe.start_locally(run_pipeline_steps_locally=True)


if __name__=='__main__':
    app_config = AppConfig.parse_raw()
    main(app_config)
