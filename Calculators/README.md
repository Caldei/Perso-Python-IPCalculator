<h1 align="center">🧮</br>IPCalculator</h1>
<p align="center">
  Calculators Documentation
</p>


---  
## RangeCalc - Network Range Calculator
### Inputs
* IP
* Decimal Mask or CIDR

### Outputs 
* Network Address of the Subnet
* Broadcast Address of the Subnet
* Number of IPs in the Subnet
* Number of Usable IPs in the Subnet

### Example 
```
Welcome: This is IP Range Calculator!
Enter an IP: 10.0.0.0

Enter a Mask or a CIDR (without the '/'): 24

Network Address: 10.0.0.0
Broadcast Address: 10.0.0.255

Number of IPs: 256
Number of usable IPs: 254
```


---
## SubNetCalc - SubNets Calculator
### Inputs
* IP
* Decimal Mask or CIDR
* Number of Subnets needed
* Number of users needed per Subnet

### Outputs 
* Network Address (for each Subnets)
* Broadcast Address (for each Subnets)
* Mask (for each Subnets)
* CIDR (for each Subnets)
* Number of IPs (for each Subnets)
* Number of Usable IPs (for each Subnets)

### Example 
```
Welcome: This is SubNet Calculator!
Enter your IP: 10.0.0.0

Enter your Mask or CIDR (without the '/'): 24

Enter the number of SubNets you need (max 64): 2

Enter the number of users in descending order for your 2 SubNets.
Enter the number of users you need for SubNet 1 (254 IPs availabes): 100

--- --- --- SubNet 1 --- --- ---
Network Address: 10.0.0.0
Broadcast Address: 10.0.0.127
Mask: 255.255.255.128
CIDR: /25

Number of IPs: 128
Number of usable IPs: 126


Enter the number of users you need for SubNet 2 (128 IPs availabes): 25

--- --- --- SubNet 2 --- --- ---
Network Address: 10.0.0.128
Broadcast Address: 10.0.0.159
Mask: 255.255.255.224
CIDR: /27

Number of IPs: 32
Number of usable IPs: 30
```