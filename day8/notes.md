# Day 8 – Exceptions and Generators

Today I learned how to handle errors in Python and how to work with generators to produce values efficiently.

## What I learned

### Exception Handling

* Using `try` and `except` to prevent program crashes
* Handling specific exceptions like:

  * `TypeError`
  * `ZeroDivisionError`
  * `FileNotFoundError`
* Using `else` and `finally` blocks
* Writing safer and more robust code

### Generators

* Creating generators using `yield`
* Understanding how generators produce values one at a time
* Using `next()` to iterate manually
* Building infinite sequences with generators

## Project

I built a turn management system that:

* Assigns a ticket number depending on the selected area (Pharmacy, Perfume, Cosmetic)
* Uses generators to create unique and sequential turn numbers
* Separates logic into different modules
* Allows continuous ticket generation without storing all values in memory

## Tools

* Pylint for improving code quality and detecting issues

## Practice

I applied exception handling to make programs more reliable and used generators to optimize performance and simplify repetitive tasks.

## Summary

This day helped me write more robust programs by handling errors properly and introduced me to generators, a powerful way to manage data efficiently.
