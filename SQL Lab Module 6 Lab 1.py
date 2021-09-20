!pip install sqlalchemy==1.3.9
!pip install ibm_db_sa
%load_ext sql
# Enter the connection string for your Db2 on Cloud database instance below
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name


#Ensure the table 'SCHOOLS' was created in Database
%sql select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA='SCHOOLS'

#or

%sql select * from SYSCAT.TABLES where TABNAME = 'SCHOOLS'

# type in your query to retrieve the number of columns in the SCHOOLS table
%sql select count(*) from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'

# type in your query to retrieve all column names in the SCHOOLS table along with their datatypes and length
%sql select COLNAME, TYPENAME, LENGTH from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'

#Find amount of elementary schools in the data
%sql select count(*) from SCHOOLS where "Elementary, Middle, or High School" = 'ES'

#Find max safety score
%sql select MAX("Safety_Score") from SCHOOLS

#or
%sql select MAX(Safety_Score) AS MAX_SAFETY_SCORE from SCHOOLS

#Find top 10 schools by average student attendance
%sql select "Name_of_School","Average_Student_Attendance" from SCHOOLS ORDER BY "Average_Student_Attendance" DESC nulls last LIMIT 10

#find list of 5 schools with lowest average student attendance
%sql select "Name_of_School","Average_Student_Attendance" FROM SCHOOLS ORDER BY "Average_Student_Attendance" asc LIMIT 5

#now find the same 5 schools with lowest attendance but replace % sign with blank space
%sql select "Name_of_School", REPLACE("Average_Student_Attendance",'%','') FROM SCHOOLS ORDER BY "Average_Student_Attendance" asc LIMIT 5

#find schools where attendance was below 70%
%sql select "Name_of_School","Average_Student_Attendance" FROM SCHOOLS WHERE DECIMAL("Average_Student_Attendance")<70

#find total enrollment by community area
%sql select "Community_Area_Name", sum("College_Enrollment__number_of_students_") AS TOTAL_ENROLLMENT from SCHOOLS group by "Community_Area_Name"

#find the 5 community areas with the least college enrollment sort in ascending
%sql select "Community_Area_Name", sum("College_Enrollment__number_of_students_") AS TOTAL_ENROLLMENT from SCHOOLS group by "Community_Area_Name" ORDER BY TOTAL_ENROLLMENT asc LIMIT 5

