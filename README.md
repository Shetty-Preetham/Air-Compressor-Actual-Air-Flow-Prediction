
##### Ingersoll Rand Make Air Compressor Actual Delivery flow(cfm) prediction

This business case study project mainly helps the sales engineer to predict what kind of model they can suggest to clients based on cfm flow and other parameters.Generally while buying compressor,clients only specifies requirement as the power and pressure.Then Its hard for the sales engineer to go through all the catalogue and to suggest the compressor model instantly, it is a time consumering process too. So the main aim of this project is to minimize the time of sales engineer to go through catalogue. This project will predict the  actual delivery flow when you input data of pressure,power and weight.Then based on the predicted actual delivery flow and other parameters like power, pressure,weight it is easy for sales engineer to suggest to clients.





##### DataSet Extraction

Currently I am working for Ingersoll Rand air compressor channel partner as a Senior Sales Engineer,I want to explore in business case study using machine learning algorithms,Hence I decided to create a business problem and solution for it where I had domain/product knowledge in our product(Air compressor)
Mainly I came across the business problem like,difficulty in suggesting the suitable prospect compressor model at the spot.To minimize the time thought of building a model that helps in suggesting the model to the customer.I scrapped from various catalouges and prepared my own data sets.
This is a mini project and needs to be enhanced in the future


* Model : name of the compressor models
* Power : power of a TEFC(Total Enclosed fan cooled motor) moter in KW
* Pressure : pressure of compressed air in bar
* Weight : Weight of the compressor in Kg
* Controller Type : Controller typer based on air end
* flow : The output air flow (cfm). Target variable to be predicted




##### Approach 

Regressor model is used to predict the flow(cfm).Different models are build out of which XGBoost Regressor gave highest accuracy and the final model is build using the same.
Pipeline is done for the final model and using pickle model is saved.



##### Deployment

Deployment is done using Streamlit
( refer : https://docs.streamlit.io/ )

```bash
  streamlit run IR_compressor.py 
```



As a future enhancement for this case study, many data records can be added and few other related features can also be included.Classification and clustering models can also be implemented in future.