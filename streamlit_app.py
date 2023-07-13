import pandas as pd
import numpy as np

import streamlit as st
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objects as go




# Title


# Data Visualization
# Line Chart


def pivot_table(df, val, idx='month', cols='year'):
    return pd.pivot_table(df, values=val, index=idx, columns=cols, aggfunc=sum, margins=True)

# Sample dataframe
df = pd.read_csv("data_updated_07_04_2023.csv")

cols = df.columns[4:]


def main():
    st.title('Pivot Table and Time Series Plot App')

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ["Pivot Tables", "Time Series Plot"])

    if page == "Pivot Tables":
        
    
        years = df['year'].unique()
        years = [int(year) for year in years]
        
        months = df['month'].unique()
        month = [int(month) for month in months]

        # Year range selection using a slider
        year_start, year_end = st.slider('Select year range', min_value=min(years), max_value=max(years), value=(min(years), max(years)))
        month_start, month_end = st.slider('Select month range', min_value=min(month), max_value=max(month), value=(min(month), max(month)))


        # Filter the dataframe based on the selected year range
        filtered_df = df[(df['year'] >= year_start) & (df['year'] <= year_end)]
        filtered_df = filtered_df[(filtered_df['month'] >= month_start) & (filtered_df['month'] <= month_end)]

        # Dropdown menu for selecting the value column
        num_piv = list(range(1,5))
        num_pivots = st.selectbox('Number of Pivots',options =num_piv)

        # Create multiple pivots based on the selected value columns
        for i in range(num_pivots):
            st.header(f'Pivot Table {i+1}')
            # Dropdown menu for selecting the value column
            value_column = st.selectbox(f'Select value column for Pivot {i+1}', options=cols)

            # Display the pivot table
            pivot_df = pivot_table(filtered_df, value_column)
            st.dataframe(pivot_df,width=1500, height=500)

            # Display the corresponding tickers for the pivot
          


    
   
       
    elif page == "Time Series Plot":
        st.header("Time Series Plot")

        dates = df['Period'].unique()
        min_date = dates.min()
        max_date = dates.max()

        # Date range selection using a slider
        date_start, date_end = st.select_slider('Select date range', options = dates, value=(min_date, max_date))

        # Filter the dataframe based on the selected date range
        filtered_df = df[(df['Period'] >= date_start) & (df['Period'] <= date_end)]
        
        
        
        
    

        # Dropdown menu for selecting the value column
        value_columns = st.multiselect('Select value columns', options=cols)

        
        fig = go.Figure()
        colors = ['blue', 'green', 'red', 'orange', 'purple'] 
        # Add initial lines based on the selected value columns
        for i,column in enumerate(value_columns):
            
            x = filtered_df['Period']
            y = filtered_df[column]
            
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column,line=dict(color=colors[i%len(colors)])))
        fig.update_layout(width=1000, height=700)
    

        # Function to handle adding a line when the button is clicked
       
        # Execute the add_line function when the button is clicked
      

        # Display the time series plot
        st.plotly_chart(fig)
        
        
        
        


   


        # Line plot of 'Value' against 'Date'
        
        
    
       



if __name__ == '__main__':
    main()

    
    
    
    


# Number of pivots to create
