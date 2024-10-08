import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.title("Indian Sencus")
st.text("Choose Options From Side Bar")
df=pd.read_csv('india.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')


st.sidebar.title("Indian Data Viz")

selected_state=st.sidebar.selectbox('Select a State',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Overall India':
        st.text('Size Represents primary parameter')
        st.text('Color Represents secondary parameter ')
        #plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=3,
                                mapbox_style="carto-positron",width=1200,height=700, hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    else:
        st.text('Size Represents primary parameter')
        st.text('Color Represents secondary parameter ')
        #plot for state
        state_df=df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=5,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)





