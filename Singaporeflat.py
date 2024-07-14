import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(layout="wide")

# Add a title to your Streamlit app
st.markdown('<h1 style="color:#B22222;">Singapore Flats - Resale Price Predictor</h1>', unsafe_allow_html=True)
st.write("**The Best Price Predictor!**")

#set up the sidebar with optionmenu

task = option_menu("",options=["Home","Prediction","Regulations & Policies","About"],
                        icons=["house","cash","check","info-circle"],
                        default_index=1,
                        orientation="horizontal",
                            styles={"container": {"width": "100%", "border": "2px ridge", "background-color": "#006400"},
                                    "icon": {"color": "#F8CD47", "font-size": "20px"}, 
                                    "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "color": "#FFFFFF"},
                                    "nav-link-selected": {"background-color": "#000000", "color": "#FFFFFF"}})

if task == 'Home':

    st.write('')


    # Load the image
    image_path = "build-to-order-bto-flats-singapore-cover.jpg"
    image = Image.open(image_path)

    # Resize the image to Facebook cover size (851x315)
    resized_image = image.resize((851, 315))

    # Display the resized image
    st.image(resized_image, caption='Singapore Flats Housing Board')

    st.subheader('''Singapore's public housing, managed by the Housing and Development Board (HDB),plays a crucial role in providing affordable homes to the majority of Singaporeans.
                    Here are some information about Singapore flats and the Housing landscape:''')

    st.subheader(':green[HDB Flats :]')

    st.markdown(''' These are public housing apartments built and managed by the Housing and Development Board. They come in various types, such as:''')
    
    st.markdown('''**Build-To-Order (BTO) :** Newly constructed flats offered for sale directly by HDB. Buyers can select the location and type of flat before construction begins.''')

    st.markdown('''**Sale of Balance Flats (SBF) :** Unsold flats from previous BTO launches or repossessed flats put up for sale.''')

    st.markdown('''**Resale Flats :** Flats sold by current HDB flat owners in the resale market.''')

    st.subheader(':green[Flat Types :]')

    st.markdown('''**1-Room and 2-Room Flexi :** Smaller flats suitable for singles or elderly residents.''')

    st.markdown('''**3-Room, 4-Room, and 5-Room :** Standard family-sized flats with varying numbers of bedrooms.''')

    st.markdown('''**Executive Flats :** Larger flats with additional features like balconies and study rooms.''')

    st.subheader(':green[Leasehold :]')

    st.write('''HDB flats are typically sold on a 99-year leasehold basis, meaning buyers own the flat for 99 years.''')

    st.subheader(':green[Resale Market :]')

    st.write('''In the resale market, buyers can purchase flats directly from existing owners. Prices are influenced by factors such as location, size, age of the flat, and remaining lease duration.''')

    st.subheader(':green[**New Developments :**]')

    st.write('''HDB regularly launches new BTO projects in different estates across Singapore, catering to the housing needs of different demographics.''')

    st.subheader(':green[**Ugrading Programs :**]')

    st.write('''HDB implements upgrading programs to improve the living environment of older estates, including amenities like playgrounds, fitness corners, and upgraded common areas''')

    st.subheader(':green[**Home Ownership :**]')

    st.write('''Singapore encourages home ownership through schemes like the Central Provident Fund (CPF) Housing Grant and Housing Loan for first-time buyers''')

    st.subheader(':green[**Integrated Townships :**]')

    st.write('''HDB estates are often integrated with amenities such as schools, shopping centers (like HDB Hub), transportation hubs, and parks.''')

    st.subheader(':green[**Green Initiatives :**]')

    st.write('''Recent developments focus on sustainability and green living, incorporating features like energy-efficient lighting, solar panels, and eco-friendly designs.''')

    st.subheader('''Overall, Singapore's public housing system aims to provide affordable, quality homes for its residents while promoting community living and sustainable urban development.''')

