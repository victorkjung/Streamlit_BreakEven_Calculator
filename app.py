import streamlit as st
import time
import locale

st.title(':smile: Break-Even Analysis')
st.title('How many :red[_units_] do you need to sell?')

# Set locale to use thousand separators
locale.setlocale(locale.LC_ALL, '')

# Inputs
units = int(st.text_input('Guess the Number of units', value='0').replace(',', ''))
sell_price_per_unit = float(st.text_input('Selling price per unit', value='10.00').replace(',', ''))
total_fixed_costs = float(st.text_input('Total fixed costs', value='1000.00').replace(',', ''))
variable_costs_per_unit = float(st.text_input('Variable cost per unit', value='5.00').replace(',', ''))

# Display formatted inputs
formatted_units = locale.format_string("%d", units, grouping=True)
formatted_sell_price_per_unit = locale.format_string("%.2f", sell_price_per_unit, grouping=True)
formatted_total_fixed_costs = locale.format_string("%.2f", total_fixed_costs, grouping=True)
formatted_variable_costs_per_unit = locale.format_string("%.2f", variable_costs_per_unit, grouping=True)

st.write("Formatted Inputs:")
st.write("Number of units:", formatted_units)
st.write("Selling price per unit:", formatted_sell_price_per_unit)
st.write("Total fixed costs:", formatted_total_fixed_costs)
st.write("Variable cost per unit:", formatted_variable_costs_per_unit)

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

# Display the results with increased font size
st.markdown(f'<h4>Total revenue: ${total_revenue:,.2f}</h3>', unsafe_allow_html=True)
st.markdown(f'<h4>Total costs: ${total_costs:,.2f}</h3>', unsafe_allow_html=True)
st.markdown(f'<h4>:white_check_mark: The break-even point is at {break_even_units:,.2f} units.</h3>', unsafe_allow_html=True)

if units >= break_even_units:
    st.markdown(f'<h3>With {units:,.2f} units, you have reached the break-even point.</h3>', unsafe_allow_html=True)
else:
    st.markdown(f'<h3>With {units:,.2f} units, you have <font color="red">not</font> reached the break-even point. You need to sell {break_even_units - units:,.2f} more units to break even.</h3>', unsafe_allow_html=True)
