// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage
{
    // If not adding any value to the variable, it shall be initialized to 0. Without and visibility modifier, it's initialized with internal;
    uint256 favoriteNumber;
    struct Person
    {
        uint256 favoriteNumber;
        string name;
    }
    
    // To set the visibility modifier, we should use it's value after the type decaration
    Person[] public people;
    
    // Declaring a map to aux us to get the favorite number based on the name of the person (so we specify it's a map from string to uint256)
    mapping(string => uint256) public nameToFavoriteNumber;
    
    Person public patrick = Person({
        favoriteNumber: 2,
        name: "Lord Patrick"
    });
    
    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
        // uint256 notVisibleOutsideThisFunctionScope = 4;
    }
    
    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }
    
    function addPersonWithoutBrakets(string memory _name, uint256 _favoriteNumber) public {
        people.push(Person(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
    
    function addPersonWithBrakets(string memory _name, uint256 _favoriteNumber) public {
        people.push(Person({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    
} 