// SPDX-License-Identifier: MIT

pragma solidity >= 0.6.0;



contract FundMe
{
    mapping(address => uint256) public addressToAmountFunded;
    
    function fund() public payable {
        addressToAmountFunded[msg.sender] += msg.value;
    }    
}