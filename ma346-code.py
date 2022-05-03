#MA346
#Juliana Spitzner, Gaby Hernandez Arias, and Luke Orysiuk

from ssl import Options
from turtle import listen
import streamlit as st
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter

#title & header
st.title('Heart Disease Analysis Project')
st.write('Project by: Juliana Spitzner, Gaby Hernandez Arias, and Luke Orysiuk')
st.write(' ')
#import dataset
df = st.cache(pd.read_csv)("heart.csv")
#CHECKBOX: Explore Initial Dataset
view_df = st.sidebar.checkbox("Explore Initial Dataset")
if view_df:
    st.subheader('Initial Heart Disease Dataset')
    st.write(df)
    st.subheader('Variable Definitions')
    st.subheader("HeartDisease")
    st.write("Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI)")
    st.subheader("PhysicalHealth")
    st.write("Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30")
    st.subheader("MentalHealth")
    st.write("Thinking about your mental health, for how many days during the past 30 days was your mental health not good?")

#CHECKBOX: Explore Merged Dataset
view_df_merged = st.sidebar.checkbox("Explore Merged Dataset")
if view_df_merged:
    #Merge 2 datasets
    dataframe_1 = pd.read_csv ('heart.csv')
    #Aggregate dataframe 1
    df1_aggregated = dataframe_1.groupby("Sex")
    #Second dataset to merge with:
    #https://www.kaggle.com/datasets/nareshbhat/health-care-data-set-on-heart-attack-possibility 
    #Prepare second dataset for merge
    dataframe_2 = pd.read_csv ('heart2.csv')
    #Group second dataset by sex (f/m) as well
    df2_aggregated = dataframe_2.groupby("sex")
    #Count aggregated dataframes
    df1_final = df1_aggregated.count()
    df1_final.reset_index(inplace=True)
    df2_final = df2_aggregated.count()
    df2_final.reset_index(inplace=True)
    #Re-name values in column, 0: Female, 1: Male
    df2_final["sex"].replace({0: "Female", 1: "Male"}, inplace=True)
    #Merge both datasets 
    merged_df = pd.concat([df1_final.set_index('Sex'),df2_final.set_index('sex')], axis=1, join='inner')
    #Show merged dataset
    st.write("Count of variables between Male & Female")
    st.write(merged_df.head())
    #Mean aggregated dataframes
    df1_final_mean = df1_aggregated.mean()
    df1_final_mean.reset_index(inplace=True)
    df2_final_mean = df2_aggregated.mean()
    df2_final_mean.reset_index(inplace=True)
    #Re-name values in column, 0: Female, 1: Male - mean
    df2_final_mean["sex"].replace({0: "Female", 1: "Male"}, inplace=True)
    #Merge both datasets - mean
    merged_df_mean = pd.concat([df1_final_mean.set_index('Sex'),df2_final_mean.set_index('sex')], axis=1, join='inner')
    #Show merged dataset - mean
    st.write("Means between Male & Female")
    st.write(merged_df_mean.head())


#CHECKBOX: View Age Bar Chart
view_plot = st.sidebar.checkbox("Heart Disease per Age Category")
if view_plot:
    #subset for people with heart disease
    df_yes = df.loc[df["HeartDisease"] == "Yes"]
    #count people with heart disease in each age category
    age_df=df_yes.groupby('AgeCategory')[["HeartDisease"]].count()
    #count total people in each age category (both with and without heart disease)
    age_df['Total in Age Group']=df.groupby('AgeCategory')[["HeartDisease"]].count()
    #get ratio of people with heart disease to total number of people in each age category
    age_df['Ratio with Heart Disease']=age_df['HeartDisease']/age_df['Total in Age Group']
    #color picker for bar color
    color = st.color_picker('Pick A Bar Color', '#B9159D')
    #get indicies of dataframe with the count of total people in each age category 
    index = age_df.index
    #list of all age categories
    ages = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']
    #slider to customize age range to look at
    start_age, end_age = st.select_slider(
        'Select a range of ages',
        options=['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'],
        value=('18-24', '80 or older'))
    st.write('You selected ages between', start_age, 'and', end_age)
    c = 
    for op in options:
        if 
    
    #create bar chart of percent with heart disease for each age category
    fig, ax = plt.subplots()
    plt.bar(index, age_df['Ratio with Heart Disease'], color=color)
    #rotate values on x axis for readability
    plt.xticks(rotation = 45)
    plt.xlabel('Age Category')
    plt.ylabel('Percent of Adults with Heart Disease')
    plt.title('Percent of Adults with Heart Disease per Age Category')
    #format y axis values to show percentage format
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    #show plot 
    st.pyplot(fig)
    #show age dataframe 
    st.write(age_df)

