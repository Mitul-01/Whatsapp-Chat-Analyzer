import streamlit as st
import preprocess, helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #convert the bytes to string
    data = bytes_data.decode("utf-8")
    df = preprocess.preprocess(data)
    
    st.dataframe(df)
    
    #fetch unique users
    user_list = df["user"].unique().tolist()
    user_list.remove("group notification")
    user_list.sort()
    user_list.insert(0, "Overall")
    
    selected_user = st.sidebar.selectbox("Show Analysis wrt", user_list)
    
    
    if st.sidebar.button("Show Analysis"):
        
        number_messages, words, number_media_messages, links = helper.fetch_stats(selected_user, df)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(number_messages)
            
        with col2:
            st.header("Total Words")
            st.title(words)
        
        with col3:
            st.header("Media Shared")
            st.title(number_media_messages)
            
        with col4:
            st.header("Links Shared")
            st.title(links)
            
        #finding the busy users in the groups
        
        if selected_user == "Overall":
            st.title("Mosy Busy Users")
            y, new_df = helper.most_busy_user(df)
            fig, ax = plt.subplots()
            plt.xticks(rotation =90)
            
            col1,col2 = st.columns(2)
            
            with col1:
                ax.bar(y.index,y.values)
                st.pyplot(fig)
                
            with col2:
                st.dataframe(new_df)
                
        #Word Cloud
        st.title("Word Cloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
       
        #Most Common Words
        most_common = helper.most_common_words(selected_user, df)
        
        fig,ax = plt.subplots()
        
        ax.barh(most_common[0], most_common[1])
        plt.xticks(rotation = 90)
        
        st.title("Most Common words")
        st.pyplot(fig)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
