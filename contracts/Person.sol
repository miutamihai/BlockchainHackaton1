pragma solidity ^0.8.0;

contract Person {
    uint256 age;
    
    constructor(uint256 _age){
        age = _age;
    }
    
    function getAge() public view returns (uint256) {
        return age;
    }
    
    function setAge(uint256 newAge) public {
        age = newAge;
    }
}
