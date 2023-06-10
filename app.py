import streamlit as st
import time

st.title(':smile: Break-Even Analyzer')
st.title('How many :red[_units_] do you need to sell?')

# Inputs
units = int(st.text_input('Guess the Number of units', value='0').replace(',', ''))
sell_price_per_unit = float(st.text_input('Selling price per unit', value='10.00').replace(',', ''))
total_fixed_costs = float(st.text_input('Total fixed costs', value='1000.00').replace(',', ''))
variable_costs_per_unit = float(st.text_input('Variable cost per unit', value='5.00').replace(',', ''))

# Format inputs with thousand separators
formatted_units = "{:,}".format(units)
formatted_sell_price_per_unit = "{:,.2f}".format(sell_price_per_unit)
formatted_total_fixed_costs = "{:,.2f}".format(total_fixed_costs)
formatted_variable_costs_per_unit = "{:,.2f}".format(variable_costs_per_unit)

# Display formatted inputs
st.write("Here are your entries:")
st.write("Number of units:", formatted_units)
st.write("Selling price per unit:", f"${formatted_sell_price_per_unit}")
st.write("Total fixed costs:", f"${formatted_total_fixed_costs}")
st.write("Variable cost per unit:", f"${formatted_variable_costs_per_unit}")

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
st.markdown(f'<h4>Total revenue: ${total_revenue:,.2f}</h4>', unsafe_allow_html=True)
st.markdown(f'<h4>Total costs: ${total_costs:,.2f}</h4>', unsafe_allow_html=True)
st.markdown(f'<h4>The break-even point is at {break_even_units:,.2f} units.</h4>', unsafe_allow_html=True)

if units >= break_even_units:
    st.markdown(f'<h4>&#x2705; With {formatted_units} units, you have reached the break-even point. &#x1F3CB;&#x200D;&#x2640;&#xFE0F;&#x1F44A;&#x1F451;</h4>', unsafe_allow_html=True)
else:
    units_needed = break_even_units - units
    formatted_units_needed = "{:,}".format(units_needed)
    st.markdown(f'<h3>&#x1F198; With {formatted_units} units, you have <font color="red">not</font> reached the break-even point. You need to sell {formatted_units_needed} more units to break even. &#x1F60E;</h3>', unsafe_allow_html=True)
