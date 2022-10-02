import clearml

def main():
    id, _version  = clearml.Dataset._get_dataset_id(dataset_project='main_dataset_project', 
                                    dataset_name='main_dataset')
    dataset = clearml.Dataset.create(dataset_project='main_dataset_project', 
                            parent_datasets=[id],
                            dataset_name= 'main_dataset',
                            description='my main dataset')
    dataset.add_files('/app/data')
    dataset.upload(verbose=True)
    dataset.finalize()


if __name__=='__main__':
    main()