!pip install sqlalchemy==1.3.9
!pip install ibm_db_sa
%load_ext sql

# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@hostname:port/BLUDB?security=SSL
# Enter the connection string for your Db2 on Cloud database instance below
# i.e. copy after db2:// from the URI string in Service Credentials of your Db2 instance. Remove the double quotes at the end.
%sql ibm_db_sa://

import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
%sql PERSIST chicago_socioeconomic_data

%sql SELECT * FROM chicago_socioeconomic_data limit 5;

#finds the amount of rows in the dataset
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;

#finds amount of communities that have a hardship index greater than 50
%sql select count(*) from chicago_socioeconomic_data where hardship_index>50.0;

#find maximum hardship index from dataset
%sql select MAX(hardship_index) from chicago_socioeconomic_data;

#find community area name with highest hardship index, below is done using a subquery (the subquery is from previous problem / query
%sql select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data )

#find community areas that have per capita income greater than 60,000
%sql select community_area_name from chicago_socioeconomic_data where per_capita_income_ > 60000;


# if the import command gives ModuleNotFoundError: No module named 'seaborn'
# then uncomment the following line i.e. delete the # to install the seaborn package
# !pip install seaborn

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())