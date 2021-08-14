# surfs_up

# Purpose 

The purpose of this analysis is to examine weather data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round. We will look initially in temperature data for the months of June and December, then percipitation levels for the same month as well as average measurements for both based on the weather station that provided the data which was recorded during a 7 year period between 2010 and 2017. 

# Results

- Minimum temperatures are 8 degrees lower in December compared to June.
- Maximum temperatures are 2 degress higher in June compared to December. 
- Average temperatures are 3 degrees higher in June at 75 degrees compared to 71 in December. 
- Standard deviation is 3.25 for June and 3.75 for December. 

# Summary

## Proof of a steady temperature pattern
The most important result of our analysis is the standard deviation of daily temperature range. The values for both months indicate remarkably steady temperature patterns. The mean Standard Deviation for June is well below the **mean std for summer days** which stands at 3.717 - In our case **std** for June is 3.25. Similarly std for June is also a bit lower than the **mean std for winter days** which stands at 3.807 - In our case **std** for December is 3.75. 

![](images/tobs_compare.png)

Zooming in into the numbers we see that the variation in temperatures is indeed insignificant compared to other regions of the world. With a year-round low of around 55 degrees, highs around 85 and means slightly over 71 degrees the surf and ice-cream business is fail safe. Another fact that stands out is the increase in average tempertature in the third and third quartile for both June and December. This translates to an increase of temperature in the most recent years. Since aveage temperatures have risen, winters are milder and this further increases the chances of this business operating year round. But let us take a look at another major factor. Rainfall. 

## Precipitation stats

![](images/prec_compare.png)

Looking at precipitation averages we see low amounts of rainfall. The first quartile equals the minimum precipitation for both June and December at 0.00
In the second and third quartiles rainfall is almost at the same levels for both months. However, standard deviation for December is significantly higher than June at 0.54 compared to 0.34 . This may indicate less rainy days with more severe rainfall for the winter. 

![](images/stations_compare.png)
