"""
Script with class filter_data
(10/10)
"""


class FilterData:
    """
    Class to filter data by year and month of publication.
    """

    def __init__(self, df):
        """
        Aceptar un DataFrame (df)
        """
        self.df = df

    # In both datasets you can filter by year

    def filter_by_year(self, year):
        """
        Filter books or films by a given minimum year.
        """
        year = int(year)
        relevant_column = (
            "Publish Date (Year)"
            if "Publish Date (Year)" in self.df.columns
            else "Year"
        )
        return self.df[self.df[relevant_column] > year]

    def filter_by_month(self, month):
        """
        Filter books by a given month.
        """
        return self.df[self.df["Publish Date (Month)"] == month]

    def filter_by_price(self, price):
        """
        Filter books by a given minimum price.
        """
        price = float(price)
        return self.df[self.df["Price Starting With ($)"] > price]

    def filter_by_genre(self, genre):
        """
        Filter the DataFrame based on a specified genre.
        """
        return self.df[self.df["Genre"] == genre]

    def filter_by_tickets(self, tickets_sold):
        """
        Filter a minimum number of tickets sold.
        """
        return self.df[self.df["Tickets Sold"] > float(tickets_sold)]


if __name__ == "__main__":
    pass
