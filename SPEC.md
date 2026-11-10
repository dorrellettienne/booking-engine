# Booking Engine v0.1

## Purpose
A system for managing reservations for a single meeting room.

## Booking Rules

Meeting room is available from 9am to 5pm
every booking must have a start time earlier than its end time

Bookings cannot extend outside of opening hours

Two bookings for the same room cannot occupy the same time

 new booking can begin exactly when an existing booking ends

A new booking must be rejected if it shares any occupied time with an existing booking. This includes partial overlaps and complete containment in either direction. Bookings that only touch at their boundaries are allowed.

Our rule is if there's no overlap, the new end is less than or equal to the existing start or the new start is greater than or equal to the existing end 