import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Load Data ----------------

def load_data(path):
    return pd.read_csv(path, encoding='latin1')


# ---------------- Data Understanding ----------------

def data_understanding(df):

    print("\nTotal Rows & Columns:")
    print(df.shape)

    print("\nAll Columns:\n")
    print(df.columns)

    print("\nData Types:\n")
    print(df.dtypes)

    print("\nMissing Values:\n")
    print(df.isnull().sum())


# ---------------- Data Cleaning ----------------

def clean_data(df):

    print("\nDuplicate Values:")
    print(df.duplicated().sum())

    df = df.drop_duplicates()

    print("\nDuplicates Removed Successfully!")

    return df


# ---------------- Feature Engineering ----------------

def feature_engg(df):

    # Convert into datetime
    df['Order.Date'] = pd.to_datetime(df['Order.Date'])

    # Year
    df['Year'] = df['Order.Date'].dt.year

    # Month Number
    df['Month_Num'] = df['Order.Date'].dt.month

    # Month Name
    df['Month_Name'] = df['Order.Date'].dt.month_name()

    # Day Name
    df['Day_Name'] = df['Order.Date'].dt.day_name()

    # Quarter
    df['Quarter'] = df['Order.Date'].dt.quarter

    # Profit Margin
    df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100

    # Average Sales Per Quantity
    df['Avg_Sales_Per_Qty'] = df['Sales'] / df['Quantity']

    return df


# ---------------- Monthly Sales Trend ----------------

def monthly_trend(df):
    feature_engg(df)
    
    print("\nQuestion:")
    print("Which month generated the highest sales?\n")

    total_sales = df['Sales'].sum()

    print(f"Overall Company Sales: {total_sales:,.2f}")

    monthly_sales_trend = df.groupby(
        ['Month_Num', 'Month_Name']
    )['Sales'].sum().reset_index()

    monthly_sales_trend = monthly_sales_trend.sort_values('Month_Num')

    plt.figure(figsize=(10,5))

    sns.lineplot(
        data=monthly_sales_trend,
        x='Month_Name',
        y='Sales',
        marker='o'
    )

    plt.title("Monthly Sales Analysis")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig('monthly_trend.png')
    plt.show()

    print("\nInsight:")
    print("Monthly sales trend helps identify seasonal demand patterns.")


# ---------------- Yearly Sales Trend ----------------

def yearly_trend(df):
    feature_engg(df)
    
    print("\nQuestion:")
    print("Which year generated the highest sales?\n")

    yearly_sales_trend = df.groupby('Year')['Sales'].sum().reset_index()

    plt.figure(figsize=(8,5))

    sns.lineplot(
        data=yearly_sales_trend,
        x='Year',
        y='Sales',
        marker='o'
    )

    plt.title("Yearly Sales Analysis")
    plt.xlabel("Year")
    plt.ylabel("Sales")

    plt.tight_layout()
    plt.savefig('yearly_trend.png')
    plt.show()

    print("\nInsight:")
    print("Sales are continuously increasing year by year, indicating business growth.")


# ---------------- Category Wise Sales ----------------

def category_wise_sales(df):
    feature_engg(df)
    
    print("\nQuestion:")
    print("Which category contributes the highest sales?\n")

    sales_by_cat = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

    plt.figure(figsize=(8,5))

    sns.barplot(
        x=sales_by_cat.index,
        y=sales_by_cat.values
    )

    plt.title("Category Wise Sales Analysis")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    
    plt.tight_layout()
    plt.savefig('category_wise_sales.png')
    plt.show()

    print("\nInsight:")
    print("Technology category contributes the highest sales and acts as a major revenue-driving segment.")


# ---------------- Sub-Category Wise Sales ----------------

def sub_cat_wise_sales(df):
    feature_engg(df)
    
    print("\nQuestion:")
    print("Which sub-category contributes the highest sales?\n")

    sales_by_sub_cat = df.groupby('Sub.Category')['Sales'].sum().sort_values(ascending=False)

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=sales_by_sub_cat.index,
        y=sales_by_sub_cat.values
    )

    plt.title("Sub-Category Wise Sales Analysis")
    plt.xlabel("Sub-Category")
    plt.ylabel("Sales")

    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.savefig('sub_category_wise_sales.png')
    plt.show()

    print("\nInsight:")
    print("Phones sub-category generates the highest sales contribution among all sub-categories.")


# ---------------- Regional Sales Analysis ----------------

def regional_sales(df):
    feature_engg(df)
    
    print("\nQuestion:")
    print("Which region contributes the highest sales?\n")

    regional_sales_analysis = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

    plt.figure(figsize=(8,5))

    sns.barplot(
        x=regional_sales_analysis.index,
        y=regional_sales_analysis.values
    )

    plt.title("Region Wise Sales Analysis")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('Regional_Sales.png')
    plt.show()

    print("\nInsight:")
    print("The Central region contributes the highest share of total sales.")


# ---------------- Complete Sales Analysis ----------------

def sales_or_trend_analysis(df):

    monthly_trend(df)

    yearly_trend(df)

    category_wise_sales(df)

    sub_cat_wise_sales(df)

    regional_sales(df)


# ---------------- Main Program ----------------

df = load_data("superstore.csv")

while True:

    print("\n========== Ecommerce Sales Analysis ==========")

    print("1. Data Understanding")
    print("2. Clean Data")
    print("3. Sales & Trend Analysis")
    print("4. Exit")

    try:

        choice = int(input("\nEnter Your Choice: "))

        if choice == 1:

            data_understanding(df)

        elif choice == 2:

            df = clean_data(df)

        elif choice == 3:

            df = feature_engg(df)

        elif choice == 4:

            sales_or_trend_analysis(df)

        elif choice == 5:

            print("\nProgram Exited Successfully!")
            break

        else:

            print("\nInvalid Input! Please enter a valid choice.")

    except ValueError:

        print("\nError: Please enter a valid number.")