import streamlit as st
import pandas as pd


st.set_page_config(page_title="SFM Dealer Portal", layout="wide")
col1, col2, col3 = st.columns(3)
col1.image('_Logo_2.png',use_column_width=True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """

st.markdown(hide_default_format,unsafe_allow_html=True)

st.title('RTO Deal Builder')

tab1, tab2, tab3 = st.tabs(['1. Customer Information','2. Trailer Information','3. Contract Information'])

# Initialize a dictionary to store the inputs
input_data = {}

with tab1:
    st.write('Enter Customer Info')
    col1, col2, col3 = tab1.columns(3)
    with col1:
        input_data['last_name'] = st.text_input('Last Name')
        input_data['first_name'] = st.text_input('First Name')
        input_data['street_addr'] = st.text_input('Street Address')
        input_data['city'] = st.text_input('City')
        input_data['state'] = st.text_input('State')
        input_data['zip'] = st.text_input('Zip')
    with col2:
        input_data['dl_no'] = st.text_input('DL#')
        input_data['ss_no'] = st.text_input('SS')
    with col3:
        input_data['home_phone'] = st.text_input('Home Phone')
        input_data['cell_phone'] = st.text_input('Cell Phone')
        input_data['employer'] = st.text_input('Name of Employer')
        input_data['employer_phone'] = st.text_input('Employer Phone')

with tab2:
    st.write('Enter Trailer Information')
    input_data['trailer_condition'] = st.radio('',['NEW', 'USED'])
    col4, col5, col6 = tab2.columns(3)
    with col4:
        input_data['serial'] = st.text_input('VIN')
        input_data['gps'] = st.text_input('GPS #')
    with col5:
        input_data['brand'] = st.text_input('Trailer Brand')
        input_data['trailer_type'] = st.text_input('Trailer Type')
        input_data['size_l'] = st.text_input('Trailer Length')
        input_data['size_w'] = st.text_input('Trailer Width')
    
def calc_pmt(down_pmt:float, sales_price:float,term:int)->float:
    pass

with tab3:
    st.write('Enter Contract Information')
    input_data['term'] = st.radio('Select Term (months)',[36,48])
    sales_tax_upfront = st.checkbox('Sales Tax Paid Upfront?')
    col7, col8, col9 = tab3.columns(3)    
    with col7:
        input_data['trailer_cost'] = st.number_input('Enter Trailer Cost')
        input_data['sales_price'] = st.number_input('Enter Trailer Cash Price',step=1000)
        input_data['down_payment'] = st.number_input('Enter Renter Down Payment',help='The total amount of Funds the borrower will put toward the RTO contract today')
    with col8:
        input_data['epo'] = st.number_input('Early Payoff Percent',value=0.5,min_value=0.5)
        input_data['sales_taxx_r'] = st.number_input('Sales Tax Rate')
    




