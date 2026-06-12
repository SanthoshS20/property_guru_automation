import logging

logger = logging.getLogger(__name__)


class PropertySearchValidator:

    @classmethod
    def validate_search_results(cls, response_json, test_data):

        properties = response_json.get("properties", [])

        assert properties, (
            f"No properties returned for test case "
            f"{test_data.get('test_case_id', 'unknown')}"
        )

        search = test_data.get("search", {})
        quick_filters = test_data.get("quick_filters", {})
        more_filters = test_data.get("more_filters", {})

        expected_location = search.get("location")
        expected_property_type = quick_filters.get("property_type")
        expected_bedrooms = quick_filters.get("bedrooms")
        expected_price = quick_filters.get("price")
        expected_bathrooms = more_filters.get("bathrooms")
        verified_listing = more_filters.get("verified_listing")

        for index, property_data in enumerate(properties, start=1):

            logger.info(
                f"Validating property {index} - "
                f"{property_data.get('id', 'Unknown')}"
            )

            if expected_location:
                actual_location = property_data.get("location", "")

                assert expected_location.lower() in actual_location.lower(), (
                    f"Location mismatch. "
                    f"Expected: {expected_location}, "
                    f"Actual: {actual_location}"
                )

            if expected_property_type:
                actual_property_type = property_data.get("propertyType")

                assert actual_property_type == expected_property_type, (
                    f"Property type mismatch. "
                    f"Expected: {expected_property_type}, "
                    f"Actual: {actual_property_type}"
                )

            if expected_bedrooms is not None:
                actual_bedrooms = property_data.get("bedrooms")

                assert int(actual_bedrooms) == int(expected_bedrooms), (
                    f"Bedroom count mismatch. "
                    f"Expected: {expected_bedrooms}, "
                    f"Actual: {actual_bedrooms}"
                )

            if expected_price:
                min_price = expected_price["min"]
                max_price = expected_price["max"]
                actual_price = property_data.get("price")

                assert min_price <= actual_price <= max_price, (
                    f"Price mismatch. "
                    f"Expected between {min_price} and {max_price}, "
                    f"Actual: {actual_price}"
                )

            if expected_bathrooms is not None:
                actual_bathrooms = property_data.get("bathrooms")

                assert int(actual_bathrooms) == int(expected_bathrooms), (
                    f"Bathroom count mismatch. "
                    f"Expected: {expected_bathrooms}, "
                    f"Actual: {actual_bathrooms}"
                )

            if verified_listing == "Yes":
                assert property_data.get("verifiedListing") is True, (
                    f"Property is not a verified listing. "
                    f"Property ID: {property_data.get('id')}"
                )
