#create database hospital_db;
#use hospital_db;

create table prescription(
	Patient_id varchar(45) not null,
    Patient_name varchar(10) not null,
    DOB varchar(45) not null,
    Age Int not null,
    Gender varchar(45) not null,
    Blood_group varchar(45) not null,
    contact_number Int not null,
    side_effect varchar(45) not null,
    Blood_pressure Int not null,
    Heart_rate Int not null,
    weight Int not null,
    tablet_name varchar(45) not null,
    address varchar(45) not null,
    NoofTablet varchar(45) not null,
    height Int not null,
    further_info varchar(45) not null
    #primary key('Patient_id')
);
    
