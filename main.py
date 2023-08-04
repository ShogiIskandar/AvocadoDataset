#import libraries
import streamlit as st
import pandas as pd
import warnings
from PIL import Image

warnings.filterwarnings("ignore")



#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Avocado Pricing In America")

#adding discription to your website
st.header('Team members')

st.write("Hi! My name is Erin Wu and I'm an incoming Sophophore. I have had no previous experience in coding and joined AI camp in order to better my understanding of AI.")

st.write("Hi I'm Shogi Iskandar and I'm a freshman and the only previous experience I've had with coding is Scratch. I joined AI Camp to learn more about how AI works and how to use it.")

st.write("My name is Thor Wikman I am taking high school classes and have taken three courses on coding. I enrolled in AI camp to continue to expand my knowledge of coding and AI")

st.write("I'm Allison Chan and I'm a rising sophomore. I haven't had any prior experience in coding. I joined this class to learn more about Ai and how it works. "  )


st.header('Context to the Dataset')

st.write('This website is designed to cover the statistics of Avocado pricing and volume of avocados sold across different cities in America. It offers a variety of data such as when the avocados were sold, what price were they, how many were there, and how large the bag they were sold in was. This is important as it can be used to show averages of data across a common product which can show inflation in prices of average good and how much of a good people are buying across a country.')


st.header('Dataset')
image = Image.open('Avocado Dataset.png')
st.image(image, caption="This shows all the data that will be used througout the article")


st.header("The Range Of Average Avocado Pricing Over Time: Shogi")

st.header('Hypothesis 1: How does the average price of the avocado change over time?')

st.write("The following graph shows the daily average price for avocados across America from 2015 to 2018. The reason for showing the price of every date is that when the data comes together you can see trends of spikes and drops among the pricing.")
image = Image.open('AveragePrice - Date.png')
st.image(image, caption='An interesting observation that can be made here is that about 3/4ths of the way through the graph you can see that the minimum price of the avocado rises dramatically.')

st.write("This following graph is a more compresssed version of the former one which shows the full year average rather than the day. This can be used to show more pronounced changes as you can see the peak and minimum price for each year.")
image = Image.open('AveragePrice - Year.png')
st.image(image, caption='An intresting thing to observe on this graph is that during 2018 the highest price of the avocado is much lower than the two years before it')


st.header("Small Bags vs Large Bags Sold")

image = Image.open('SmallvsLargeBags.png')
st.image(image, caption='About a 1:3 ratio between small bags vs large bags sold')
st.write("This graph is a scatterplot that shows an the distribution between the bags sold. There is a pretty even distribution with the data being really compact at zero but presenting more spread as the numbers grow larger. You can see that for about every one small bag sold, about 2-3 large bags are sold as well.")

st.header("Average price vs the total volume")

image = Image.open('Averagepricetotalvolume2.png')

st.image(image, caption="This scatterplot increases in price to $1.35 as the total volume decreases from 119 thousand to 51 thousand")

st.write("The following graph is a rougher line graph that is less compressed yet still helps to strengthen the clear pattern.")

image = Image.open('Averagepricetotalvolume.png')

st.image(image, caption="This graph shows that as the total volume of avocados decreased the average price of the avocados increased.")

st.write("There is a clear pattern between the average price and the total volume within both graphs. There is a correlation, as the total volume decreases the average price increases. This is a perfect example of supply and demand, as the supply decreases the price increases and as the supply increases the price decreases.")


st.header("Comparing Total Volume and the Date")
image = Image.open('avocados.png')

st.image(image, caption="This graph shows the differences between the total volume in avocados and the date it was recorded. ")

st.write ("The graph shows that there is not really any pattern on how the total volume and date relate to each other. ALl the data on the graph are kind of scattered around.")


st.header('Conclusion')

st.write("The data shows that their is a correlation between total volume of the avocados and the average price of avocados. As the total volume decreases the average price increases. The data also shows that there is no clear pattern between the total volume and the date. As well as there is aboout a 1:3 ratio between small bags and large bags. And to top it all off the price of avocados fluctuate over time")