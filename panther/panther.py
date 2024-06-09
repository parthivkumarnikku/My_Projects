

def PlaintextProcessingMatrix(state, PT):
    ptlen = len(PT)
    if ptlen % 64 != 0:
        pad = 64 - (ptlen % 64) - 1
        PT += '1' + '0' * pad
    n = ptlen // 64
    matrix_PT = []
    for i in range(n):
        current_block = PT[i * 64: (i + 1) * 64]
        row = [int(bit) for bit in current_block]
        matrix_PT.append(row)
    return matrix_PT

def F(state, n):
    for _ in range(n):
        fp = state[0] ^ state[7] ^ state[10] ^ state[6] ^ (state[18] & state[6])
        fq = state[0] ^ state[4] ^ state[6] ^ state[7] ^ state[15] ^ (state[3] & state[7])
        fr = state[0] ^ state[1] ^ state[15] ^ state[17] ^ state[19] ^ (state[13] & state[15])
        fs = state[0] ^ state[1] ^ state[4] ^ (state[10] & state[4]) ^ (state[11] & state[18])
        gp = state[9] ^ state[10] ^ state[12]
        gq = state[4] ^ state[2] ^ state[5]
        gr = state[12] ^ state[11] ^ state[16]
        gs = state[16] ^ state[17] ^ state[2]
        rc1, rc2, rc3, rc4 = 0b0111, 0b1001, 0b1011, 0b1101
        l1 = fp ^ gp ^ rc1
        l2 = fq ^ gq ^ rc2
        l3 = fr ^ gr ^ rc3
        l4 = fs ^ gs ^ rc4
        d1, d2, d3, d4 = toeplitz_multiply(Tp, [l1, l2, l3, l4])
        t1, t2, t3, t4 = toeplitz_multiply(Tp, [Sb[d1], Sb[d2], Sb[d3], Sb[d4]])
        state = state[1:] + [t1, t2, t3, t4]
    return state

def toeplitz_multiply(matrix, vector):
    result = [sum(matrix[i][j] * vector[i] for i in range(len(matrix))) for j in range(len(vector))]
    return result

def Initialize(key, IV):
    state = [0] * 328 
    for i in range(128):
        state[i] = key[i]
    for i in range(128):
        state[i + 128] = IV[i]
    for i in range(64):
        state[i + 256] = key[i]
    for i in range(8):
        state[i + 320] = 1
    state[327] = 0
    state = F(state, 92) 
    return state

def AdProcessing(state, AD):
    adlen = len(AD)
    if adlen % 64 != 0:
        pad = 64 - (adlen % 64) - 1
        AD += '1' + '0' * pad
    k = adlen // 64
    for i in range(k):
        current_block = AD[i * 64: (i + 1) * 64]
        for j in range(64):
            state[j] ^= int(current_block[j])
        F(state, 4)
    return state

def PlaintextProcessing(state, PT):
    ptlen = len(PT)
    if ptlen % 64 != 0:
        pad = 64 - (ptlen % 64) - 1
        PT += '1' + '0' * pad
    n = ptlen // 64
    CT = []
    ct = 0
    for i in range(n):
        current_block = PT[i * 64: (i + 1) * 64]
        for j in range(64):
            state[j] ^= int(current_block[j])
            CT.append(state[j])
            ct += 1
        if i < n - 1:
            F(state, 4) 
    return CT, state

def Finalization(state, hashlen):
    F(state, 92)
    t = 0
    if hashlen % 64 == 0:
        for i in range(hashlen // 64):
            for j in range(64):
                tag[t] = state[j]
                t += 1
            F(state, 4)
    else:
        for i in range(hashlen // 64):
            for j in range(64):
                tag[t] = state[j]
                t += 1
            F(state, 4)
        for j in range(hashlen % 64):
            tag[t] = state[j]
            t += 1
    return tag

def Encryption(key, IV, AD, PT, hashlen):
    state = 0
    state = Initialize(key, IV)
    state = AdProcessing(state, AD)
    state, CT = PlaintextProcessing(state, PT)
    tag = Finalization(state, hashlen)
    return CT, tag

plaintext = "Hello, World!"  # Replace this with your actual plaintext
state = [0] * 328  # Assuming this is the correct initialization for the state
hashlen = 64  # Replace with your desired hash length
key = [1, 0, 1, 0] * 32  # Replace this with your actual key
IV = [0, 1, 0, 1] * 32  # Replace this with your actual IV
AD = "AdditionalData"  # Replace this with your actual associated data

CT, tag = Encryption(key, IV, AD, plaintext, hashlen)
print("Ciphertext:", CT)
print("Tag:", tag)