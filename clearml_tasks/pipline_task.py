from clearml import PipelineController
from config.config import AppConfig



def main(app_config):
    
    #task.connect(app_config)

    pipe = PipelineController(
        name="Training pipeline", 
        project=app_config.project_name, 
        version="0.0.1"
    )

    # pipe.add_step(
    #     name='extraction_data',
    #     base_task_project=app_config.project_name,
    #     base_task_name='data validation',
    #     parameter_override={
    #         'General/dataset_id': "154c3168ba74424bba3fd9a848a00594"},
    # )

    pipe.add_step(
        name='validation_data',
        # parents=['extraction_data', ],
        base_task_project=app_config.project_name,
        base_task_name='data validation',
        # parameter_override={
        #     'General/dataset_id': "154c3168ba74424bba3fd9a848a00594"},
    )

    pipe.add_step(
        name='model_training',
        parents=['validation_data', ],
        base_task_project=app_config.project_name,
        base_task_name='model training',
        # parameter_override={
        #     'General/dataset_id': "154c3168ba74424bba3fd9a848a00594"},
    )
    #pipe.start()
    # pipe.add_step(
    #     name='preparation_data',
    #     parents=['validation_data', ],
    #     base_task_project=app_config.project_name,
    #     base_task_name='data validation',
    #     parameter_override={
    #         'General/dataset_id': "154c3168ba74424bba3fd9a848a00594"},
    # )

    # pipe.add_step(
    #     name='model_training',
    #     parents=['preparation_data', ],
    #     base_task_project=app_config.project_name,
    #     base_task_name='training model',
    #     parameter_override={
    #         'General/dataset_id': "154c3168ba74424bba3fd9a848a00594"},
    # )
    # pipe.add_step(
    #     name='model_validation',
    #     parents=['model_training', ],
    #     base_task_project=app_config.project_name,
    #     base_task_name='validation model',
    #     parameter_override={
    #         'General/dataset_id': "${preparation_data.parameters.dataset_id}"},
    # )
    # pipe.add_step(
    #     name='model_evaluation',
    #     parents=['model_validation', ],
    #     base_task_project=app_config.project_name,
    #     base_task_name='evaluation model',
    #     parameter_override={
    #         'General/dataset_id': "${preparation_data.parameters.dataset_id}"},
    # )

if __name__=='__main__':
    app_config = AppConfig.parse_raw()
    main(app_config)




