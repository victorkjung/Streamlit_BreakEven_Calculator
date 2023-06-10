import streamlit as st
import time

st.title(':smile: Break-Even Analysis')
st.title('How many :red[units] do you need to sell?')

# Inputs
units = int(st.text_input('Guess the Number of units', value='100').replace(',', ''))
sell_price_per_unit = float(st.text_input('Selling price per unit', value='50.00').replace(',', ''))
total_fixed_costs = float(st.text_input('Total fixed costs', value='1000.00').replace(',', ''))
variable_costs_per_unit = float(st.text_input('Variable cost per unit', value='10.00').replace(',', ''))

# Creating a progress bar
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Calculating: {i+1}%')
    bar.progress(i + 1)
    time.sleep(0.01)

# Calculate total revenue and total costs
total_revenue = units * sell_price_per_unit
total_variable_costs = units * variable_costs_per_unit
total_costs = total_fixed_costs + total_variable_costs

# Calculate break-even point
break_even_units = total_fixed_costs / (sell_price_per_unit - variable_costs_per_unit)

# Display the results
st.write(f'Total revenue: ${total_revenue:,.2f}')
st.write(f'Total costs: ${total_costs:,.2f}')
st.write(f':white_check_mark: The break-even point is at {break_even_units:,.2f} units.')

if units >= break_even_units:
    st.write(f':100: With {units:,.2f} units, you have reached the break-even point. :woman-lifting-weights::punch::crown:')
else:
    st.write(f':sos: With {units:,.2f} units, you have :red[not] reached the break-even point. You need to sell {break_even_units - units:,.2f} more units to break even. :sunglasses:')
