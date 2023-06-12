import streamlit as st
import time

st.sidebar.title("Break Even Analysis Calculator")

# Add a description to the sidebar
st.sidebar.write("Welcome to the Break Even Analysis Calculator. This tool helps you determine the point at which your total revenue equals your total costs, allowing you to break even.")

# Add instructions to the sidebar
st.sidebar.subheader("Instructions:")
st.sidebar.write("1. Enter the values for your inputs in the respective fields.")
st.sidebar.write("2. Your cost inputs should be represented as are daily rate. For example, if the weekly hourly payroll is **14,000** per week and you are open seven days a week, then you would input **2000** in the hourly paroll field. And if your property insurance is **36,500** a year, then you would input **100** in the property insurance field.")
st.sidebar.write("3. Variable cost per unit is the wholesale cost of item you are selling. For example if your invoice is **1,200 for 100 units**. You would input **1.20** in variable cost per unit field.")

# About the Developer
st.sidebar.title("About the Developer")
st.sidebar.write("**Victor Jung** is a serial entrepreneur and technology hobbyist. With a passion for innovation and problem-solving, Victor has successfully launched and managed multiple ventures. He combines business acumen with a deep understanding of technology to create impactful solutions.")

st.sidebar.write("The Break Even Analysis Calculator was developed by Victor Jung using **PyCharm**, a powerful integrated development environment (IDE), and **GitHub Co-Pilot**, an AI-powered coding assistant. This collaboration helped streamline the programming process, resulting in efficient code generation and error correction.")

# Guidance for Break Even Analysis Calculator
st.sidebar.subheader("Guidance on Break Even Analysis")
st.sidebar.write("The Break Even Analysis Calculator is a valuable tool for businesses to assess their financial performance. It provides insights into the number of units a business needs to sell in order to cover all costs and break even.")

st.sidebar.write("While the calculator offers a useful estimate, it's important to consult your accountant and bookkeeper to ensure that the inputs accurately reflect your true cost structure. They can help you identify all relevant expenses and provide guidance on calculating costs specific to your business.")

st.sidebar.write("Please use this Break Even Analysis Calculator as a reference to understand the potential number of units needed to break even. Remember to consult professionals for a comprehensive analysis tailored to your business.")

st.title(':smile: Retail Store Dilemna')
st.title('How many :red[_units_] do you need to sell?')

# Inputs
units = int(st.text_input('Guess the Number of units', value='0').replace(',', ''))
sell_price_per_unit = float(st.text_input('Selling price per unit', value='10.00').replace(',', ''))
variable_costs_per_unit = float(st.text_input('Variable cost per unit', value='5.00').replace(',', ''))
hourly_payroll = float(st.text_input('Hourly payroll', value='0.00').replace(',', ''))
salaried_payroll = float(st.text_input('Salaried payroll', value='0.00').replace(',', ''))
consultants = float(st.text_input('Consultants', value='0.00').replace(',', ''))
security = float(st.text_input('Security', value='0.00').replace(',', ''))
workers_compensation = float(st.text_input("Worker's compensation", value='0.00').replace(',', ''))
other_payroll_expense = float(st.text_input('Other payroll expense', value='0.00').replace(',', ''))
rent = float(st.text_input('Rent', value='0.00').replace(',', ''))
maintenance = float(st.text_input('Maintenance', value='0.00').replace(',', ''))
repairs = float(st.text_input('Repairs', value='0.00').replace(',', ''))
electric_utilities = float(st.text_input('Electric utilities', value='0.00').replace(',', ''))
property_insurance = float(st.text_input('Property Insurance', value='0.00').replace(',', ''))
gl_insurance = float(st.text_input('GL insurance', value='0.00').replace(',', ''))
epli_insurance = float(st.text_input('EPLI insurance', value='0.00').replace(',', ''))
other_insurance = float(st.text_input('Other insurance', value='0.00').replace(',', ''))
pos = float(st.text_input('POS', value='0.00').replace(',', ''))
internet = float(st.text_input('Internet', value='0.00').replace(',', ''))
phone = float(st.text_input('Phone', value='0.00').replace(',', ''))
other_operating_expense = float(st.text_input('Other operating expense', value='0.00').replace(',', ''))

# Format inputs with thousand separators
formatted_units = "{:,}".format(units)
formatted_sell_price_per_unit = "{:,.2f}".format(sell_price_per_unit)

# Calculate total fixed costs
total_payroll_expense = hourly_payroll + salaried_payroll + consultants + security + workers_compensation + other_payroll_expense
total_occupancy_expense = rent + maintenance + repairs + electric_utilities + property_insurance + gl_insurance + epli_insurance + other_insurance
total_operating_expense = pos + internet + phone + other_operating_expense
total_fixed_costs = total_payroll_expense + total_occupancy_expense + total_operating_expense

# Format fixed costs with thousand separators
formatted_total_fixed_costs = "{:,.2f}".format(total_fixed_costs)
formatted_total_payroll_expense = "{:,.2f}".format(total_payroll_expense)
formatted_total_occupancy_expense = "{:,.2f}".format(total_occupancy_expense)
formatted_total_operating_expense = "{:,.2f}".format(total_operating_expense)

# Format variable costs with thousand separators and decimals
formatted_variable_costs_per_unit = "{:,.2f}".format(variable_costs_per_unit)

# Display formatted inputs
st.write("**Here are your summary entries:**")
st.write("Number of units:", formatted_units)
st.write("Selling price per unit:", f"${formatted_sell_price_per_unit}")
st.write("Variable cost per unit:", f"${variable_costs_per_unit}")
st.write("Total fixed costs:", f"${formatted_total_fixed_costs}")
st.write("**Here are your fixed cost components:**")
st.write("Total payroll expense:", f"${formatted_total_payroll_expense}")
st.write("Total occcupancy expense:", f"${formatted_total_occupancy_expense}")
st.write("Total operating expense:", f"${formatted_total_operating_expense}")

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
    formatted_units_needed = "{:,.2f}".format(units_needed)
    st.markdown(f'<h3>&#x1F198; With {formatted_units} units, you have <font color="red">not</font> reached the break-even point. You need to sell {formatted_units_needed} more units to break even. &#x1F60E;</h3>', unsafe_allow_html=True)
