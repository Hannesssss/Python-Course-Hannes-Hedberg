# Assignment - Workflow for AI-project

The goal of this report is to attempt to describe a workflow to get an overview of the most common steps in creating a machinelearning application. In this example the application will attepempt to get an overview of the price ranges of houses. The price ranges will be based on different features such as amount of rooms, sieze, location. 

To begin the process we research if this has been done before, which it most likley has. Similiar applications has been done by people trying on Kaggles competition [^source4] regarding the same subject.    

In order to gather data, depending on the scale and budget of the project we can approach it in a few different ways. If its a large project with a high budget we could pay for already collected data to use in our machinelearning module. One advantage to this method is we get alot of data quickly and is less time consuming that collecting it ourselfs. If we however wish to gather the data ourselves then tryo labs [^source5] has written an indepth guide on how we could approach this. Everything from maps, pictures, house sieze, neighboorhood school, rents, emergency service, socioeconmic enviroments and more would need to be collected.  

Tryo labs recommend utilizing a great variety of sources for this data, the more sources, the more data, the more data the more accurate our application will become. One soild example from tryo labs is the usage of Mapboxs Satellite API [^source6] which allows the user to query any location by coordinates with 50 000 requests per month. This provides a solid amount of data to feed the machinelearning.

Other data such as demographic variables are a little more tricky, we cant just feed satellite images for this. In Try Labs example they are gathering data on house values in the United States, where they utilize "American Community Survey" (ACS) [^source7]. Since they gather monthly surveys on income, education, employment, vacant housing etc they would be a great source for demographic data. ACS measure census tract level, which are small subdivisions of a county. In order to display all this data we can utilize heatmaps.

<img src="assets/heatmaps1.png" alt="Coding man" width="50%" height="20%" />

Using the heatmaps we can explore the correlation between the variablies and what ever our target might be. This is where linear regression comes into play.

<img src="assets/LinearRegression2.png" alt="Coding man" width="50%" height="20%" />

Linear regression analysis is commonly used as a tool to predict the value of X varible compared to Y variable. Where you try to predict one X, which is usually refered to as the "dependent variable", compared to the "Y" variable, which is usually known as the independent variable. This is possible by comparing the dependent variable to the independent variable. By utilizing this form of analysis we can estimate coefficients on a linear equation. Linear regression minimizes the discrepanices between the predict and the actual output of the values.  


<img src="assets/LinearRegression.png" alt="Coding man" width="50%" height="20%" />

### Soruces

1. [^source1] topflight:  Machine Learning Mobile App Development: All the Whys and Hows

2. [^source2] Nivida:  machine learning guide

3. [^source3] Towards Data Sience: Predicting House Prices with Machine Learning

4. [^source4] Kaggle:  House Prices - Advanced Regression Techniques

5. [^source5] Tryo Labs: Real Estate pricing with Machine Learning & non-traditional data sources

6. [^source6] Mapbox Imagery

7. [^source7] American Community Survey: ACS

---

[^source1]: https://topflightapps.com/ideas/how-to-create-a-machine-learning-app/

[^source2]: https://developer.nvidia.com/blog/step-by-step-guide-to-building-a-machine-learning-application-with-rapids/

[^source3]: https://towardsdatascience.com/predicting-house-prices-with-machine-learning-62d5bcd0d68f

[^source4]: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview/tutorials

[^source5]: https://tryolabs.com/blog/2021/06/25/real-estate-pricing-with-machine-learning--non-traditional-data-sources

[^source6]: https://www.mapbox.com/maps/satellite

[^source7]: https://www.census.gov/programs-surveys/acs


