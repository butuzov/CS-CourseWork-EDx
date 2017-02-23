## whodunit.c

![GitHub Logo](/pset4/whodunit/out.gif)

### Answering questions.

1. What’s stdint.h?

	`stdint.h` is a `C` header file (used in `bmp.h` in our project) that describe and declare additional int structures.

2. What’s the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

	While we programming on C we should respect memory, and not use it more then we need it.


3. How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

Type | Definition
------------ | -------------
BYTE| unsigned integer of 8 bits
DWORD| unsigned interger of 32 bits
LONG|interger of 32 bits
WORD|unsigned interger of 16 bits

4. What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

Byte | ASCII | Dec | Hex
---- | ----- | ----| ---
1st | B | 66 | 0x42
2nd | M | 77 | 0x4d


5. What’s the difference between bfSize and biSize?

	`bfSize` is file size in bytes + file header + info header, `biSize` is "The number of bytes (size) required by the structure." of `BITMAPINFOHEADER`.

6. What does it mean if biHeight is negative?

   "If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner."
	by https://msdn.microsoft.com/ru-ru/library/windows/desktop/dd183376(v=vs.85).aspx

7. What field in `BITMAPINFOHEADER` specifies the BMP’s color depth (i.e., bits per pixel)?

   `biBitCount`

8) Why might fopen return NULL in lines 24 and 32 of `copy.c`?

	File system can not allow our program to real file location, or forbit to write it. There are number of reasons for than: starting from file can be busy to permissions.

9) Why is the third argument to fread always 1 in our code?

	Because we reading only 1 RGB tripple (and RGB tripple size is second argument), so we always reading 3 bytes per iteration (which means we reading one by one pixel).

10) What value does line `65` of `copy.c` assign to padding if bi.biWidth is 3?

    `0` - biWidth is 3 pixels so it will take 12 bytes which divided by 3 without change.

11) What does fseek do?

    Set file position (from where we can read ) in some position determined by the offset and `whence` position.

12) What is SEEK_CUR?

     SEEK_CUR - this is constant that tells fseek that we fseek should search for offset starting from current streeam position. We can rewind this position to begining or end of file using `SEEK_SET` and `SEEK_END`.
