import time

st.sidebar.title("Break Even Analysis Calculator")

# Add a description to the sidebar
st.sidebar.write("Welcome to the Break Even Analysis Calculator. This tool helps you determine the point at which your total revenue equals your total costs, allowing you to break even.")

# Add instructions to the sidebar
st.sidebar.subheader("Instructions:")
st.sidebar.write("1. Enter the values for your inputs in the respective fields.")
st.sidebar.write("2. Click on the 'Calculate' button to see the results.")

st.title(':smile: Break-Even Analyzer')
st.title('How many :red[_units_] do you need to sell?')

# Inputs
units = int(st.text_input('Guess the Number of units', value='0'))
sell_price_per_unit = float(st.text_input('Selling price per unit', value='10.00'))
variable_costs_per_unit = float(st.text_input('Variable cost per unit', value='5.00'))

# Calculate total fixed costs
total_fixed_costs = hourly_payroll + salaried_payroll + consultants + security + workers_compensation + other_payroll_expense + rent + maintenance + repairs + electric_utilities + property_insurance + gl_insurance + epli_insurance + other_insurance + pos + internet + phone + other_operating_expense

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
    st.markdown(f'<h4>&#x2705; With {units} units, you have reached the break-even point. &#x1F3CB;&#x200D;&#x2640;&#xFE0F;&#x1F44A;&#x1F451;</h4>', unsafe_allow_html=True)
else:
    units_needed = break_even_units - units
    st.markdown(f'<h3>&#x1F198; With {units} units, you have <font color="red">not</font> reached the break-even point. You need to sell {units_needed:,.2f} more units to break even. &#x1F60E;</h3>', unsafe_allow_html=True)
