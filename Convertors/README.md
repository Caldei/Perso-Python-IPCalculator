<h1 align="center">🧮</br>IPCalculator</h1>
<p align="center">
  Convertors Documentation
</p>


---
## C2M - CIDR to Mask Convertor
### Input
* CIDR

### Outputs 
* Decimal Mask
* Wildcard Mask
* Binary Mask
* Number of potential IPs for this Mask
* Number of potential Usable IPs for this Mask
* Number of potential Subnets 

### Example 
```
Welcome: This is CIDR to Mask convertor!
Enter a CIDR (just the number): 24

Decimal Mask: 255.255.255.0
Wildcard Mask: 0.0.0.255
Binary Mask:  11111111.11111111.11111111.00000000

Number of IPs: 256
Number of usable IPs: 254

Number of SubNets: 64
```


--- 
## M2C - Mask to CIDR Convertor
### Input 
* Decimal Mask

### Outputs
* CIDR
* Wildcard Mask
* Binary Mask
* Number of potential IPs for this Mask
* Number of potential Usable IPs for this Mask
* Number of potential Subnets 

### Example 
```
Welcome: This is Mask to CIDR convertor!
Enter a Mask: 255.255.255.0

CIDR: /24
Wildcard Mask: 0.0.0.255
Binary Mask: 11111111.11111111.11111111.00000000

Number of IPs: 256
Number of usable IPs: 254

Number of SubNets: 64
```

---
## W2C - WildCard Mask to Mask Convertor
### Input 
* Wildcard Mask

### Outputs 
* CIDR
* Decimal Mask
* Binary Mask
* Number of potential IPs for this Mask
* Number of potential Usable IPs for this Mask
* Number of potential Subnets 

### Example 
```
Welcome: This is Wildcard Mask to Mask convertor!
Enter a Wildcard Mask: 0.0.0.255

CIDR: /24
Mask: 255.255.255.0
Binary Mask: 11111111.11111111.11111111.00000000

Number of IPs: 256
Number of usable IPs: 254

Number of SubNets: 64
```
