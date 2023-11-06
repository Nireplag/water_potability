# water_potability
This repo is created for the projects done for the ML_ZOOMCAMP from data.talks

## Files present
- notebook.ipynb: jupyter notebook file with dataframe ingestion, analysis, EDA, feature selection and ml model hyperparameter tuning
- train.py: python file that was used to create final ml model available at model.bin
- model.bin: binary file created with pickle with ml model to be used into classification
- predict.py: python file created to generate a flask app to allow usage of model.bin as a webservice.
- predict_test.py: python file created to test the webservice. This can be used for localhost test or cloud test, just chaneg the url.
- Pipfile and Pipfile.lock: files to create a pipenv to execute files and build container.
- Dockerfile: docker configuration file to create containerto be run locally or at cloud.
- water_potability.csv: dataset to be used in case link to original github file repository is removed. This dataset was originated from [link](https://github.com/MainakRepositor/Datasets/tree/master).
  
## Description of the problem
The dataset used is related to determine the potability of water based on water sample attributes. This can be used to determine the risk for consumption and utilization on other activities, as irrigation.

The attributes as the following:

- pH: pH level of the water.
- Hardness: measure of mineral content.
- Solids: total dissolved solids in the water.
- Chloramines: Chloramines concentration in the water.
- Sulfate: Sulfate concentration in the water.
- Conductivity: Electrical conductivity of the water.
- Organic_carbon: Organic carbon content in the water.
- Trihalomethanes: Trihalomethanes concentration in the water.
- Turbidity: measure of water clarity.
- Potability: Target variable; indicates water potability with values 1 (potable) and 0 (not potable).

## How to run project

### Clone project locally
Plase fork the project and create a local clone of the project locally using:

``` git clone <your-repo-url> ``` 

### Start pipenv environent
The files Pipfile and Pipfile.lock conatin the dependencies to execute the code without issues, therefore it is recomended to  start the virtual environment as following:

- ``` pip install pipenv ``` in case you do not already have if
- From within the directory that have the Pipfile and Pipfile.lock execute the following command in prompt ``` pipenv shell```

### Create model.bin - no need to be executed
This step is not mandatory since we already have the file model available. You can execute the file using the command:
``` python3 train.py```

### Run webservice locally 
It is possible to run the webservice locally using the following command: ``` python3 predict.py```.
In order to locally test the service, uncomment the url from the file predict_test.py for localhost, save it and run the file predict_test.py from a differnt enviroment. Trying to use the same from pipenv will cause an error since it is already running the webservice.
In order to stop the webservice send the command: ``` CTRL + c```.

### Creating a docker image and save it to docker hub

In order to create a docker image, we assume you already have a docker installed in your computer.
To build the image execute the following command into the directory with Dockerfile:
``` python3 train.py```
