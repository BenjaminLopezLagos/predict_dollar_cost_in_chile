# small project which consists of a model that predicts next month's dollar cost in CLP.
* Extracts historic data from Banco Central de Chile using BeautifulSoup. By using Airflow, the scraping script is being executed once a day.
* Uses jenkins and dind to automate the data transformation and model training process, and then proceeds to deploy to DockerHub a flask application containing the trained scikit-learn model.
* You can access this application by pulling the following image.
```
docker pull benjaminlopezlagos/clp_dollar_prediction
```

### to-do:
* (done): Use airflow and download an updated dataset each week or month.
* add model and data version control.
