# multitp_cracker - Multi Time Pad Cracker

It's just the beginning so there's still not much to see.

### Key features (in the future): ###
- [x] attacking ciphertexts by using xor properties
- [ ] attacking them by using a dictionary
- [ ] automatic and interactive mode
- [ ] library is going to be easy to extend (adding new ways of reading stored ciphertexts, new modes of attack, etc)

### What's here now: ###

Well, you can use xor properties to crack some simple ciphertexts. But you need to satisfy these conditions:
* ciphers ought to be in format of string of octects where single octet represents one byte of the ciphertext.
  See file **tests/crypto01**
* the ciphertexts must be in **ASCII** (not ASCII-ext). Nothing else.

After using it you'll see partially decrypted messages (it's not and it will never be 100% accurate) - 
that's why there will be the interactive mode.

### TODOs: ###
* dict attack, more encodings, more ways to store ciphertexts
* true interactive mode
* automatic mode
* semi-automatic (automatic, but asking user to resolve ambiguity)

### Another TODOs: ###
* create unittests and setup CI
* prepare some HOWTOs
* dict attack is going to be very consuming, so maybe some GPU acceleration
