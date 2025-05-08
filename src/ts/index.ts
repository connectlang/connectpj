interface ConstructorInterface {
    host?: string;
    port?: number;
    baseUrl?: string;
}

class PythonClient {
    baseUrl: string;

    constructor({ host = 'http://localhost', port = 5000, baseUrl }: ConstructorInterface = {}) {
        this.baseUrl = baseUrl || `${host}:${port}`;
    }

    async connect() {
        try {
            const res = await fetch(`${this.baseUrl}/ping`);
            if (!res.ok) throw new Error('Ping failed');
            console.log('✅ 연결 성공');
        } catch (err) {
            console.error('❌ 연결 실패:', err);
            throw err;
        }
    }

    async callFunction(funcName: string, args: any = {}) {
        const res = await fetch(`${this.baseUrl}/call/${funcName}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(args)
        });
        const data = await res.json();
        if ('result' in data) return data.result;
        throw new Error(data.error || 'Unknown error');
    }
}

export {
    PythonClient,
};
