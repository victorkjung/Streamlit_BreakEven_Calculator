import streamlit as st
import time

st.title('Break-Even Analysis Calculator')

# Inputs
units = st.number_input('Number of units', value=100, step=10)
sell_price_per_unit = st.number_input('Selling price per unit', value=50.0)
total_fixed_costs = st.number_input('Total fixed costs', value=1000.0)
variable_costs_per_unit = st.number_input('Variable cost per unit', value=10.0)

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
st.write(f'Total revenue: ${total_revenue}')
st.write(f'Total costs: ${total_costs}')
st.write(f'The break-even point is at {break_even_units} units.')

if units >= break_even_units:
    st.write(f'With {units} units, you have reached the break-even point.')
else:
    st.write(f'With {units} units, you have not reached the break-even point. You need to sell {break_even_units - units} more units to break even.')
