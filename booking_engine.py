
# ------------------------------------
# 1. Check whether a booking is valid
# ------------------------------------

def is_valid_slot(start, end):
    return start >= 9 and end <= 17 and start < end


# ------------------------------------
# 2. Check whether bookings overlap
# ------------------------------------

def overlaps(existing_start, existing_end,
             requested_start, requested_end):

    return (
        existing_start < requested_end
        and requested_start < existing_end
    )


# ------------------------------------
# 3. Add a new booking
# ------------------------------------

def add_booking(bookings, start, end):

    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            return False

    # First: check whether the requested time is valid
    if not is_valid_slot(start, end):
        return False

    # Second: check each existing booking for conflicts
    for existing_start, existing_end in bookings:
        if overlaps(existing_start, existing_end,
                    start, end):
            return False

    # Third: add the booking if there are no conflicts
    bookings.append((start, end))
    return True

# ------------------------------------
# 4. Automated unit tests
# ------------------------------------

import unittest


class TestBookingEngine(unittest.TestCase):

    # Test 1: Duplicate bookings must be rejected
    def test_duplicate_booking(self):
        bookings = [(9, 10)]

        result = add_booking(bookings, 9, 10)

        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    # Test 2: Bookings outside hours must be rejected
    def test_outside_hours(self):
        bookings = [(9, 10)]

        result = add_booking(bookings, 18, 19)

        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    # Test 3: Adjacent bookings should be accepted
    def test_adjacent_booking(self):
        bookings = [(9, 10)]

        result = add_booking(bookings, 10, 11)

        self.assertTrue(result)
        self.assertEqual(bookings, [(9, 10), (10, 11)])

    # Test 4: Partial overlaps must be rejected
    def test_partial_overlap(self):
        bookings = [(9, 10)]

        result = add_booking(bookings, 9.5, 10.5)

        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    def test_malformed_start_input(self):
        bookings = [(9, 10)]
        
        result = add_booking(bookings, "ten", 11)
        
        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    def test_malformed_end_input(self):
        bookings = [(9, 10)]
                
        result = add_booking(bookings, 10, "eleven")
                
        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    def test_zero_length_booking(self):
        bookings = [(9, 10)]
                        
        result = add_booking(bookings, 11, 11)
                        
        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    def test_closing_time_boundary(self):
        bookings = [(9, 10)]
                                
        result = add_booking(bookings, 16, 17)
                                
        self.assertTrue(result)
        self.assertEqual(bookings, [(9, 10), (16, 17)])


# ------------------------------------
# 5. Run automated tests
# ------------------------------------

if __name__ == "__main__":
    unittest.main()