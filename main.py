import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns


def val_col_null(df, cols: list[str]):
    null_values = pd.DataFrame(columns=["Column", "Null Count", "Total Count"])
    
    for col in cols:
        null_count = df[col].isnull().sum()
        total_count = len(df)
        null_percentage = round(null_count * 100 / total_count, 2)
        
        null_values = null_values.append({"Column": col, "Null Count": null_count, "Total Count": total_count, "Null Percentage": null_percentage}, ignore_index=True)

    st.title("Null Values Analysis")
    
    # Display null values table
    st.subheader("Null Values in Columns")
    st.table(null_values)

    # Create a diagonal bar plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x="Column", y="Null Count", data=null_values, palette="viridis")
    plt.xticks(rotation=45, ha="right")

    # Add percentage labels on the bars
    for p, percentage in zip(ax.patches, null_values["Null Percentage"]):
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width() / 2,
            height + 0.1,
            f"{percentage:.1f}%",
            ha="center",
            va="bottom",
            fontsize=8,
            color="black"
        )

    plt.title("Null Values Distribution by Column")
    plt.xlabel("Column")
    plt.ylabel("Null Count")

    st.subheader("Histogram: Null Values Distribution")
    st.pyplot(plt)


def analyze_sold_products(df):
    # Group by sold products
    grouped_data = df.groupby('Sold Products')['Paid Amount'].agg(['count', 'sum', 'mean']).reset_index()
    grouped_data.columns = ['Sold Products', 'Total Sales', 'Total Revenue', 'Average Price']

    st.title("Sold Products Analysis")

    # Display table with interesting metrics
    st.subheader("Key Metrics by Sold Products")
    st.table(grouped_data)

    # Plot total sales and average price
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Total Sales
    ax1.bar(grouped_data['Sold Products'], grouped_data['Total Sales'])
    ax1.set_title('Total Sales by Product')
    ax1.set_xlabel('Sold Products')
    ax1.set_ylabel('Total Sales')

    # Average Price
    ax2.bar(grouped_data['Sold Products'], grouped_data['Average Price'])
    ax2.set_title('Average Price by Product')
    ax2.set_xlabel('Product')
    ax2.set_ylabel('Average Price')

    # Adjust layout
    plt.tight_layout()

    st.subheader("Plots: Total Sales and Average Price by Product")
    st.pyplot(fig)


def analyze_sold_products_by_country(df):
    # Group by sold products and country
    grouped_data = df.groupby(['Sold Products', 'Country of payment'])['Paid Amount'].agg(['count', 'sum', 'mean']).reset_index()
    grouped_data.columns = ['Sold Products', 'Country of payment', 'Total Sales', 'Total Revenue', 'Average Price']

    st.title("Sold Products Analysis by Country")

    # Display table with interesting metrics
    st.subheader("Key Metrics by Sold Products and Country")
    st.table(grouped_data)

    # Plot total sales and average price by country
    unique_products = df['Sold Products'].unique()

    for product in unique_products:
        product_data = grouped_data[grouped_data['Sold Products'] == product]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 12))

        # Total Sales
        ax1.bar(product_data['Country of payment'], product_data['Total Sales'])
        ax1.set_title(f'Total Sales of {product} by Country of payment', fontsize=15)
        ax1.set_xlabel('Country of payment', fontsize=15)
        ax1.set_ylabel('Total Sales', fontsize=15)
        ax1.set_xticklabels(product_data['Country of payment'], rotation=90, ha='right',  fontsize=15)

        # Average Price
        ax2.bar(product_data['Country of payment'], product_data['Average Price'])
        ax2.set_title(f'Average Price of {product} by Country of payment',  fontsize=10)
        ax2.set_xlabel('Country of payment', fontsize=15)
        ax2.set_ylabel('Average Price',fontsize=15)
        ax2.set_xticklabels(product_data['Country of payment'], rotation=90, ha='right',  fontsize=15)


        # Adjust layout
        plt.tight_layout()

        st.subheader(f"Plots: {product} - Total Sales and Average Price by Country")
        st.pyplot(fig)


# Load the Excel data
excel_path = "/Users/zappy/Downloads/Dataset M2 Efrei HumanIT 23-24.xlsx"  # Replace with the actual path
df = pd.read_excel(excel_path)

# Sidebar
st.sidebar.title("Data Quality Analysis")

# Show raw data
st.sidebar.subheader("Raw Data")
#st.sidebar.write(df)

# Data Quality Analysis
st.title("Data Quality Analysis")

# Display basic statistics
st.subheader("Basic Statistics")
st.write(df.describe())

# Data Quality Issues
st.subheader("Data Quality Issues")
st.write("1. Incomplete Data:")
val_col_null(df, df.columns)

st.write("2. Inconsistent Data, Amount is a float ?:")
st.write(df.Amount.head())

st.write("3. Data Accuracy:")
# Add code to identify inaccurate data

st.write("4. Data Redundancy:")
# Add code to identify duplicate entries

# Remediation Plan
st.subheader("Remediation Plan")
# Add code to propose a remediation plan

# Key Data Quality Steps
st.title("Key Data Quality Steps")

# Display key data quality steps
st.write("1. Data Profiling:")
# Add code for data profiling

st.write("2. Data Cleaning:")
# Add code for data cleaning

st.write("3. Data Validation:")
# Add code for data validation

# Data Visualization
st.title("Data Visualization Insights")
analyze_sold_products(df)
# Display an example visualization
analyze_sold_products_by_country(df)
# Next Steps
st.title("Next Steps for Data Transformation")
st.write("1. Short Term:")
# Add code for short-term steps

st.write("2. Mid-Term:")
# Add code for mid-term steps

st.write("3. Long Term:")
# Add code for long-term steps

# Q&A and Discussion
st.title("Q&A and Discussion")

# Open the floor for questions and discussions
# Add code for interactive elements or discussion forum

