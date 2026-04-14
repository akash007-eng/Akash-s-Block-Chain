// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FileStorage {

    struct File {
        string fileHash;
        address uploader;
        uint timestamp;
    }

    File[] public files;

    function storeHash(string memory _hash) public {
        files.push(File(_hash, msg.sender, block.timestamp));
    }

    function getFile(uint index) public view returns (string memory, address, uint) {
        File memory f = files[index];
        return (f.fileHash, f.uploader, f.timestamp);
    }

    function getFileCount() public view returns (uint) {
        return files.length;
    }
}