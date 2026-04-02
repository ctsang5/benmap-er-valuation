

* The goal of this paper is to estimate the total value of avoiding ED visits for cardiovascular/respiratory illness.   
  * If it makes it easier to understand, replace the total value of avoiding an illness with the total cost of an illness. 


* The researchers define the total value of avoiding ED visits for illness as the sum of four parts; each part:  
  * Cost of treatment–every dollar spent by anyone (the hospital, the government, the patient) because the patient was treated in an ED  
  * Lost productivity–the missed work days valued at the average daily wage (CAN$119.60/day in 1997); includes the missed work days by parents/caregivers of the patient  
  * Pain and suffering–the dollar value of pain, inconvenience, restricted activities, reduced enjoyment of leisure, and anxiety to the patient and family members/others (if a patient’s spouse has to cancel their plans, worry, and drive them to follow up appointments–those are part of V\_PS too)  
  * Averting expenditures–money spent to prevent or reduce cardiovascular/respiratory disease  
* Each part was estimated separately except V\_PS and V\_AE (researchers couldn’t disentangle V\_PS and V\_AE in their survey), so the model they estimated was actually V\_T \= V\_COT \+ V\_LP \+ V\_SP, where V\_SP \= V\_PS \+ V\_AE. 

* Johnson et al (2000) created a stated-preference survey which was used to estimate a WTP model–which Stieb et al. used.  
  * Healthy participants were shown flashcards that described an illness. Each flashcard listed:  
    * A combination of symptoms (coughing/wheezing/shortness of breath); see Table 1 for full list of symptoms  
    * Activity restriction levels (mild limitations/housebound/need help/in hospital); see Table 1 for description of each restriction level  
    * Duration (days)  
  * Estimated a WTP model 

—THE FOLLOWING NUMBERS ARE FOR RESPIRATORY DISEASE (which is defined as Asthma and Respiratory Infection) BECAUSE IT WAS ON MY MIND; EACH PROCESS MENTIONED BELOW IS THE SAME FOR CALCULATING CARDIOVASCULAR DISEASE NUMBERS—

* Saint John ED data says that–of 100 respiratory ED patients:   
  * (Symptoms) –44 have asthma/COPD symptoms and 56 have respiratory infection symptoms  
  * (Activity Restriction Level) –74 have mild limitations, 14 are housebound, 5 care for themselves, 7 admitted to hospital  
  * (Duration) –see Table 3 under “Number of days:” and then “Individuals visiting emergency department”  
* How did Stieb et al. use Johnson et al (2000) and Saint John ED data to calculate V\_SP for respiratory disease?  
  * Created combinations of symptoms, activity restriction level and duration from the Saint John data  
  * Used the WTP model from Johnson et al. to estimate the WTP  
  * Calculated the (weighted) sum of all the rows in the Weight\*WTP column to get V\_SP for respiratory disease  
    

| Combination | Weight | WTP  | (Weight \* WTP) |
| :---: | :---: | :---: | :---: |
| Asthma \* mild | 0.44 \* 0.74 \= 0.326 | (asthma, mild, 12.9 days) | 0.326 \* WTP |
| Asthma \* in hospital | 0.44 \* 0.07 \= 0.031 | (asthma, in hospital, 0.6 days) | 0.031 \* WTP |
| Respiratory Infection \* mild | 0.56 \* 0.74 \= 0.414 | (respiratory infection, mild, 14.3 days) | 0.414 \* WTP |
| Respiratory Infection \* in hospital | 0.56 \* 0.07 \= 0.039 | (respiratory infection, in hospital, 0.9 days) | 0.039 \* WTP |

* V\_LP \= (Weight for Asthma \* Lost Work for Asthma\* $119.60) \+ (Weight for Respiratory Infection \* Lost Work for Respiratory Infection \* $119.60).  
  * Weight for Asthma/Respiratory Infection found in Table 2: 0.44 and 0.56  
  * Lost Work for Asthma/Respiratory Infection found in Table 3: 1.2 and 1.5  
  * $119.60 is the average daily wage in 1997 Canadian dollars  
  * V\_LP for respiratory disease \= $160–see Table 5\.  
* The researchers estimated V\_COT using Saint Johns ED data. See Table 4 for the model.   
  * Interaction terms–what mean?  
  * Plug in critical care, non-critical care, and mean total duration (in hospital \+ out of hospital) from asthma/respiratory infection (see Table 3 for exact numbers)  
  * V\_COT for respiratory disease \= (0.44 \* V\_COT model estimate for asthma) \+ (0.56 \* V\_COT model estimate for respiratory infection)

* Stieb et al. found the total value of avoiding a respiratory ED visit is CAN$2,000; and the total value of avoiding a cardiovascular ED visit is CAN$4,400. In 2015 U.S. dollars that’s ($2,000 \* 0.72 \* 1.90) \= $2,752 and ($4,400 \* 0.72 \* 1.90) \= $6,054, respectively.   
  * 1 CAD \= 0.7226 USD (0.72) was the 1997 exchange rate from CAN$ → USD  
  * CPI Medical Care inflation (1997 → 2015\) says: $1 spent on medical costs in 1997 \= $1.90 spent on medical costs in 2015 ($1 \* (446.752 / 234.583) \= $1.90)  
    * 1997 index \= 234.583  
    * 2015 index \= 446.752  
* BenMAP says avoiding one respiratory ED visit is worth $875. Stieb et al. say it’s worth $2,752. That’s 3.1 times more. BenMAP says avoiding one cardiovascular ED visit is worth $1,161. Stieb et al. say it’s worth $6,054. That’s 5.2 times more.   
* BenMAP doesn’t include WTP and lost productivity/wages for ED visits.  
  * (Stieb et al.): medical costs \+ lost wages \+ pain/suffering \+ averting expenditures  
  * (BenMAP): medical costs

