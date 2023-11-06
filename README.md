# water_potability
This repo is created for the projects done for the ML_ZOOMCAMP from data.talks

## files present
- notebook.ipynb: jupyter notebook file with dataframe ingestion, analysis, EDA, feature selection and ml model hyperparameter tuning
- train.py: python file that was used to create final ml model available at model.bin
- model.bin: binary file created with pickle with ml model to be used into classification
- predict.py: python file created to generate a flask app to allow usage of model.bin as a webservice.
- predict_test.py: python file created to test the webservice. This can be used for localhost test or cloud test, just chaneg the url.
- Pipfile and Pipfile.lock: files to create a pipenv to execute files and build container.
- Dockerfile: docker configuration file to create container.
- water_potability.csv: dataset to be used in case link to original github file repository is removed. This dataset was originated from [link](https://github.com/MainakRepositor/Datasets/tree/master)
  
## Description of the problem

