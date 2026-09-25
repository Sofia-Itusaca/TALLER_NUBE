<script>
    let city = '';
    let weather = null;
    let loading = false;
    let error = '';

    async function searchWeather() {
        error = '';
        weather = null;

        if (!city.trim()) {
            error = 'Ingresa una ciudad para consultar el clima.';
            return;
        }

        loading = true;

        try {
            const url =
                `http://127.0.0.1:8000/api/weather` +
                `?city=${encodeURIComponent(city.trim())}`;

            console.log('Consultando backend:', url);

            const response = await fetch(url);
            const data = await response.json();

            console.log('Backend status:', response.status);
            console.log('Backend respuesta:', data);

            if (!response.ok) {
                throw new Error(
                    data.detail || 'No se pudo obtener el clima.'
                );
            }

            weather = data;

        } catch (err) {
            console.error('ERROR COMPLETO:', err);
            error = err.message || 'No se pudo consultar el clima.';
        } finally {
            loading = false;
        }
    }
</script>

<div class="weather-page">

    <!-- Decoración -->
    <div class="sun"></div>
    <div class="cloud cloud-one">☁️</div>
    <div class="cloud cloud-two">☁️</div>

    <main class="weather-content">

        <!-- ENCABEZADO -->

        <section class="hero">

            <div class="hero-icon">
                🌤️
            </div>

            <h1>
                Consulta el clima
            </h1>

            <p>
                Consulta las condiciones meteorológicas
                de cualquier ciudad al instante.
            </p>

        </section>


        <!-- BUSCADOR -->

        <section class="search-card">

            <label for="city">
                🌎 ¿Qué ciudad quieres consultar?
            </label>

            <div class="search-box">

                <input
                    id="city"
                    type="text"
                    bind:value={city}
                    placeholder="Ejemplo: Tingo Maria"
                    on:keydown={(e) =>
                        e.key === 'Enter' && searchWeather()
                    }
                />

                <button
                    on:click={searchWeather}
                    disabled={loading}
                >
                    {#if loading}
                        Consultando...
                    {:else}
                        🔍 Consultar
                    {/if}
                </button>

            </div>

            <p class="search-help">
                Puedes ingresar el nombre de una ciudad,
                por ejemplo: Lima, Cusco o Tingo Maria.
            </p>

        </section>


        <!-- ERROR -->

        {#if error}

            <div class="error">

                <span class="error-icon">
                    ⚠️
                </span>

                <div>
                    <strong>No pudimos realizar la consulta</strong>

                    <p>
                        {error}
                    </p>
                </div>

            </div>

        {/if}


        <!-- RESULTADO -->

        {#if weather}

            <section class="result-card">

                <!-- Ciudad -->

                <div class="location">

                    <div>

                        <span class="location-label">
                            Clima actual
                        </span>

                        <h2>
                            {weather.city}
                        </h2>

                        <p>
                            📍 {weather.country}
                        </p>

                    </div>

                    <button
                        class="new-search"
                        on:click={() => {
                            weather = null;
                            city = '';
                        }}
                    >
                        Nueva consulta
                    </button>

                </div>


                <!-- PRINCIPAL -->

                <div class="main-weather">

                    <div class="weather-icon">

                        <img
                            src={weather.icon}
                            alt={weather.description}
                        />

                    </div>


                    <div class="temperature-box">

                        <span class="temperature">
                            {weather.temperature}°
                        </span>

                        <span class="unit">
                            C
                        </span>

                        <p>
                            {weather.description}
                        </p>

                    </div>

                </div>


                <!-- DETALLES -->

                <div class="details">

                    <div class="detail">

                        <div class="detail-icon">
                            🌡️
                        </div>

                        <div>

                            <span>
                                Sensación térmica
                            </span>

                            <strong>
                                {weather.feelsLike}°C
                            </strong>

                        </div>

                    </div>


                    <div class="detail">

                        <div class="detail-icon">
                            💧
                        </div>

                        <div>

                            <span>
                                Humedad
                            </span>

                            <strong>
                                {weather.humidity}%
                            </strong>

                        </div>

                    </div>


                    <div class="detail">

                        <div class="detail-icon">
                            💨
                        </div>

                        <div>

                            <span>
                                Viento
                            </span>

                            <strong>
                                {weather.wind} km/h
                            </strong>

                        </div>

                    </div>

                </div>


                <!-- FUENTE -->

                <div class="source">

                    Datos meteorológicos proporcionados por
                    <strong>
                        {weather.source}
                    </strong>

                </div>

            </section>

        {:else if !loading && !error}

            <!-- ESTADO INICIAL -->

            <section class="empty-state">

                <div class="empty-icon">
                    🌎
                </div>

                <h2>
                    ¿Quieres conocer el clima?
                </h2>

                <p>
                    Escribe una ciudad arriba para conocer
                    su temperatura y condiciones actuales.
                </p>

            </section>

        {/if}

    </main>

</div>


<style>

    /* =========================
       PÁGINA
       ========================= */

    .weather-page {
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

        width: 210px;
        height: 210px;

        top: 40px;
        right: 60px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle at 35% 35%,
                #fff7cc,
                #fde68a 50%,
                #facc15
            );

        opacity: .7;

        box-shadow:
            0 20px 60px rgba(245, 158, 11, .2);
    }


    .cloud {
        position: absolute;

        font-size: 130px;

        opacity: .2;

        pointer-events: none;

        user-select: none;
    }


    .cloud-one {
        top: 230px;
        left: 40px;
    }


    .cloud-two {
        bottom: 70px;
        right: 100px;

        font-size: 90px;
    }


    /* =========================
       CONTENIDO
       ========================= */

    .weather-content {
        position: relative;

        z-index: 2;

        width: 100%;

        max-width: 1000px;

        margin: 0 auto;

        padding: 70px 30px;

        box-sizing: border-box;
    }


    /* =========================
       HERO
       ========================= */

    .hero {
        text-align: center;

        margin-bottom: 35px;
    }


    .hero-icon {
        font-size: 65px;

        margin-bottom: 5px;
    }


    .hero h1 {
        margin: 0;

        font-size: clamp(40px, 6vw, 64px);

        line-height: 1.05;

        letter-spacing: -2px;

        color: #0f2f52;

        font-weight: 800;
    }


    .hero p {
        max-width: 650px;

        margin: 15px auto 0;

        color: #526b83;

        font-size: 18px;

        line-height: 1.6;
    }


    /* =========================
       BUSCADOR
       ========================= */

    .search-card {
        padding: 28px;

        border-radius: 22px;

        background: rgba(255, 255, 255, .72);

        border: 1px solid rgba(255, 255, 255, .85);

        box-shadow:
            0 18px 45px rgba(30, 64, 175, .1);

        backdrop-filter: blur(10px);

        margin-bottom: 25px;
    }


    .search-card label {
        display: block;

        margin-bottom: 12px;

        color: #173b61;

        font-size: 17px;

        font-weight: 750;
    }


    .search-box {
        display: flex;

        gap: 12px;
    }


    .search-box input {
        flex: 1;

        min-width: 0;

        padding: 16px 18px;

        border-radius: 14px;

        border: 1px solid #cbd5e1;

        background: rgba(255, 255, 255, .95);

        color: #173b61;

        font-size: 17px;

        outline: none;

        transition: .2s ease;
    }


    .search-box input:focus {
        border-color: #60a5fa;

        box-shadow:
            0 0 0 4px rgba(96, 165, 250, .15);
    }


    .search-box input::placeholder {
        color: #94a3b8;
    }


    .search-box button {
        min-width: 150px;

        padding: 15px 24px;

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
            0 10px 24px rgba(59, 130, 196, .22);

        transition: .2s ease;
    }


    .search-box button:hover:not(:disabled) {
        transform: translateY(-2px);

        box-shadow:
            0 14px 28px rgba(59, 130, 196, .3);
    }


    .search-box button:disabled {
        opacity: .65;

        cursor: wait;
    }


    .search-help {
        margin: 12px 0 0;

        color: #71869b;

        font-size: 13px;
    }


    /* =========================
       ERROR
       ========================= */

    .error {
        display: flex;

        align-items: flex-start;

        gap: 13px;

        padding: 17px;

        margin-bottom: 25px;

        border-radius: 15px;

        background: #fff1f2;

        border: 1px solid #fecdd3;

        color: #9f1239;
    }


    .error-icon {
        font-size: 22px;
    }


    .error strong {
        display: block;

        margin-bottom: 4px;
    }


    .error p {
        margin: 0;

        font-size: 14px;
    }


    /* =========================
       RESULTADO
       ========================= */

    .result-card {
        padding: 32px;

        border-radius: 26px;

        background: rgba(255, 255, 255, .8);

        border: 1px solid rgba(255, 255, 255, .9);

        box-shadow:
            0 22px 55px rgba(30, 64, 175, .14);

        backdrop-filter: blur(12px);
    }


    /* =========================
       UBICACIÓN
       ========================= */

    .location {
        display: flex;

        justify-content: space-between;

        align-items: flex-start;

        gap: 20px;

        margin-bottom: 20px;
    }


    .location-label {
        display: block;

        margin-bottom: 5px;

        color: #6b8299;

        font-size: 13px;

        text-transform: uppercase;

        letter-spacing: .08em;

        font-weight: 700;
    }


    .location h2 {
        margin: 0;

        color: #0f2f52;

        font-size: 32px;
    }


    .location p {
        margin: 5px 0 0;

        color: #607890;

        font-size: 15px;
    }


    .new-search {
        padding: 10px 15px;

        border: 1px solid #b8cce0;

        border-radius: 10px;

        background: rgba(255, 255, 255, .8);

        color: #315f8c;

        font-weight: 700;

        cursor: pointer;

        transition: .2s ease;
    }


    .new-search:hover {
        background: white;
    }


    /* =========================
       CLIMA PRINCIPAL
       ========================= */

    .main-weather {
        display: flex;

        align-items: center;

        justify-content: center;

        gap: 30px;

        padding: 20px 0 30px;
    }


    .weather-icon img {
        width: 120px;

        height: 120px;

        image-rendering: auto;
    }


    .temperature-box {
        display: flex;

        align-items: baseline;

        flex-wrap: wrap;
    }


    .temperature {
        color: #0f2f52;

        font-size: clamp(70px, 10vw, 105px);

        line-height: .9;

        font-weight: 800;

        letter-spacing: -5px;
    }


    .unit {
        margin-left: 5px;

        color: #315f8c;

        font-size: 34px;

        font-weight: 700;
    }


    .temperature-box p {
        width: 100%;

        margin: 12px 0 0;

        color: #526b83;

        font-size: 20px;

        font-weight: 600;

        text-transform: capitalize;
    }


    /* =========================
       DETALLES
       ========================= */

    .details {
        display: grid;

        grid-template-columns:
            repeat(3, 1fr);

        gap: 15px;
    }


    .detail {
        display: flex;

        align-items: center;

        gap: 14px;

        padding: 18px;

        border-radius: 16px;

        background: rgba(219, 234, 254, .55);

        border: 1px solid rgba(148, 163, 184, .2);
    }


    .detail-icon {
        width: 48px;

        height: 48px;

        display: flex;

        align-items: center;

        justify-content: center;

        flex-shrink: 0;

        border-radius: 13px;

        background: rgba(255, 255, 255, .8);

        font-size: 24px;
    }


    .detail span {
        display: block;

        margin-bottom: 5px;

        color: #6b8299;

        font-size: 13px;
    }


    .detail strong {
        display: block;

        color: #173b61;

        font-size: 19px;
    }


    /* =========================
       FUENTE
       ========================= */

    .source {
        margin-top: 25px;

        padding-top: 18px;

        border-top: 1px solid #dbe5ef;

        text-align: center;

        color: #71869b;

        font-size: 13px;
    }


    .source strong {
        color: #315f8c;
    }


    /* =========================
       ESTADO INICIAL
       ========================= */

    .empty-state {
        padding: 50px 30px;

        text-align: center;

        border-radius: 22px;

        background: rgba(255, 255, 255, .48);

        border: 1px solid rgba(255, 255, 255, .7);
    }


    .empty-icon {
        font-size: 60px;

        margin-bottom: 10px;
    }


    .empty-state h2 {
        margin: 0;

        color: #173b61;

        font-size: 26px;
    }


    .empty-state p {
        max-width: 520px;

        margin: 10px auto 0;

        color: #607890;

        line-height: 1.6;
    }


    /* =========================
       RESPONSIVE
       ========================= */

    @media (max-width: 700px) {

        .weather-content {
            padding: 45px 18px;
        }


        .sun {
            width: 130px;
            height: 130px;

            top: 20px;
            right: -20px;
        }


        .search-box {
            flex-direction: column;
        }


        .search-box button {
            width: 100%;
        }


        .details {
            grid-template-columns: 1fr;
        }


        .location {
            flex-direction: column;
        }


        .new-search {
            width: 100%;
        }


        .main-weather {
            flex-direction: column;

            text-align: center;
        }


        .temperature-box {
            justify-content: center;
        }


        .temperature-box p {
            text-align: center;
        }


        .result-card {
            padding: 24px;
        }

    }

</style>