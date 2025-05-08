// test.ts
import { PythonClient } from '../index';
import { z } from 'zod';

const conn = new PythonClient({
    host: 'http://localhost',
    port: 5500,
});

const AddSchema = z.object({
    name: z.string(),
    age: z.number(),
});

async function ConnectWork() {
    await conn.connect();

    const userInfo = {
        name: 'Alice',
        age: 22,
    };

    const addIt = AddSchema.parse(userInfo);
    const result = await conn.callFunction('process_user', addIt);

    console.log('✅ 처리된 사용자 데이터:');
    console.log(result);
}

ConnectWork();
