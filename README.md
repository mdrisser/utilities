# Python Utilities
I find myself consistenly needing to write the same basic functions over and over again, converting between units, etc., so I created this python module to address that issue. This is an ongoing endevour, I'll be adding new files and functions as I deem necessary, so check back to see if there is anything new.

# Net Helpers
Various network helper functions that I find useful.
- **ipgeo_lookup()**
  - Gets the country associated with the given IP address.
  - Requires an API key for ipgeolocation.io.
  - Prints the information to the console.
- **~~auth0_lookup()~~**
  - **DEPRECATED!** Service is being shutdown by Auth0
  - Queries Auth0 to determine any blacklists that the IP in question may be on, prints the results to the console.
- **check_blocklist()**
  - Given an IP address, checks to see if it is on one of the blocklists

MORE TO ADD - STAY TUNED

# Terminal
Contains various functions and "constants" to make life easier when working in the terminal (things like printing the degree symbol)
