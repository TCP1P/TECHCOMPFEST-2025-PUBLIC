# pdf-flag-checker (medium)

## description

I just create handmade pdf. Well i also made flag checker inside pdf file. Cool right? 😎 

## how to solve

1. first we need to know the password to open the pdf file
2. we can use `pdf-parser` to extract the pdf file and see the stream inside it
3. or we can use hex editor to see the stream and decode it using zlib.decompress in python
4. Then we use jsf*ck deobfuscator to see javascript
5. We can reverse it and get the flag

## flag

TCF2024{mallic1ous_pdf_is_cr4zyy_e1695f085f069fb1ebb2d9df1d013ecb}