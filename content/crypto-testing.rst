########################################
Assured Remote Testing With Cryptography
########################################
:date: 2016-10-12

[[illustration goes here]]

I was part of a team that needed to test a vendor product.
This product would predict a future state based on measurements up until the present.
The problem was we only had historical data to test it against.

The vendor was unable to have us observe the system, so we could not be certain that the future results were not used in their testing.
I came up with a solution using a cryptographic hash and automated REST service that would feed them data one day at time.

They would start with one day of data unlocked, then submit their cryptographic hash of their results.
Once that hash was received, the next day of input data would be unlocked.
This allowed testing to be done rapidly and securely.
The test results were in the many hundreds of gigabytes, so the cryptographic hash also minimized the amount of data transfer needed.

Input data was similarly large in size.
We gave the vendor all of the data in encrypted form.
The web service would unlock each piece of data by sending them the appropriate decryption key.