#CHECKBOX: View Grouped Bar Chart
view_pivot = st.sidebar.checkbox("Heart Disease by BMI, Physical Health, Mental Health, and Sleep Time")
if view_pivot:
    #create dataframe of means of values for people with heart disease and those without
    df_bar = df.groupby('HeartDisease').mean()
    #allow user to select which categories to view in the bar chart
    cats = st.multiselect("Choose categories to view the mean of:", ('BMI','PhysicalHealth','MentalHealth','SleepTime'), default=('BMI','PhysicalHealth','MentalHealth','SleepTime'))
    #create dataframe with selected categories
    df_cats = pd.DataFrame({})
    for category in cats:
        df_cats[category] = df_bar[category]
    st.write(df_cats)
    #transpose df_cats
    df_cats_T = df_cats.T
    index = df_cats_T.index

    #create list of indicies of df_cats_T
    list = []
    for val in index:
        list.append(val)

    #create grouped bar chart
    fig, ax = plt.subplots()
    noHeartDisease = df_cats_T["No"]
    yesHeartDisease = df_cats_T["Yes"]
    
    X_axis = np.arange(len(list))
    
    plt.bar(X_axis - 0.2, noHeartDisease, 0.4, label = 'No Heart Disease', color='green')
    plt.bar(X_axis + 0.2, yesHeartDisease, 0.4, label = 'Heart Disease', color='red')
    plt.xticks(X_axis, list)
    plt.xlabel("Category")
    plt.ylabel("Mean Amount")
    plt.title("Means for Each Category per Heart Disease")
    plt.legend()
    plt.show()
    #show grouped bar chart
    st.pyplot(fig)

#CHECKBOX: View Pie Charts
#Pie charts showing the correlation between mental and physical health and heart disease
view_pie = st.sidebar.checkbox("Mental and Physical Health & Heart Disease")
if view_pie:
    #separating the dataframe into to new datadrames dfh for healthy hearts and dfn for non healthy hearts
    dfh = df[df['HeartDisease'].str.contains("Yes")]
    dfn = df[df['HeartDisease'].str.contains("No")]

    #creating a labels key for the pie chart
    labels = ['Zero Risk', 'Low Risk', 'High Risk', 'Med Risk']

    #MENTAL HEALTH
    st.subheader("Mental Health & Heart Disease")
    #create two columns to put display mental health pie charts next to each other
    col1, col2= st.columns(2)
    with col1:    
        col1.header = "mental health x heart disease"
        fig1, ax1 = plt.subplots()
        #creating bins in 10 point increments to group the data on different levels of mental health
        mh = dfh['MentalHealth'].value_counts(bins = [0, 0.5, 10, 21, 31])
        #plotting the pie chart for heart disease
        mh.plot.pie(figsize=(11, 6), autopct='%1.1f%%', labels=labels)
        plt.title('Mental Health for People with Heart Disease')
        #show pie chart
        st.pyplot(fig1)
    with col2:
        col2.header = "mental health x no heart disease"
        fig2, ax2 = plt.subplots()
        #creating bins in 10 point increments to group the data on different levels of mental health
        mn = dfn['MentalHealth'].value_counts(bins = [0, 0.5, 10, 21, 31])
        #plotting the pie chart for no heart disease
        mn.plot.pie(figsize=(11, 6), autopct='%1.1f%%', labels=labels)
        plt.title('Mental Health for People without Heart Disease')
        #show pie chart
        st.pyplot(fig2)

    #PHYSICAL HEALTH
    st.subheader("Physical Health & Heart Disease")
    #create two columns to put display physical health pie charts next to each other
    col3, col4= st.columns(2)
    with col3:
        #PHYSICAL HEALTH
        fig3, ax3 = plt.subplots()
        #creating bins in 10 point increments to group the data on different levels of physical health
        ph = dfh['PhysicalHealth'].value_counts(bins = [0, 0.5, 10, 21, 31])
        #plotting the pie chart for heart disease
        ph.plot.pie(figsize=(11, 6), autopct='%1.1f%%', labels=labels)
        plt.title('Physical Health for People with Heart Disease')
        #show pie chart
        st.pyplot(fig3)
    with col4:
        fig4, ax4 = plt.subplots()
        #creating bins in 10 point increments to group the data on different levels of physical health
        pn = dfn['PhysicalHealth'].value_counts(bins = [0, 0.5, 10, 21, 31])
        #plotting the pie chart for no heart disease
        pn.plot.pie(figsize=(11, 6), autopct='%1.1f%%', labels=labels)
        plt.title('Physical Health for People without Heart Disease')
        #show pie chart
        st.pyplot(fig4)

