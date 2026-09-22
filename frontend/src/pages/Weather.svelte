<script>
    const API_KEY = import.meta.env.VITE_WEATHERAPI_KEY;

    let city = '';
    let weather = null;
    let loading = false;
    let error = '';

    async function searchWeather() {
        error = '';
        weather = null;

        if (!city.trim()) {
            error = 'Ingresa una ciudad.';
            return;
        }

        if (!API_KEY) {
            error = 'No se encontró la API Key de WeatherAPI.';
            return;
        }

        loading = true;

        try {
            const url =
                `https://api.weatherapi.com/v1/current.json` +
                `?key=${API_KEY}` +
                `&q=${encodeURIComponent(city.trim())}` +
                `&lang=es`;

            console.log('Consultando WeatherAPI:', city);

            const response = await fetch(url);
            const data = await response.json();

            console.log('WeatherAPI status:', response.status);
            console.log('WeatherAPI respuesta:', data);

            if (!response.ok) {
                throw new Error(
                    data.error?.message || 'Error al consultar WeatherAPI.'
                );
            }

            weather = {
                city: data.location.name,
                country: data.location.country,
                temperature: Math.round(data.current.temp_c),
                feelsLike: Math.round(data.current.feelslike_c),
                humidity: data.current.humidity,
                wind: data.current.wind_kph,
                description: data.current.condition.text,
                icon: `https:${data.current.condition.icon}`
            };

        } catch (err) {
            console.error('ERROR COMPLETO:', err);
            error = err.message || 'No se pudo consultar el clima.';
        } finally {
            loading = false;
        }
    }
</script>

<div class="weather-card">

    <div class="header">
        <h1>🌤️ Consulta del clima</h1>
        <p>Consulta el clima actual de cualquier ciudad.</p>
    </div>

    <div class="search-box">
        <input
            type="text"
            bind:value={city}
            placeholder="Ejemplo: Tingo Maria"
            on:keydown={(e) => e.key === 'Enter' && searchWeather()}
        />

        <button on:click={searchWeather} disabled={loading}>
            {loading ? 'Consultando...' : 'Consultar'}
        </button>
    </div>

    {#if error}
        <div class="error">
            ⚠️ {error}
        </div>
    {/if}

    {#if weather}
        <div class="result">

            <div class="location">
                <h2>{weather.city}</h2>
                <p>{weather.country}</p>
            </div>

            <div class="main-weather">
                <img
                    src={weather.icon}
                    alt={weather.description}
                />

                <div>
                    <span class="temperature">
                        {weather.temperature}°C
                    </span>

                    <p>{weather.description}</p>
                </div>
            </div>

            <div class="details">

                <div class="detail">
                    <span>🌡️</span>
                    <div>
                        <small>Sensación térmica</small>
                        <strong>{weather.feelsLike}°C</strong>
                    </div>
                </div>

                <div class="detail">
                    <span>💧</span>
                    <div>
                        <small>Humedad</small>
                        <strong>{weather.humidity}%</strong>
                    </div>
                </div>

                <div class="detail">
                    <span>💨</span>
                    <div>
                        <small>Viento</small>
                        <strong>{weather.wind} km/h</strong>
                    </div>
                </div>

            </div>

        </div>
    {/if}

</div>

<style>
    .weather-card {
        max-width: 900px;
        margin: 0 auto;
    }

    .header {
        margin-bottom: 30px;
    }

    .header h1 {
        margin: 0;
        font-size: 32px;
        color: #f8fafc;
    }

    .header p {
        color: #94a3b8;
        margin-top: 8px;
    }

    .search-box {
        display: flex;
        gap: 12px;
        margin-bottom: 25px;
    }

    .search-box input {
        flex: 1;
        padding: 14px 16px;
        border-radius: 10px;
        border: 1px solid #334155;
        background: #1e293b;
        color: white;
        font-size: 16px;
        outline: none;
    }

    .search-box input:focus {
        border-color: #38bdf8;
    }

    .search-box button {
        padding: 14px 24px;
        border: none;
        border-radius: 10px;
        background: #0ea5e9;
        color: white;
        font-weight: bold;
        cursor: pointer;
    }

    .search-box button:hover {
        background: #0284c7;
    }

    .search-box button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }

    .error {
        background: #451a1a;
        border: 1px solid #7f1d1d;
        color: #fecaca;
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 20px;
    }

    .result {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 30px;
    }

    .location h2 {
        margin: 0;
        color: white;
        font-size: 28px;
    }

    .location p {
        margin: 5px 0 25px;
        color: #94a3b8;
    }

    .main-weather {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 30px;
    }

    .main-weather img {
        width: 100px;
        height: 100px;
    }

    .temperature {
        font-size: 48px;
        font-weight: bold;
        color: white;
    }

    .main-weather p {
        margin: 5px 0 0;
        color: #cbd5e1;
        text-transform: capitalize;
    }

    .details {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }

    .detail {
        display: flex;
        align-items: center;
        gap: 12px;
        background: #0f172a;
        padding: 15px;
        border-radius: 12px;
    }

    .detail > span {
        font-size: 25px;
    }

    .detail small {
        display: block;
        color: #94a3b8;
        margin-bottom: 4px;
    }

    .detail strong {
        color: white;
    }

    @media (max-width: 700px) {
        .details {
            grid-template-columns: 1fr;
        }

        .search-box {
            flex-direction: column;
        }
    }
</style>