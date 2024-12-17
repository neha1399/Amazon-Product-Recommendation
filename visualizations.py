import plotly.graph_objects as go
import plotly.express as px

def create_all_visualizations(avg_ratings, total_ratings, top_5_by_category):
    # First graph: Average ratings by category (Bar Chart)
    fig1 = px.bar(
        avg_ratings,
        x=avg_ratings.index,
        y='ratings',
        title="Average Ratings by Category",
        labels={"ratings": "Average Rating", "main_category": "Category"},
        color=avg_ratings.index,  # Different colors for each category
        color_discrete_sequence=px.colors.qualitative.Set3  # Use a color palette
    )
    fig1.update_layout(xaxis_title="Category", yaxis_title="Average Rating")
    fig1.show()

    # Second graph: Total number of ratings by category (Bar Chart with a different color)
    fig2 = px.bar(
        total_ratings,
        x=total_ratings.index,
        y='no_of_ratings',
        title="Total Number of Ratings by Category",
        labels={"no_of_ratings": "Total Ratings", "main_category": "Category"},
        color=total_ratings.index,  # Different colors for each category
        color_discrete_sequence=px.colors.qualitative.Pastel  # Changed color scheme
    )
    fig2.update_layout(xaxis_title="Category", yaxis_title="Total Ratings")
    fig2.show()

    # Third graph: Table for Top 5 Products by Category with Category as Header
    table_data = []
    categories = top_5_by_category['main_category'].unique()
    
    for category in categories:
        # Add category heading
        table_data.append([f"<b>{category}</b>", "", ""])  # Leave the other columns empty
        
        # Add products for the current category
        category_data = top_5_by_category[top_5_by_category['main_category'] == category]
        for _, row in category_data.iterrows():
            table_data.append([row['name'], f"{row['ratings']:.2f}", int(row['no_of_ratings'])])

    # Format table data for Plotly
    formatted_table_data = list(zip(*table_data))  # Transpose rows into columns for Plotly
    
    fig3 = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["<b>Product Name</b>", "<b>Ratings</b>", "<b>Number of Ratings</b>"],
                    fill_color="lightblue",
                    align="center",
                    font=dict(color="black", size=12),
                ),
                cells=dict(
                    values=formatted_table_data,
                    fill_color=["white", "lightgrey"] * len(table_data),
                    align="center",
                    font=dict(color="black", size=11),
                ),
            )
        ]
    )
    fig3.update_layout(title="Top 5 Products by Category")
    fig3.show()

    # Fourth graph: Pie Chart of Ratings Distribution (Total Ratings across Categories)
    fig4 = px.pie(
        total_ratings,
        names=total_ratings.index,
        values='no_of_ratings',
        title="Ratings Distribution by Category",
        color=total_ratings.index,  # Different colors for each category
        color_discrete_sequence=px.colors.qualitative.Pastel  # Use the same color palette
    )
    # Add numbers on top of the pie chart slices (percentages and category names)
    fig4.update_traces(textinfo='percent+label', pull=[0.1 if x == total_ratings.idxmax() else 0 for x in total_ratings.index])
    fig4.show()