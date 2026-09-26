# 🍔 Food Delivery Order & Delivery Performance Analysis

## 📊 Power BI Data Analytics Project

This project analyzes food delivery orders to understand **order volume, customer purchasing behavior, restaurant performance, delivery efficiency, cancellation patterns, and peak ordering periods**.

The dashboard was created using **Microsoft Power BI** to transform raw food delivery data into an interactive and visually appealing analytics dashboard.

---

## 🎯 Project Objective

The main objective of this project is to analyze food delivery data and identify important patterns related to:

- 📦 Order volume
- 💰 Revenue and order value
- 👥 Customer purchasing behavior
- 🚴 Delivery performance
- ❌ Order cancellations
- ⏰ Peak ordering periods
- 📍 City and delivery-area performance
- 🍽️ Restaurant types
- 🚦 Traffic and weather impact on delivery
- 💳 Payment methods

The dashboard provides an interactive way to explore these insights using filters and visualizations.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Microsoft Power BI** | Dashboard creation and data visualization |
| **Power Query** | Data cleaning and transformation |
| **DAX** | Measures and KPI calculations |
| **Microsoft Excel** | Dataset preparation |
| **GitHub** | Project documentation and version control |

---

## 📁 Dataset

The project uses a food delivery orders dataset containing information about:

### Order Information
- Order ID
- Order Date
- Order Hour
- Order Timestamp
- Order Status
- Order Total
- Subtotal
- Tax Amount
- Delivery Fee
- Service Fee
- Tip Amount

### Customer Information
- Customer ID
- Customer Age
- Customer Rating
- Customer Type

### Restaurant Information
- Restaurant ID
- Restaurant Type
- Restaurant Rating

### Location Information
- City
- Delivery Area

### Delivery Information
- Delivery Partner
- Distance (km)
- Estimated Delivery Time
- Actual Delivery Time
- Late Delivery

### Other Information
- Cancellation Reason
- Items Count
- Payment Method
- Discount Percentage
- Traffic Level
- Weather
- Day of Week
- Weekend Indicator

---

## 🧹 Data Preparation

The dataset was prepared using Power Query and Power BI before creating the dashboard.

The preparation process included:

- Checking column data types
- Handling missing values
- Cleaning categorical fields
- Checking duplicate records
- Validating numerical fields
- Formatting date and time columns
- Preparing fields for visualization
- Creating calculated measures using DAX

---

## 📐 Key DAX Measures

### Total Orders

```DAX
Total Orders =
DISTINCTCOUNT('cleaned_dataset (2)'[order_id])
