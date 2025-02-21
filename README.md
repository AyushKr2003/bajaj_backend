# Number and Alphabet Filter API

A Flask-based REST API that processes arrays of numbers and alphabets, providing filtered results and user information.

## Features

- Filters numbers and alphabets from input array
- Finds the highest alphabet in the input
- Returns user information along with filtered data
- Includes both POST and GET endpoints

## API Endpoints

### POST /bfhl

Processes an array of inputs and returns filtered results.

#### Request Format
```json
{
    "data": ["A", "1", "B", "2", "C", "3"]
}