# Secure Login
Is it really secure?

Flag: TCF{`sha256(username+password)`}
For example:
- Username: admin
- Password: Admin#1234
- SHA256 (adminAdmin#1234): 09d4ebc297f76d7a59b5f077dc6edb99787187e9d18a60f62243eda87fdeede5
- Flag: TCF{09d4ebc297f76d7a59b5f077dc6edb99787187e9d18a60f62243eda87fdeede5}

URL: http://localhost:8081/

# Flag
TCF{338d4b418d030bf8fc7dcd10eea783237b24afde7fcaa12137b40b7880c1843f}