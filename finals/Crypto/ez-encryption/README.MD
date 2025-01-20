# Ez Encryption

## Challenge Overview

The challenge involves a custom encryption scheme that uses a **Dual Xorshift-based Stream Cipher** to encrypt a secret flag. The encryption process combines two independent Xorshift PRNG states to generate a keystream, which is then used to encrypt the plaintext. The plaintext consists of a **hex-encoded key** concatenated with the **XOR of the key and the flag**.

### Encryption Steps

1. **Key and Flag Preparation**:
   - **Key Generation**: A random key (`key`) is generated with the same byte length as the secret `FLAG`.
   - **Plaintext Formation**: The plaintext is created by concatenating:
     - **Hex-Encoded Key (`key_hex`)**: Converts the `key` to a hexadecimal string, resulting in bytes containing only `[0-9a-f]`.
     - **XOR of Key and Flag (`key_xor_flag`)**: Performs a byte-wise XOR between the `key` and the `FLAG`.

2. **Dual Xorshift PRNG**:
   - **Initialization**: Two random 64-bit seeds (`s0` and `s1`) initialize the PRNG.
   - **Keystream Generation**: For each 8-byte block of plaintext, both seeds are updated using the `initialMagic` function, and their XOR produces a 64-bit keystream block.

3. **Encryption**:
   - The plaintext is divided into 8-byte blocks.
   - Each block is XORed with the corresponding keystream block to produce the ciphertext.
   - The final ciphertext is output as a hexadecimal string.

## Solver Overview

The provided solver leverages the known structure of the plaintext to recover the internal PRNG states (`s0` and `s1`) and ultimately decrypt the ciphertext to reveal the `FLAG`. It utilizes the **Z3 SMT solver** to model and solve the constraints imposed by the encryption scheme.

### How the Solver Works

1. **Ciphertext Parsing**:
   - Converts the hexadecimal ciphertext back to raw bytes.
   - Identifies the segments corresponding to the hex-encoded key (`key_hex`) and the `key XOR flag` (`key_xor_flag`).

2. **Modeling PRNG States**:
   - Defines two 64-bit symbolic variables (`s0` and `s1`) representing the unknown initial seeds.
   - Simulates the PRNG's state updates for each ciphertext block using the `apply_initial_state_z3` function, which mirrors the `initialMagic` function from the encryption.

3. **Applying Constraints**:
   - For each byte in the decrypted `key_hex` portion, enforces that the byte must be a valid hexadecimal ASCII character (`0-9` or `a-f`).
   - These constraints significantly narrow down the possible values of `s0` and `s1`.

4. **Solving for Internal States**:
   - Utilizes Z3 to find values for `s0` and `s1` that satisfy all imposed constraints.
   - If successful, retrieves the concrete values of the initial seeds.

5. **Decrypting the Ciphertext**:
   - With the recovered seeds, the solver replicates the keystream generation process.
   - XORs the ciphertext with the regenerated keystream to obtain the full plaintext (`key_hex || key XOR flag`).
   - Extracts and decodes the `key_hex` to retrieve the original `key`.
   - XORs the `key` with `key XOR flag` to recover the original `FLAG`.

6. **Output**:
   - Prints the recovered `key` in hexadecimal format.
   - Displays the decrypted `FLAG`.

### Key Points

- **Predictable Plaintext**: The hex-encoded key portion of the plaintext (`key_hex`) is constrained to `[0-9a-f]`, providing strong clues to deduce the keystream.
  
- **Linear PRNG Vulnerability**: The use of Xorshift-based PRNGs, even in dual configurations, is susceptible to state recovery attacks when plaintext structure is predictable.
  
- **Z3 Solver**: The solver models the PRNG behavior and applies constraints to recover the internal states.
