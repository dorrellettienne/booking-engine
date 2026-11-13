## Booking Engine

A booking system that checks for overlaps, clashes and time boundaries

---

## Project Overview

A system for managing reservations for a single meeting room.

---

## Booking Rules

Meeting room is available from 9am to 5pm

every booking must have a start time earlier than its end time

Bookings cannot extend outside of opening hours

Two bookings for the same room cannot occupy the same time

A new booking can begin exactly when an existing booking ends

A new booking must be rejected if it shares any occupied time with an existing booking. This includes partial overlaps and complete containment in either direction. Bookings that only touch at their boundaries are allowed.

Our rule is if there's no overlap, the new end is less than or equal to the existing start or the new start is greater than or equal to the existing end 

booking intervals use [start, end), meaning the start is included and the end is excluded.

---

## Running Tests

Tests can be executed from the `booking-engine` directory using the following command:

```bash
python -m unittest booking_engine -v
```

This command runs eight automated tests to check whether bookings are correctly accepted or rejected, including conflicts, invalid inputs and boundary conditions.

The tests also verify that the booking list contains the expected values after each operation.

A successful run displays `Ran 8 tests` followed by `OK`, indicating that all eight tests passed.