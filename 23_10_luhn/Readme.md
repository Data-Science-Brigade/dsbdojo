# Luhn Algorithm

Luhn formula, also known as the "modulus 10" or "mod 10" algorithm, named after its creator, IBM scientist Hans Peter Luhn

https://en.wikipedia.org/wiki/Luhn_algorithm


- From the rightmost digit and moving left, double the value of every second digit. 
    - If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then add the digits of the result (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, alternatively, the same final result can be found by subtracting 9 from that result (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).

- Take the sum of all the digits.

- If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; otherwise it is not valid.

Examples:

Valid credit card number 
------------------------
```
4539 1488 0343 6467
```
and
```
4539-1488-0343-6467
```

The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling

```
4_3_ 1_8_ 0_4_ 6_6_
```

If doubling the number results in a number greater than 9 then subtract 9
from the product. The results of our doubling:

```
8569 2478 0383 3437
```

Then sum all of the digits:

```
8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
```

If the sum is evenly divisible by 10, then the number is valid. This number is valid!


Invalid credit card number
--------------------------

```
8273 1232 7352 0569
```

Double the second digits, starting from the right

```
7253 2262 5312 0539
```

Sum the digits

```
7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
```

57 is not evenly divisible by 10, so this number is not valid.


### 23/10/2019 - Participantes
* Hellen
* Tailor
* Bruno
* Karina
* Antonio
