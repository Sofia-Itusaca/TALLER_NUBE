<script>
    import Login from './pages/Login.svelte';
    import Dashboard from './pages/Dashboard.svelte';
    import Weather from './pages/Weather.svelte';

    let authenticated = false;
    let currentPage = 'dashboard';

    function handleLogin() {
        authenticated = true;
        currentPage = 'dashboard';
    }

    function handleLogout() {
        authenticated = false;
        currentPage = 'dashboard';
    }

    function showPage(page) {
        currentPage = page;
    }
</script>

{#if !authenticated}

    <Login onLogin={handleLogin} />

{:else if currentPage === 'dashboard'}

    <Dashboard
        onLogout={handleLogout}
        onNavigate={showPage}
    />

{:else if currentPage === 'weather'}

    <div class="weather-wrapper">

        <header class="navbar">

            <div class="brand">
                <span class="brand-icon">🌤️</span>

                <div>
                    <strong>Consultor de Clima</strong>
                    <small>Información meteorológica</small>
                </div>
            </div>

            <button
                class="back-button"
                on:click={() => showPage('dashboard')}
            >
                ← Inicio
            </button>

            <button
                class="logout"
                on:click={handleLogout}
            >
                Cerrar sesión
            </button>

        </header>

        <Weather />

    </div>

{/if}


<style>

    .weather-wrapper {
        min-height: 100vh;

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
       NAVBAR
       ========================= */

    .navbar {
        height: 72px;

        display: flex;

        align-items: center;

        gap: 12px;

        padding: 0 45px;

        box-sizing: border-box;

        background: rgba(255, 255, 255, .7);

        border-bottom: 1px solid rgba(255, 255, 255, .8);

        backdrop-filter: blur(12px);
    }


    .brand {
        display: flex;

        align-items: center;

        gap: 10px;

        margin-right: auto;
    }


    .brand-icon {
        font-size: 32px;
    }


    .brand strong {
        display: block;

        color: #173b61;

        font-size: 17px;
    }


    .brand small {
        display: block;

        margin-top: 2px;

        color: #607890;

        font-size: 11px;
    }


    /* =========================
       BOTONES
       ========================= */

    .back-button,
    .logout {
        padding: 9px 16px;

        border-radius: 10px;

        font-size: 14px;

        font-weight: 700;

        cursor: pointer;

        transition: .2s ease;
    }


    .back-button {
        border: 1px solid #b8cce0;

        background: rgba(255, 255, 255, .75);

        color: #315f8c;
    }


    .logout {
        border: 1px solid #b8cce0;

        background: rgba(255, 255, 255, .75);

        color: #315f8c;
    }


    .back-button:hover,
    .logout:hover {
        background: white;

        transform: translateY(-1px);
    }


    /* =========================
       RESPONSIVE
       ========================= */

    @media (max-width: 600px) {

        .navbar {
            padding: 0 15px;
        }

        .brand small {
            display: none;
        }

        .brand strong {
            font-size: 14px;
        }

        .back-button,
        .logout {
            padding: 8px 10px;

            font-size: 12px;
        }

    }

</style>