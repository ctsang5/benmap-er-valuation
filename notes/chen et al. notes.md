Chen et al. (2023)

* There is evidence that wildfire-specific PM2.5 increases ED visit risk compared to PM2.5 (Elser et al. 2023), which is supported by toxicological evidence of greater lung inflammation from wildfire smoke vs. ambient non-wildfire PM2.5 (Wegesser et al. 2009).   
  * Wildfire-specific PM2.5 has been shown to increase the risk of ED visits for headache disorders  
  * Mice exposed to wildfire-specific PM2.5 had a greater risk of inflammation of the lungs compared to PM2.5  
  * Wildfire-specific PM2.5 may increase the risk of respiratory hospital visits by ten times compared to non-wildfire ambient PM2.5  
* Previous studies have shown a clear negative correlation between respiratory diseases and wildfire-specific PM2.5. But it’s not yet clear how wildfire-specific PM2.5 correlates with cardiovascular diseases–this paper aims to contribute to this gap.

* The method has two parts:  
  * Part (1): the paper ran a regression for each air basin to estimate the association between smoke from wildfires and ED visits for cardiovascular and respiratory diseases.   
    * The expected cardiovascular/respiratory ED visit count is B\_{1} times what it would be  
    * The result was 11 distinct coefficients–originally 15 but 4 basins had no wildfire event during the study period  
  * Part (2): the paper took the weighted average of the coefficients; a coefficient with a smaller standard error was given a higher weight.  
    * Results: wildfire smoke was associated with a 14.3% increase in the risk of ED visits for all respiratory diseases; and 3.2% increase in the risk of ED visits for all cardiovascular diseases. 

* The health impact function estimates the number of ED visits caused by smoke from wildfires. It is the sum of cardiovascular/respiratory ED visits in each basin. Each cardiovascular/respiratory ED visit in a basin is the product of:  
  * total respiratory/cardiovascular ED visits in a basin  
  * study period (4 years \+ 214 days \= 856 days)  
  * basin population  
  * baseline daily rate (total number of ED visits for respiratory/cardiovascular in a basin / study period / basin population)  
  * coefficient estimate found from random effects meta analysis (Part 2\)  
  * number of days with wildfire smoke  
* The result is 4,597 ER visits for respiratory disease caused by wildfire smoke; and 889 ED visits for cardiovascular disease.

The goal of the capstone project is to estimate the economic cost of 4,597 ER visits for respiratory disease and 889 ED visits for cardiovascular disease.   
