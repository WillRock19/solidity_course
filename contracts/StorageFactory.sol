// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;

import "./SimpleStorage.sol";

contract StorageFactory
{
    SimpleStorage[] public simpleStorageArray;
    
    
    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }
    
    // Here we are going to interact with the SimpleStorage's store() function. Everytime we interact with a contract we need two things:
    
        // Contract address -> address where the contract was deployed in the network
        // Contract ABI     -> is the Application Binary Interface 
        
    function storageFactoryStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        getStorageByIndex(_simpleStorageIndex).store(_simpleStorageNumber);
    }
    
    function storageFactoryGet(uint256 _simpleStorageIndex) public view returns (uint256){
        return getStorageByIndex(_simpleStorageIndex).retrieve();
    }
    
    function getStorageByIndex(uint256 _simpleStorageIndex) private view returns(SimpleStorage) {
        address existingStorageAddress = address(simpleStorageArray[_simpleStorageIndex]); 
        return SimpleStorage(existingStorageAddress);
    }
}