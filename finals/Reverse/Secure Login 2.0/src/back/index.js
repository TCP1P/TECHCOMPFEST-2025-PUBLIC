import express from 'express';
import bodyParser from 'body-parser';
import CryptoJS from 'crypto-js';
import cors from 'cors';

const app = express();
const PORT = 80;

app.use(cors());
app.use(bodyParser.json());

const aesKey = "th1s_1s_a3s_k3y!";

function decryptData(encryptedData) {
    const bytes = CryptoJS.AES.decrypt(encryptedData, aesKey);
    const decrypted = bytes.toString(CryptoJS.enc.Utf8);
    return JSON.parse(decrypted);
}

function validateSignature(data, signature) {
    const hash = CryptoJS.SHA256(data).toString(CryptoJS.enc.Hex);
    return hash === signature;
}

app.post('/api/login', (req, res) => {
    try {
        const { data } = req.body;
        const signature = req.headers['x-signature'];

        if (!data || !signature) {
            return res.status(400).json({ error: 'Missing data or signature.' });
        }

        const decryptedData = decryptData(data);
        const isValidSignature = validateSignature(JSON.stringify(decryptedData), signature);

        if (!isValidSignature) {
            return res.status(403).json({ error: 'Invalid signature.' });
        }

        const { username, password } = decryptedData;
        
        if (username === 'admin' && password === 'admin') {
            if (decryptedData.is_admin === true) {
                return res.status(200).json({ 
                    flag: 'TCF{we-need-more-end-to-end-encryption-challenges-in-ctfs-tbh}',
                });
            } else {
                return res.status(403).json({ error: 'Cannot login as `admin` if is_admin is false.' });
            }
        } else {
            return res.status(200).json({ 
                username: username,
            });
        }
    } catch (error) {
        console.error('Error during login:', error);
        return res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});