class option():


    town_values=['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
                    'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST','KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
                    'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN','LIM CHU KANG', 'BUKIT PANJANG', 'PASIR RIS', 'SEMBAWANG','PUNGGOL']

    town_encoded = {"ANG MO KIO" : 0,"BEDOK" : 1,"BISHAN" : 2,"BUKIT BATOK" : 3,"BUKIT MERAH" : 4,"BUKIT PANJANG" : 5,"BUKIT TIMAH" : 6,"CENTRAL AREA" : 7,
                    "CHOA CHU KANG" : 8,"CLEMENTI" : 9,"GEYLANG" : 10, "HOUGANG" : 11, "JURONG EAST" : 12, "JURONG WEST" : 13,"KALLANG/WHAMPOA" : 14, "LIM CHU KANG" : 15,
                    "MARINE PARADE" : 16, "PASIR RIS" : 17, "PUNGGOL" : 18, "QUEENSTOWN" : 19, "SEMBAWANG" : 20, "SENGKANG" : 21, "SERANGOON" : 22,
                    "TAMPINES" : 23, "TOA PAYOH" : 24, "WOODLANDS" : 25, "YISHUN" : 26}
    
    flat_type_values = ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE','MULTI GENERATION', '1 ROOM']

    flat_type_encoded = {"1 ROOM" : 0,"2 ROOM" : 1,"3 ROOM" : 2,"4 ROOM" : 3,"5 ROOM" : 4,"EXECUTIVE" : 5,"MULTI GENERATION" : 6}
    
    floor_area_sqm_values=[ 73. ,  67. ,  82. ,  88. ,  89. ,  74. ,  83. ,  68. ,  75. , 81. ,  91. ,  92. ,  97. ,  90. ,  98. ,  99. , 100. ,  93. ,
                            103. , 119. , 120. , 118. , 121. , 135. , 117. ,  45. ,  65. ,59. ,  76. ,  84. , 104. , 105. , 125. , 132. , 139. , 123. ,
                            143. , 151. ,  69. , 106. , 107. , 116. , 149. , 141. , 146. ,148. , 145. , 154. , 150. ,  61. ,  70. ,  63. ,  64. ,  72. ,
                            60. ,  66. ,  54. ,  77. , 133. , 131. , 115. ,  53. ,  43. ,38. ,  58. ,  85. , 111. , 101. , 112. , 137. , 127. , 147. ,
                            163. , 102. ,  83.1, 126. , 140. , 142. ,  71. , 108. , 144. ,96. , 114. , 157. , 152. , 155. ,  87. , 109. , 110. ,  94. ,
                            134. , 122. , 128. ,  49. ,  86. , 156. ,  79. ,  80. ,  78. ,124. ,  52. , 113. ,  95. , 160. , 136. , 138. , 161. ,  39. ,
                            130. , 159. ,  62. ,  51. ,  48. ,  56. ,  64.9, 129. ,  57. ,55. ,  40. ,  46. , 153. , 166. , 165. ,  73.1,  41. ,  74.9,
                            164. , 158. ,  60.3,  50. , 173. ,  42. ,  47. , 171. ,  31. ,63.1,  68.2,  44. , 169. ,  67.2,  37. ,  29. ,  64.8,  74.8,
                            59.2,  59.1,  28. ,  69.9, 162. , 170. ,  48.1,  56.4,  75.9,69.7,  69.2, 172. , 168. , 167. , 152.4,  64.7, 131.1,  89.1,
                            88.1,  87.1,  34. ,  35. ,  68.8]
    
    flat_model_values=['new generation', 'improved', 'model a', 'standard', 'simplified', 'model a-maisonette', 'apartment', 'maisonette', 'terrace',
                        'improved-maisonette', 'multi generation', '2-room','premium apartment', 'adjoined flat', 'premium maisonette',
                        'model a2', 'dbss', 'type s1', 'premium apartment loft', 'type s2','3gen']

    flat_model_encoded = {"2-room" : 0, "3gen" : 1,"adjoined flat" : 2,"apartment" : 3,"dbss" : 4,"improved" : 5,"improved-maisonette" : 6,
                            "maisonette" : 7,"model a" : 8,"model a-maisonette" : 9,"model a2" : 10,"multi generation" : 11,"new generation" : 12,
                            "premium apartment" : 13,"premium apartment loft" : 14, "premium maisonette" : 15,"simplified" : 16,"standard" : 17,
                            "terrace" : 18,"type s1" : 19,"type s2" : 20}
    
    lease_commence_year_values=[1976, 1977, 1978, 1979, 1984, 1980, 1985, 1981, 1982, 1986, 1972, 1983, 1973, 1975, 1974, 1967, 1969, 1970, 
                                1971, 1988, 1968, 1987, 1989, 1990, 1992, 1993, 1994, 1991, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 1966,
                                2002, 2006, 2003, 2005, 2004, 2008, 2007, 2009, 2010, 2012, 2011, 2013, 2014, 2015, 2016, 2017, 2018]
    
    year_values = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                    2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    
    month_values = [1,2,3,4,5,6,7,8,9,10,11,12]

    remaining_lease_values=[54]

