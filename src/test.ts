import { PythonClient } from './index';

const conn = new PythonClient({
    host: 'http://localhost',
    port: 5000,
});

async function ConnectWork() {
    await conn.connect();
    const result = await conn.callFunction('add', { a: "hello", b: " ", c: "world!" });
    console.log(result);
}

ConnectWork();
