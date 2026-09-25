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

    <!-- Fondo decorativo -->
    <div class="sun"></div>
    <div class="cloud cloud-one">☁️</div>
    <div class="cloud cloud-two">☁️</div>

    <div class="content">

        <!-- Encabezado -->
        <div class="hero">

            <div class="weather-icon">
                🌤️
            </div>

            <h1>Consultor de Clima</h1>

            <h2>
                El clima de tu destino, al instante
            </h2>

            <p>
                Inicia sesión para consultar temperatura,
                estado y humedad de cualquier ciudad.
            </p>

        </div>

        <!-- Formulario -->
        <div class="login-card">

            <form on:submit|preventDefault={login}>

                <div class="field">

                    <label for="email">
                        Usuario
                    </label>

                    <input
                        id="email"
                        type="email"
                        bind:value={email}
                        placeholder="admin@tallernube.com"
                        autocomplete="username"
                    />

                </div>

                <div class="field">

                    <label for="password">
                        Contraseña
                    </label>

                    <input
                        id="password"
                        type="password"
                        bind:value={password}
                        placeholder="••••••••"
                        autocomplete="current-password"
                    />

                </div>

                {#if error}
                    <div class="error">
                        ⚠️ {error}
                    </div>
                {/if}

                <button type="submit">
                    Ingresar
                </button>

            </form>

        </div>

        <!-- Acceso de demostración -->
        <div class="demo">

            <span>Acceso demo:</span>

            <strong>admin@tallernube.com</strong>

            <span>·</span>

            <strong>123456</strong>

        </div>

        <p class="course">
            Consulta meteorológica · TALLER_NUBE
        </p>

    </div>

</div>

<style>

    .login-page {
        min-height: 100vh;
        width: 100%;
        position: relative;
        overflow: hidden;

        display: flex;
        justify-content: center;
        align-items: center;

        padding: 40px 20px;
        box-sizing: border-box;

        background:
            linear-gradient(
                135deg,
                #dbeafe 0%,
                #bfdbfe 45%,
                #e0f2fe 100%
            );

        font-family:
            Inter,
            system-ui,
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            sans-serif;
    }

    /* =========================
       CONTENEDOR PRINCIPAL
       ========================= */

    .content {
        width: 100%;
        max-width: 780px;
        position: relative;
        z-index: 2;
    }

    /* =========================
       ELEMENTOS DECORATIVOS
       ========================= */

    .sun {
        position: absolute;

        width: 190px;
        height: 190px;

        top: 35px;
        right: 70px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle at 35% 35%,
                #fff7cc 0%,
                #fde68a 45%,
                #facc15 100%
            );

        opacity: .9;

        box-shadow:
            0 15px 50px rgba(245, 158, 11, .25);
    }

    .cloud {
        position: absolute;

        font-size: 110px;

        opacity: .28;

        user-select: none;
        pointer-events: none;
    }

    .cloud-one {
        top: 250px;
        left: 170px;
    }

    .cloud-two {
        bottom: 80px;
        right: 130px;
        font-size: 80px;
        opacity: .2;
    }

    /* =========================
       ENCABEZADO
       ========================= */

    .hero {
        margin-bottom: 30px;
    }

    .weather-icon {
        font-size: 55px;
        margin-bottom: 8px;
    }

    h1 {
        margin: 0;

        font-size: clamp(42px, 7vw, 70px);

        line-height: 1.05;

        font-weight: 800;

        letter-spacing: -2px;

        color: #0f2f52;
    }

    h2 {
        margin: 15px 0 12px;

        font-size: clamp(24px, 4vw, 38px);

        line-height: 1.15;

        color: #173b61;

        font-weight: 750;
    }

    .hero p {
        max-width: 650px;

        margin: 0;

        font-size: 19px;

        line-height: 1.6;

        color: #526b83;
    }

    /* =========================
       TARJETA LOGIN
       ========================= */

    .login-card {
        width: 100%;

        box-sizing: border-box;

        padding: 32px;

        border-radius: 24px;

        background: rgba(255, 255, 255, .78);

        border: 1px solid rgba(255, 255, 255, .9);

        box-shadow:
            0 25px 60px rgba(30, 64, 175, .14);

        backdrop-filter: blur(12px);
    }

    /* =========================
       CAMPOS
       ========================= */

    .field {
        margin-bottom: 20px;
    }

    label {
        display: block;

        margin-bottom: 9px;

        font-size: 16px;

        font-weight: 700;

        color: #172b43;
    }

    input {
        width: 100%;

        box-sizing: border-box;

        padding: 17px 18px;

        border-radius: 15px;

        border: 1px solid #d5dde7;

        background: rgba(255, 255, 255, .95);

        color: #172b43;

        font-size: 17px;

        outline: none;

        transition:
            border-color .2s ease,
            box-shadow .2s ease;
    }

    input::placeholder {
        color: #94a3b8;
    }

    input:focus {
        border-color: #60a5fa;

        box-shadow:
            0 0 0 4px rgba(96, 165, 250, .15);
    }

    /* =========================
       ERROR
       ========================= */

    .error {
        margin-bottom: 18px;

        padding: 13px 15px;

        border-radius: 12px;

        background: #fee2e2;

        border: 1px solid #fecaca;

        color: #991b1b;

        text-align: center;

        font-size: 14px;

        font-weight: 600;
    }

    /* =========================
       BOTÓN
       ========================= */

    button {
        width: 100%;

        margin-top: 4px;

        padding: 17px;

        border: none;

        border-radius: 15px;

        background:
            linear-gradient(
                135deg,
                #5b8fc5,
                #3b82c4
            );

        color: white;

        font-size: 17px;

        font-weight: 800;

        cursor: pointer;

        box-shadow:
            0 10px 25px rgba(59, 130, 196, .25);

        transition:
            transform .2s ease,
            box-shadow .2s ease;
    }

    button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 14px 30px rgba(59, 130, 196, .32);
    }

    button:active {
        transform: translateY(0);
    }

    /* =========================
       DEMO
       ========================= */

    .demo {
        display: flex;

        justify-content: center;
        align-items: center;

        gap: 8px;

        margin-top: 22px;

        color: #526b83;

        font-size: 15px;
    }

    .demo strong {
        color: #315f8c;
    }

    /* =========================
       PIE
       ========================= */

    .course {
        margin: 12px 0 0;

        text-align: center;

        color: #607890;

        font-size: 14px;
    }

    /* =========================
       RESPONSIVE
       ========================= */

    @media (max-width: 700px) {

        .login-page {
            align-items: flex-start;

            padding-top: 45px;
        }

        .sun {
            width: 120px;
            height: 120px;

            top: 20px;
            right: -20px;
        }

        .cloud-one {
            left: -25px;
            top: 300px;
        }

        .cloud-two {
            right: -20px;
            bottom: 30px;
        }

        .hero {
            margin-bottom: 22px;
        }

        h1 {
            letter-spacing: -1px;
        }

        .hero p {
            font-size: 16px;
        }

        .login-card {
            padding: 24px;
        }

        .demo {
            flex-wrap: wrap;
        }
    }

</style>