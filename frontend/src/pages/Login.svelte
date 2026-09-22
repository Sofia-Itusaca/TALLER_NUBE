<script>
    export let onLogin;

    let email = '';
    let password = '';
    let error = '';

    function login() {
        error = '';

        if (!email || !password) {
            error = 'Completa todos los campos.';
            return;
        }

        if (email === 'admin@tallernube.com' && password === '123456') {
            onLogin();
        } else {
            error = 'Correo o contraseña incorrectos.';
        }
    }
</script>

<div class="login-page">

    <div class="login-card">

        <div class="logo">
            ☁️
        </div>

        <h1>TALLER_NUBE</h1>

        <p class="subtitle">
            Acceso al sistema
        </p>

        <form on:submit|preventDefault={login}>

            <label>
                Correo electrónico
            </label>

            <input
                type="email"
                bind:value={email}
                placeholder="admin@tallernube.com"
            />

            <label>
                Contraseña
            </label>

            <input
                type="password"
                bind:value={password}
                placeholder="••••••••"
            />

            {#if error}
                <div class="error">
                    {error}
                </div>
            {/if}

            <button type="submit">
                Iniciar sesión
            </button>

        </form>

        <small>
            Sistema de gestión cloud
        </small>

    </div>

</div>

<style>
    .login-page {
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        background: #0f172a;
    }

    .login-card {
        width: 420px;
        padding: 40px;
        border-radius: 20px;
        background: #1e293b;
        border: 1px solid #334155;
        box-shadow: 0 20px 50px rgba(0, 0, 0, .35);
    }

    .logo {
        text-align: center;
        font-size: 45px;
    }

    h1 {
        text-align: center;
        color: white;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 30px;
    }

    label {
        display: block;
        margin-top: 18px;
        margin-bottom: 8px;
        color: #e2e8f0;
    }

    input {
        width: 100%;
        padding: 13px;
        box-sizing: border-box;
        border-radius: 8px;
        border: 1px solid #475569;
        background: #0f172a;
        color: white;
        font-size: 14px;
    }

    input:focus {
        outline: none;
        border-color: #38bdf8;
    }

    button {
        width: 100%;
        margin-top: 25px;
        padding: 13px;
        border: none;
        border-radius: 8px;
        background: #0284c7;
        color: white;
        font-weight: bold;
        cursor: pointer;
        font-size: 14px;
    }

    button:hover {
        background: #0369a1;
    }

    .error {
        margin-top: 15px;
        padding: 10px;
        border-radius: 8px;
        background: #7f1d1d;
        color: #fecaca;
        text-align: center;
    }

    small {
        display: block;
        text-align: center;
        margin-top: 25px;
        color: #64748b;
    }
</style>