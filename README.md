<<<<<<< HEAD

ABOUT 
As we all know COVID-19 has been prevalent across the nation starting in 2019 in China 
and reaching the rest of the world shortly after. As someone who lives in the United States 
and similar to other countries who were not 
=======
ABOUT: 


As we all know the COVID-19 virus has been prevalent across the nation starting with China in 2019 and reaching the rest of the world shortly after. The lack of information regarding the pandemic has caused many unforseen circumstances. As someone who lives in the United States, I have seen the effects of COVID-19 first hand, from shutdowns to lack of interactions with others and sadly how it has effected peoples mental and physical health. Although the beggnning of the pandemic caused the governemnt to implement many precautions as of lately that no longer seems to be the case. Currently, precautions sucha as standing six feet a part, requiring a mask, and/or being tested no longer seems necessary. This cultural shift made me wonder how and/or did the rest of the world experienced COVID? I began to look at different countries and decided to pick India. I believed analyzing COVID-19 trends in India was an interesting idea given that the population is very large. 


With this in mind, this project analyzes the impact of  confirmed cases of COVID-19 specfically the relationship between foreign and Indian born citizens in different territories, the number of deaths caused by COVID-19 compared to the number of cured cases. It will also compare the highest territory of testing data and the lowest testing activity data. It also comapres vaccine activity for both females, males and total vaccine statewide.


DATA SOURCES: 

In order to access the data used in this project you can visit the following site: https://www.mohfw.gov.in/ and https://www.covid19india.org/
It provides three different data set and you would download each one which are: 
StatewiseTestingDetails.csv, (which can be found in the first link )
covid_vaccine_statewise.csv, (first link)
covid_19_india.csv, (second link) 

This data set provides information on all territories within India and how COVID-19 invididually affected each territory. Also, it goes into detail about the level of testing activity within each state, the activity varies greatly depending which state you look at. The last dataset hones in on vaccination activity, whether thats the number of doses taken and/or how inviduals identify themselves. This ranges from female, male and transgender. It also breaks down vaccination status by ages such as 18- 25,30 -44 and 60+. 

Order of Running the Scripts: 

1) = covid. py
This script first cleans the data in order for it to become more readable, by dropping specific cloumns and checking if there any null values. It also groups and sums up all the cases. In order to get is sorted and cleaned we combined all cases and sorting the data so that it easier to work with. The script then sorts and graph cases among foriegn born citizens in India by territory which produces "Cases among Foreign Born by Territory.png" It also graphs cases among Indians by territory which produces "Cases among Indians by Territory.png". Followed by confirmed cases among territories which results in "Confirmed Cases.png",  Followed by all curedcases among terriotires which produces "Cured Cases.png" and lastly deaths caused by COVID-19 which produces a bar plot "deaths.png"

 
2)= StateWisetTesting.py
3 = vaccinaton_status.py 
>>>>>>> 095d7b2e81bbcfcbd68f937bd378fb86267f94ae
