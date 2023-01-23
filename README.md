# Students-Performance-Analysis-Using-Python

## Introduction

Analyzing student work is an essential part of teaching. Teachers assign, collect and examine student work all the time to assess student learning and to revise and improve teaching.Student assessment enables instructors to measure the effectiveness of their teaching by linking student performance to specific learning objectives. As a result, teachers are able to institutionalize effective teaching choices and revise ineffective ones in their pedagogy.Performance Analysis (PA) is a gathering data methodology that represents an objective observation system that provides useful information to improve performance.Ongoing assessment of student learning allows teachers to engage in continuous quality improvement of their courses. Many factors can influence a student's performance, including the influence of the parents' educational background, test preparation, student health, and so on.

### Loading libraries and data

![image](https://user-images.githubusercontent.com/105121789/214106466-3d0ec004-efa8-4388-9c84-f9d8643733ce.png)

![image](https://user-images.githubusercontent.com/105121789/214106541-3da47f76-10c4-4e39-a980-1ac99dec1467.png)

## Quick look at the data

### Description of the dataset :

![image](https://user-images.githubusercontent.com/105121789/214106947-9da01a4b-6f24-4f0a-a1a7-4767a47249b5.png)

The dataset has 1000 rows and 8 columns.

#### Checking if the data has some missing values.

![image](https://user-images.githubusercontent.com/105121789/214107568-d27454f9-b0c0-4643-a6ff-1cffe1081e94.png)

There are no missing values in the dataset.

#### Checking if the datatype of all the column values.


![image](https://user-images.githubusercontent.com/105121789/214107899-180b399f-6a8f-415a-82d7-954bc017a89b.png)


#### Analyze the values of the columns and check whether they are numerical or categorical.

![image](https://user-images.githubusercontent.com/105121789/214108517-a253b78d-3d21-4e09-b7f3-e3c9cf24b6d1.png)

There 5 categorical columns and 3 numerical columns
The dataset has no null or duplicate values

Attribute Information

Categorical columns are:

Gender: Male or Female
Race/ethnicity: 5 groups, from group A to group E
Parental level of education: from high school to a master’s degree
lunch: free/reduced or standard.
Numerical columns are:

Math score: out of 100
Reading score: out of 100
Writing score: out of 100
The dataset contains the data of about 1000 students. This analysis aims to understand the influence of important factors such as parental level of education, the status of test preparation course etc. on the performance of the students in the exams.


## Data Prep

#### Adding columns “total” and “average” to the dataset.

![image](https://user-images.githubusercontent.com/105121789/214110160-d6f42a8c-df70-4f98-be5d-7b1b9ffba690.png)

## Data Visualization 

![image](https://user-images.githubusercontent.com/105121789/214111378-f30aaa70-8101-498b-852e-e1b379d58cde.png)

![image](https://user-images.githubusercontent.com/105121789/214111848-641d2c6e-38e8-441b-bbdb-345fce7c90bb.png)

### Comparing the number of total male and female students

![image](https://user-images.githubusercontent.com/105121789/214114163-2d5be005-c8c4-4814-ad20-1ed580e2fb36.png)

Out of the total number of students, 51.89% are females while 48.20% are males.


#### Analyzing the average score of all the students on the basis of “race/ethnicity”, “parental level of education”, “test preparation course”.

![image](https://user-images.githubusercontent.com/105121789/214112342-27d3a252-ab46-4b8d-9b86-b0a2a57eb3a1.png)

#### Analyzing the data on the basis of the no. of students who failed or passed the exam.

We can see the no. of students who passed or failed from the below code.

![image](https://user-images.githubusercontent.com/105121789/214112909-04f8f6c5-c924-40d8-931b-55dd01c42980.png)

![image](https://user-images.githubusercontent.com/105121789/214113238-56411af2-98cf-41cf-a8ea-519d7e9bebf3.png)

![image](https://user-images.githubusercontent.com/105121789/214113420-bd1f996b-643c-4e16-bd94-46d34d7ce3e8.png)

![image](https://user-images.githubusercontent.com/105121789/214113475-d102e90b-cd5c-40be-8676-a2b73856c695.png)