if task == 'Prediction':
    title_text = '''<h1 style='font-size: 32px;text-align: center;color:#B22222;'>SGP - Flat Resale Price Prediction</h1>'''
    st.markdown(title_text, unsafe_allow_html=True)
    

    st.markdown("<h5 style=color:#006400>Provide the following Information:",unsafe_allow_html=True)
    st.write('')

    # creted form to get the user input 
    with st.form('prediction'):

        col1,col2=st.columns(2)

        with col1:

            Town_Name=st.selectbox(label='**Town Name**',options=option.town_values,index=None)

            Flat_type=st.selectbox(label='**Flat Type**',options=option.flat_type_values,index=None)

            Floor_area_sqm=st.selectbox(label='**Floor Area in Sqm [min=28.0 , max=173.0]**',options=option.floor_area_sqm_values,index=None)

            Flat_model=st.selectbox(label='**Flat Model**',options=option.flat_model_values,index=None)

            Lease_Commence_year=st.selectbox(label='**Lease Commence Year**',options=option.lease_commence_year_values,index=None)
        
        with col2:

            Year=st.selectbox(label='**Year [From 1990 to 2024]**',options=option.year_values,index=None)

            Month=st.selectbox(label='**Month [Jan - Dec]**',options=option.month_values,index=None)

            Remaining_Lease = st.selectbox(label='**Remaining Lease**',options=option.remaining_lease_values,index=None)

            Price_per_sqm=st.number_input(label='**Price Per Sqm [min=22.87 , max=89.32]**',min_value=22.869193252058544,max_value=89.31965069345043)

            st.markdown('<br>', unsafe_allow_html=True)
            
            button=st.form_submit_button(':red[**PREDICT**]',use_container_width=True)

    if button:

    #check whether user fill all required fields

        if not all([Town_Name, Flat_type, Flat_type, Flat_model, Lease_Commence_year, Year,
                    Month, Remaining_Lease, Price_per_sqm]):
            
            st.error("Data Missing, Complete all the information above.")

        else:
            
            #opened pickle model and predict the selling price with user data
            with open('model_SG_resale_price.pkl','rb') as files:
                predict_model=pickle.load(files)

            # customize the user data to fit the feature 
            Town_Name=option.town_encoded[Town_Name]
            Flat_type=option.flat_type_encoded[Flat_type]
            Flat_model=option.flat_model_encoded[Flat_model]

            #predict the selling price with regressor model
            input_data=np.array([[Town_Name, Flat_type, Flat_type, Flat_model, Lease_Commence_year, Year,
                                    Month, Remaining_Lease, Price_per_sqm]])
            
            input=predict_model.predict(input_data)

            predict_resale_price = input[0] ** 2

            #display the predicted selling price 
            st.subheader(f":green[Predicted Resale Price :] {predict_resale_price:.2f}") 
            st.balloons()

