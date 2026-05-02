# Pagination

This directory contains Python tasks about pagination.

## Files

### 0-simple_helper_function.py

This file contains a helper function named `index_range`.

## Function

`index_range(page, page_size)`

The function takes two integer arguments:

- `page`: page number, starting from 1
- `page_size`: number of items per page

It returns a tuple containing the start index and the end index for pagination.

## Example

index_range(1, 7)
Returns: (0, 7)

index_range(page=3, page_size=15)
Returns: (30, 45)
