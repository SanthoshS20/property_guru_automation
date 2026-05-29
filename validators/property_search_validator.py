class PropertySearchValidator:

    @staticmethod
    def validate(response_json, test_data):

        properties = response_json.get("properties", [])

        assert properties, "No properties returned"

        search = test_data.get("search", {})
        quick_filters = test_data.get("quick_filters", {})
        more_filters = test_data.get("more_filters", {})

        for property_data in properties:

            # Location Validation
            if search.get("location"):
                assert search["location"].lower() in \
                       property_data.get("location", "").lower(), \
                    f"Location mismatch: {property_data.get('location')}"

            # Property Type Validation
            if quick_filters.get("property_type"):
                assert property_data.get("propertyType") == \
                       quick_filters["property_type"], \
                    f"Property Type mismatch"

            # Bedrooms Validation
            if quick_filters.get("bedrooms"):
                assert int(property_data.get("bedrooms")) == \
                       int(quick_filters["bedrooms"]), \
                    f"Bedroom mismatch"

            # Price Validation
            if quick_filters.get("price"):

                min_price = quick_filters["price"]["min"]
                max_price = quick_filters["price"]["max"]

                property_price = property_data.get("price")

                assert min_price <= property_price <= max_price, \
                    f"Price {property_price} not within range"

            # Bathrooms Validation
            if more_filters.get("bathrooms"):

                assert int(property_data.get("bathrooms")) == \
                       int(more_filters["bathrooms"]), \
                    f"Bathroom mismatch"

            # Verified Listing Validation
            if more_filters.get("verified_listing") == "Yes":

                assert property_data.get("verifiedListing") is True, \
                    "Property is not verified"