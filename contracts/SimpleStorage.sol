// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedData;

    event PaymentSent(address indexed sender, address indexed receiver, uint256 amount);

    function set(uint256 x) public {
        storedData = x;
    }

    function get() public view returns (uint256) {
        return storedData;
    }

    function payMoney(address payable receiver) external payable {
    // Transfer ether to the receiver account
    receiver.transfer(msg.value);

    // Optionally emit an event or update contract state
    emit PaymentSent(msg.sender, receiver, msg.value);
}
}