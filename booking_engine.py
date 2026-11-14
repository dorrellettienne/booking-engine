

def is_valid_slot(start, end):
    return start >= 9 and end <= 17 and start < end

def overlaps(existing_start, existing_end,
             requested_start, requested_end):

    return (
        existing_start < requested_end
        and requested_start < existing_end
    )

def add_booking(bookings, start, end):

    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            return False

    if not is_valid_slot(start, end):
        return False

    for existing_start, existing_end in bookings:
        if overlaps(existing_start, existing_end,
                    start, end):
            return False

    bookings.append((start, end))
    return True

import unittest


class TestBookingEngine(unittest.TestCase):

    def test_duplicate_booking(self):
        bookings = [(9, 10)]

        result = add_booking(bookings, 9, 10)

        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    def test_outside_hours(self):
        bookings = [(9, 10)]

        result = add_booking(bookings, 18, 19)

        self.assertFalse(result)
        self.assertEqual(bookings, [(9, 10)])

    def test_adjacent_booking(self):
        bookings = [(9, 10)]

        result = add_booking(bookings, 10, 11)

        self.assertTrue(result)
        self.assertEqual(bookings, [(9, 10), (10, 11)])

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


if __name__ == "__main__":
    unittest.main()