<script>
    export let onLogout;
    export let onNavigate;
</script>

<div class="dashboard">

    <!-- Decoración -->
    <div class="sun"></div>
    <div class="cloud cloud-one">☁️</div>
    <div class="cloud cloud-two">☁️</div>

    <!-- NAVBAR -->
    <header class="navbar">

        <div class="brand">
            <span class="brand-icon">🌤️</span>

            <div>
                <strong>Consultor de Clima</strong>
                <small>Información meteorológica</small>
            </div>
        </div>

        <button class="logout" on:click={onLogout}>
            Cerrar sesión
        </button>

    </header>


    <!-- CONTENIDO -->
    <main class="main-content">

        <section class="hero">

            <div class="hero-icon">
                ☀️
            </div>

            <h1>
                Consulta el clima
            </h1>

            <p>
                Descubre las condiciones meteorológicas
                de cualquier ciudad al instante.
            </p>

            <button
                class="weather-button"
                on:click={() => onNavigate('weather')}
            >
                <span>🌤️</span>
                Consultar clima
            </button>

        </section>


        <!-- INFORMACIÓN -->
        <section class="features">

            <div class="feature-card">

                <div class="feature-icon">
                    🌡️
                </div>

                <h3>
                    Temperatura
                </h3>

                <p>
                    Conoce la temperatura actual
                    de tu ciudad.
                </p>

            </div>


            <div class="feature-card">

                <div class="feature-icon">
                    💧
                </div>

                <h3>
                    Humedad
                </h3>

                <p>
                    Consulta el porcentaje de
                    humedad en el ambiente.
                </p>

            </div>


            <div class="feature-card">

                <div class="feature-icon">
                    💨
                </div>

                <h3>
                    Viento
                </h3>

                <p>
                    Conoce la velocidad actual
                    del viento.
                </p>

            </div>

        </section>

    </main>


    <!-- FOOTER -->
    <footer>
        TALLER_NUBE · Consulta meteorológica
    </footer>

</div>


<style>

    .dashboard {
        min-height: 100vh;

        position: relative;

        overflow: hidden;

        background:
            linear-gradient(
                135deg,
                #dbeafe 0%,
                #bfdbfe 45%,
                #e0f2fe 100%
            );

        color: #173b61;

        font-family:
            Inter,
            system-ui,
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            sans-serif;
    }


    /* =========================
       DECORACIÓN
       ========================= */

    .sun {
        position: absolute;

        width: 220px;
        height: 220px;

        top: 60px;
        right: 70px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle at 35% 35%,
                #fff7cc,
                #fde68a 50%,
                #facc15
            );

        opacity: .75;

        box-shadow:
            0 20px 60px rgba(245, 158, 11, .2);
    }


    .cloud {
        position: absolute;

        font-size: 130px;

        opacity: .22;

        pointer-events: none;

        user-select: none;
    }


    .cloud-one {
        top: 280px;
        left: 80px;
    }


    .cloud-two {
        bottom: 80px;
        right: 120px;

        font-size: 90px;
    }


    /* =========================
       NAVBAR
       ========================= */

    .navbar {
        position: relative;

        z-index: 5;

        height: 78px;

        display: flex;

        justify-content: space-between;

        align-items: center;

        padding: 0 55px;

        box-sizing: border-box;

        background: rgba(255, 255, 255, .58);

        border-bottom: 1px solid rgba(255, 255, 255, .7);

        backdrop-filter: blur(12px);
    }


    .brand {
        display: flex;

        align-items: center;

        gap: 12px;
    }


    .brand-icon {
        font-size: 34px;
    }


    .brand strong {
        display: block;

        color: #173b61;

        font-size: 18px;
    }


    .brand small {
        display: block;

        margin-top: 2px;

        color: #607890;

        font-size: 12px;
    }


    .logout {
        padding: 10px 18px;

        border-radius: 10px;

        border: 1px solid #9bb6d1;

        background: rgba(255, 255, 255, .7);

        color: #315f8c;

        font-size: 14px;

        font-weight: 700;

        cursor: pointer;

        transition: .2s ease;
    }


    .logout:hover {
        background: white;

        transform: translateY(-1px);
    }


    /* =========================
       CONTENIDO PRINCIPAL
       ========================= */

    .main-content {
        position: relative;

        z-index: 2;

        max-width: 1100px;

        margin: 0 auto;

        padding: 80px 30px 40px;

        box-sizing: border-box;
    }


    .hero {
        text-align: center;

        max-width: 760px;

        margin: 0 auto 65px;
    }


    .hero-icon {
        font-size: 70px;

        margin-bottom: 10px;
    }


    .hero h1 {
        margin: 0;

        font-size: clamp(42px, 6vw, 68px);

        line-height: 1.05;

        letter-spacing: -2px;

        color: #0f2f52;

        font-weight: 800;
    }


    .hero p {
        margin: 18px auto 30px;

        max-width: 650px;

        color: #526b83;

        font-size: 19px;

        line-height: 1.6;
    }


    /* =========================
       BOTÓN CLIMA
       ========================= */

    .weather-button {
        display: inline-flex;

        align-items: center;

        justify-content: center;

        gap: 10px;

        padding: 16px 30px;

        border: none;

        border-radius: 14px;

        background:
            linear-gradient(
                135deg,
                #5b8fc5,
                #3b82c4
            );

        color: white;

        font-size: 16px;

        font-weight: 800;

        cursor: pointer;

        box-shadow:
            0 12px 28px rgba(59, 130, 196, .25);

        transition: .2s ease;
    }


    .weather-button:hover {
        transform: translateY(-3px);

        box-shadow:
            0 16px 35px rgba(59, 130, 196, .3);
    }


    .weather-button span {
        font-size: 22px;
    }


    /* =========================
       TARJETAS
       ========================= */

    .features {
        display: grid;

        grid-template-columns:
            repeat(3, 1fr);

        gap: 22px;
    }


    .feature-card {
        padding: 28px;

        text-align: center;

        border-radius: 22px;

        background: rgba(255, 255, 255, .68);

        border: 1px solid rgba(255, 255, 255, .85);

        box-shadow:
            0 15px 35px rgba(30, 64, 175, .1);

        backdrop-filter: blur(10px);

        transition: .2s ease;
    }


    .feature-card:hover {
        transform: translateY(-5px);

        background: rgba(255, 255, 255, .82);
    }


    .feature-icon {
        font-size: 38px;

        margin-bottom: 12px;
    }


    .feature-card h3 {
        margin: 0 0 8px;

        color: #173b61;

        font-size: 20px;
    }


    .feature-card p {
        margin: 0;

        color: #607890;

        line-height: 1.5;

        font-size: 14px;
    }


    /* =========================
       FOOTER
       ========================= */

    footer {
        position: relative;

        z-index: 2;

        padding: 25px;

        text-align: center;

        color: #607890;

        font-size: 13px;
    }


    /* =========================
       RESPONSIVE
       ========================= */

    @media (max-width: 800px) {

        .navbar {
            padding: 0 20px;
        }

        .main-content {
            padding-top: 55px;
        }

        .features {
            grid-template-columns: 1fr;
        }

        .sun {
            width: 140px;
            height: 140px;

            right: -20px;
        }

    }


    @media (max-width: 500px) {

        .brand small {
            display: none;
        }

        .brand strong {
            font-size: 15px;
        }

        .logout {
            padding: 8px 12px;
        }

        .hero h1 {
            letter-spacing: -1px;
        }

        .hero p {
            font-size: 16px;
        }

    }

</style>