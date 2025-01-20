const { invoke } = window.__TAURI__.core;

function sha256(plain) {
    const hash = CryptoJS.SHA256(plain);
    return hash.toString(CryptoJS.enc.Hex);
}

async function login(username, password){ 
    const data = {
        username: username,
        password: password
    }

    const aesKey = await invoke("get_aes_key");
    const encryptedData = CryptoJS.AES.encrypt(JSON.stringify(data), aesKey).toString();

    try {
        const jsonData = JSON.stringify(data);

        const response = await fetch('https://secure-login-20.aimar.id/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Signature': sha256(jsonData),
            },
            body: JSON.stringify({
                data: encryptedData
            }),
        });

        const result = await response.json();
        if (result.flag !== undefined) {
            document.getElementById('result').innerHTML = result.flag;
        } else if (result.error !== undefined) {
            document.getElementById('result').innerHTML = '<p style="color: red;">' + result.error + '</p>';
        } else {
            document.getElementById('result').innerHTML = 'Hi, ' + result.username + '!';
        }
    } catch (error) {
        document.getElementById('result').innerHTML = '<p style="color: red;">' + error + '</p>';
    }
}

window.addEventListener("DOMContentLoaded", () => {
    username = document.getElementById('username');
    password = document.getElementById('password');
    document.querySelector("#login-form").addEventListener("submit", (e) => {
        e.preventDefault();
        login(username.value, password.value);
    });
});