if task == "Regulations & Policies":

    st.subheader('''The resale of flats in Singapore is governed by various policies and regulations set by the Housing & Development Board (HDB) and other relevant authorities.
                    Here are some key policies and details regarding resale of HDB flats in Singapore:''')
    
    st.subheader(":green[Eligibility Criteria for Resale :]")
    st.markdown(''' **1. Ownership Eligibility:** To be eligible to sell an HDB flat, the seller must meet certain ownership criteria, such as fulfilling the Minimum Occupation Period (MOP), which is typically 5 years for most flats.''')
    st.markdown(''' **2. Citizenship/Permanent Residency:** The seller and all co-owners must be Singapore citizens or Permanent Residents.''')
    st.markdown(''' **3. Financial Eligibility:** Sellers may need to repay any outstanding housing loans and fulfill other financial obligations before selling their flats.''')

    st.subheader(":green[Resale Procedure :]")
    st.markdown(''' **1. Engaging an Agent:** Sellers may engage a licensed property agent to assist with the sale process, including marketing the flat, arranging viewings, and negotiating with buyers.''')
    st.markdown(''' **2. Resale Application:** Sellers and buyers must submit a resale application to HDB through the HDB Resale Portal or a property agent.''')
    st.markdown(''' **3. Resale Checklist:** Both parties must complete a resale checklist provided by HDB, which outlines important steps and documents required for the resale transaction.''')
    st.markdown(''' **4. Resale Price:** The resale price of the flat is determined through valuation by HDB or a professional valuer, taking into account factors such as location, size, age, and market conditions.''')
    st.markdown(''' **5. Resale Levy:** Sellers who purchased their new flat from HDB or took advantage of housing subsidies may be subject to a resale levy, which is payable upon resale of the flat.''')

    st.subheader(":green[Policies and Regulations :]")
    st.markdown(''' **1. Minimum Occupation Period (MOP):** Owners must fulfill the MOP before they can sell their HDB flat on the open market.''')
    st.markdown(''' **2. HDB Loan Eligibility:** Buyers must meet HDB's eligibility criteria to obtain an HDB housing loan for the purchase of resale flats.''')
    st.markdown(''' **3. Ethnic Integration Policy (EIP):** The EIP ensures a balanced ethnic mix in HDB estates by restricting the sale and purchase of flats to maintain racial harmony.''')
    st.markdown(''' **4. Singapore Permanent Resident (SPR) Quota:** The SPR quota limits the number of flats that can be sold to non-citizens or Permanent Residents in each HDB block or neighborhood.''')
    st.markdown(''' **5. Enhanced CPF Housing Grant (EHG):** Eligible buyers may receive government grants, such as the EHG, to assist with the purchase of resale flats..''')

    st.subheader(":green[Other Considerations :]")
    st.markdown(''' **1. Valuation and Financing:** Buyers and sellers should consider the valuation of the flat and their financing options, including housing loans, before proceeding with the resale transaction.''')
    st.markdown(''' **2. Legal and Financial Advice:** It is advisable for both parties to seek legal and financial advice to understand their rights, obligations, and potential costs associated with the resale process.''')

    st.write("")
    st.subheader('''Overall, the resale of HDB flats in Singapore is governed by a set of policies and procedures aimed at ensuring a fair and transparent resale market while meeting the housing needs of Singapore residents.''')



#set up information for 'About' menu 
if task == "About":
    st.subheader(':green[Project Title :]')
    st.markdown('<h5> Singapore Flats Resale Price Prediction',unsafe_allow_html=True)

    st.subheader(':green[Processes :]')
    st.markdown(' <h5> Python scripting, Data Preprocessing, Machine learning, Exploratory Data Analysis, Streamlit',unsafe_allow_html=True)

    st.subheader(':green[Information :]')
    st.markdown('''**This Project - Singapore Flats Resale Price Prediction Webapp was done by myself, :red[**NAGAPPAN M.S**]**''')
    st.markdown('''**To refer codes of this project, refer my Github page by clicking on the button below**''')
    st.link_button('**Go to Github**',' ')