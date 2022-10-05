from clearml.automation import TaskScheduler


def main():
    scheduler = TaskScheduler()
    scheduler.add_task(schedule_task_id='ccba9c20eb9d411ba9bb7ce6a441746b',
                         queue='default', 
                         name="Training pipeline",
                         execute_immediately=True, 
                         day=1, 
                         target_project='main_project')
    scheduler.start()


if __name__ == '__main__':
    main()
