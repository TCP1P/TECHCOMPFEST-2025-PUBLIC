#include <emscripten.h>

// s3cr3t_us3rn4m3
char *ENCRYPTED_USERNAME = "\x00\x07\x05\x41\x6c\x04\x6b\x06\x00\x44\x42\x1c\x50\x1e\x07";
int USERNAME_LEN = 15;

char *XOR_KEY = "s4f3_p4ssw0rd";
int KEY_LEN = 13;

int _memcmp(const void *s1, const void *s2, int n) {
    const unsigned char *p1 = s1, *p2 = s2;
    while (n--) {
        if (*p1 != *p2) {
            return *p1 - *p2;
        }
        p1++;
        p2++;
    }
    return 0;
}

EMSCRIPTEN_KEEPALIVE
unsigned int login(const char *uname, const char *passwd) {
    char *username = (char *)uname;
    char *password = (char *)passwd;

    if (_memcmp((void *)password, (void *)XOR_KEY, KEY_LEN) != 0) {
        return 0;
    }

    for (int i = 0; i < USERNAME_LEN; i++) {
        username[i] ^= XOR_KEY[i % KEY_LEN];
    }

    if (_memcmp((void *)username, (void *)ENCRYPTED_USERNAME, USERNAME_LEN) == 0) {
        return 1;
    } else {
        return 0;
    }
}

EMSCRIPTEN_KEEPALIVE
char *allocateString(int len) {
    return (char *)malloc(len);
}

EMSCRIPTEN_KEEPALIVE
void freeString(char *str) {
    free(str);
}