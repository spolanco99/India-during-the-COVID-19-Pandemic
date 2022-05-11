##ABOUT: 


As we all know the COVID-19 virus has been prevalent across the nation starting with China in 2019 and reaching the rest of the world shortly after. The lack of information regarding the pandemic has caused many unforeseen circumstances. As someone who lives in the United States, I have seen the effects of COVID-19 first hand, from shutdowns to lack of interactions with others and sadly how it has affected people's mental and physical health. Although the beginning of the pandemic caused the government to implement many precautions as of lately that no longer seems to be the case. Currently, precautions such as standing six feet a part, requiring a mask, and/or being tested no longer seems necessary. This cultural shift made me wonder how and/or did the rest of the world experience COVID? I began to look at different countries and decided to pick India. I believed analyzing COVID-19 trends in India was an interesting idea given that the population is very large. 


With this in mind, this project analyzes the impact of  confirmed cases of COVID-19 specifically the relationship between foreign and Indian born citizens in different territories, the number of deaths caused by COVID-19 compared to the number of cured cases. It will also compare the highest territory of testing data and the lowest testing activity data. It also compares vaccine activity for both females, males and total vaccine statewide.


##DATA SOURCES: 

In order to access the data used in this project you can visit the following site: https://www.mohfw.gov.in/ and https://www.covid19india.org/
It provides three different data set and you would download each one which are: 
StatewiseTestingDetails.csv, (which can be found in the first link )
covid_vaccine_statewise.csv, (first link)
covid_19_india.csv, (second link) 

This data set provides information on all territories within India and how COVID-19 invididually affected each territory. Also, it goes into detail about the level of testing activity within each state, the activity varies greatly depending which state you look at. The last dataset hones in on vaccination activity, whether that's the number of doses taken and/or how individuals identify themselves. This ranges from female, male and transgender. It also breaks down vaccination status by ages such as 18- 25,30 -44 and 60+. 

##Order of Running the Scripts: 


1)= covid.py
This script first cleans the data in order for it to become more readable, by dropping specific columns and checking if there are any null values. It also groups and sums up all the cases. In order to get it sorted and cleaned we combined all cases and sorted the data so that it is easier to work with. The script then sorts and analyzes cases among foriegn born citizens in India by territory. It also analyzes the impact COVID-19 had among Indians by  territory. Followed by confirmed cases among territories which results in. Followed by all cured COVID -19 cases among territories and lastly deaths caused by COVID-19 which produces a bar plot.


2) = statewiseTesting.py 
Script starts off by reading the file and shows general information about testing across all states. This script will show and  then sorts the level of testing activity in chronological order from lowest to highest. After, it analyzes the state with the highest testing activity which results and then compares  and analyzes the state with the lowest testing data which produces a line plot.

 
3) = vaccination_status.py 
This script analyzes vaccination status between male and female within India which results in and lastly the number of people who opted in for the first dose compared to the second dose of the vaccine. In others individuals who are partially vaccinated vs fully vaccinated. 

##Results
The following are the key findings of this study 
1. Covid cases among Indians were relatively higher across every territory compared to foreign nationals within India. 
2. Confirmed cases were highest in territory 27 and lowest in territory 5,6 and 31 
3. There was a higher correlation between people contracting COVID-19 and being cured compared to contracting and not surviving relative to confirmed cases in the different territories. In other words, territory 27 had the highest confirmed cases but more people survived compared to losing their life. 
4. Comparing men to females in terms of vaccination status, there was slightly more males vaccinated compared to females 
5. Most people who received the first dose went on to receive the second dose of vaccinations 
6. Lastly, Haryana had the highest level of testing while Dadra had the lowest testing data and in Dandra there was a higher level of positive COVID-19 cases compared to Haryana 

