class MockRestaurantAPI:
    @classmethod
    def check_table_availability(cls, **kwargs):
        """
        This function mocks the call of an API where restaurant information would be available.
        """
        required_args = ['party_size', 'date', 'time', 'restaurant_name']
        missing_args = [arg for arg in required_args if arg not in kwargs]

        if missing_args:
            return f"Missing required arguments: {', '.join(missing_args)}"

        party_size = kwargs.get('party_size')
        date = kwargs.get('date')
        time = kwargs.get('time')
        restaurant_name = kwargs.get('restaurant_name')

        # Placeholder for the actual availability check logic
        # This could involve querying a database, an API, etc.
        is_available = True  # Assuming availability for now

        if is_available:
            return (True, (f"Yes, a reservation for {party_size} people on {date} at {time} "
                    f"at {restaurant_name} is possible"))
        else:
            return (False, (f"Sorry, a reservation for {party_size} people on {date} at {time} "
                    f"at {restaurant_name} is not available"))

    @classmethod
    def perform_dummy_reservation(cls, **kwargs):
        """
        This function mocks the call of an API to reserve the restaurant
        """
        required_args = ['party_size', 'date', 'time', 'restaurant_name']
        missing_args = [arg for arg in required_args if arg not in kwargs]

        if missing_args:
            return f"Missing required arguments: {', '.join(missing_args)}"

        availability = cls.check_table_availability(**kwargs)

        if not availability[0]:
            return (False, f"Reservation could not be made. {availability[1]}")

        # Placeholder for the actual reservation logic
        # This could involve updating a database, an API call, etc.
        reservation_id = "RES123456"  # Dummy reservation ID

        return (True, (f"Reservation confirmed! Your reservation ID is {reservation_id}. "
                       f"A table for {kwargs['party_size']} people on {kwargs['date']} at {kwargs['time']} "
                       f"at {kwargs['restaurant_name']} has been booked."))
