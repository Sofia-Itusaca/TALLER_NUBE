<script>
    export let onLogout;
    export let onNavigate;
    export let currentPage;
</script>

<div class="app">

    <header>
        <div class="brand">
            <span>☁️</span>
            <div>
                <strong>TALLER_NUBE</strong>
                <small>Cloud Management</small>
            </div>
        </div>

        <div class="user">
            <div class="avatar">A</div>
            <div>
                <strong>Administrador</strong>
                <small>admin@tallernube.com</small>
            </div>

            <button class="logout" on:click={onLogout}>
                Cerrar sesión
            </button>
        </div>
    </header>

    <div class="layout">

        <aside>
            <p class="menu-title">MENÚ PRINCIPAL</p>

            <button class="menu active">
                📊
                <span>Dashboard</span>
            </button>

            <button
                class:active={currentPage === 'weather'}
                class="menu"
                on:click={() => onNavigate('weather')}
            >
                🌤️
                <span>Consulta clima</span>
            </button>

            <div class="sidebar-bottom">
                <p>☁️ Azure</p>
                <small>Aplicación en desarrollo</small>
            </div>
        </aside>

        <main>

            <div class="welcome">
                <div>
                    <p>Panel principal</p>
                    <h1>Bienvenido a TALLER_NUBE</h1>
                    <span>
                        Plataforma preparada para despliegue en la nube.
                    </span>
                </div>
            </div>

            <section class="cards">

                <article class="card">
                    <div class="icon blue">☁️</div>
                    <div>
                        <small>PLATAFORMA</small>
                        <h2>Azure</h2>
                        <span class="status">● Preparado</span>
                    </div>
                </article>

                <article class="card">
                    <div class="icon green">✓</div>
                    <div>
                        <small>APLICACIÓN</small>
                        <h2>Operativa</h2>
                        <span class="status">● Funcionando</span>
                    </div>
                </article>

                <article class="card">
                    <div class="icon purple">⚡</div>
                    <div>
                        <small>ENTORNO</small>
                        <h2>Desarrollo</h2>
                        <span class="status">● Activo</span>
                    </div>
                </article>

            </section>

            <section class="information">

                <div class="panel">
                    <h2>Estado del sistema</h2>

                    <div class="system-row">
                        <span>Frontend</span>
                        <strong class="online">ONLINE</strong>
                    </div>

                    <div class="system-row">
                        <span>Servidor web</span>
                        <strong class="online">PREPARADO</strong>
                    </div>

                    <div class="system-row">
                        <span>Docker</span>
                        <strong class="online">CONFIGURADO</strong>
                    </div>

                    <div class="system-row">
                        <span>Azure</span>
                        <strong class="pending">PENDIENTE</strong>
                    </div>
                </div>

                <div class="panel">
                    <h2>Próximas funcionalidades</h2>

                    <div class="feature">
                        <span>🔐</span>
                        <div>
                            <strong>Autenticación</strong>
                            <small>Sistema de acceso</small>
                        </div>
                    </div>

                    <div class="feature">
                        <span>🌤️</span>
                        <div>
                            <strong>Consulta de clima</strong>
                            <small>Integración con API</small>
                        </div>
                    </div>

                    <div class="feature">
                        <span>☁️</span>
                        <div>
                            <strong>Despliegue Azure</strong>
                            <small>Publicación cloud</small>
                        </div>
                    </div>
                </div>

            </section>

        </main>

    </div>

</div>

<style>
    :global(body) {
        background: #0f172a;
        color: #e2e8f0;
    }

    .app {
        min-height: 100vh;
        background: #0f172a;
    }

    header {
        height: 72px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 30px;
        background: #111827;
        border-bottom: 1px solid #263244;
    }

    .brand,
    .user {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand > span {
        font-size: 28px;
    }

    .brand strong {
        display: block;
        font-size: 17px;
    }

    .brand small,
    .user small {
        display: block;
        color: #64748b;
        margin-top: 3px;
    }

    .user {
        gap: 10px;
    }

    .avatar {
        width: 38px;
        height: 38px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        background: #0284c7;
        font-weight: bold;
    }

    .logout {
        margin-left: 15px;
        padding: 8px 14px;
        border: 1px solid #334155;
        border-radius: 8px;
        background: transparent;
        color: #cbd5e1;
        cursor: pointer;
    }

    .logout:hover {
        background: #1e293b;
    }

    .layout {
        display: flex;
        min-height: calc(100vh - 73px);
    }

    aside {
        width: 230px;
        padding: 25px 15px;
        background: #111827;
        border-right: 1px solid #263244;
        position: relative;
    }

    .menu-title {
        font-size: 11px;
        color: #64748b;
        font-weight: bold;
        margin: 0 10px 15px;
    }

    .menu {
        width: 100%;
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px;
        margin-bottom: 7px;
        border: 0;
        border-radius: 8px;
        background: transparent;
        color: #94a3b8;
        text-align: left;
        cursor: pointer;
    }

    .menu:hover,
    .menu.active {
        background: #1e3a5f;
        color: #38bdf8;
    }

    .sidebar-bottom {
        position: absolute;
        bottom: 25px;
        left: 20px;
        color: #38bdf8;
    }

    .sidebar-bottom small {
        color: #64748b;
    }

    main {
        flex: 1;
        padding: 35px;
        overflow: auto;
    }

    .welcome p {
        color: #38bdf8;
        margin-bottom: 5px;
    }

    .welcome h1 {
        margin: 0 0 8px;
        font-size: 30px;
    }

    .welcome span {
        color: #94a3b8;
    }

    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-top: 30px;
    }

    .card,
    .panel {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
    }

    .card {
        display: flex;
        gap: 15px;
        padding: 22px;
    }

    .icon {
        width: 48px;
        height: 48px;
        display: grid;
        place-items: center;
        border-radius: 10px;
        font-size: 22px;
    }

    .blue {
        background: #082f49;
        color: #38bdf8;
    }

    .green {
        background: #052e16;
        color: #4ade80;
    }

    .purple {
        background: #2e1065;
        color: #c084fc;
    }

    .card small {
        color: #64748b;
        font-size: 10px;
    }

    .card h2 {
        margin: 5px 0;
    }

    .status {
        color: #4ade80;
        font-size: 12px;
    }

    .information {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin-top: 20px;
    }

    .panel {
        padding: 22px;
    }

    .panel h2 {
        margin-top: 0;
        font-size: 17px;
    }

    .system-row {
        display: flex;
        justify-content: space-between;
        padding: 14px 0;
        border-bottom: 1px solid #334155;
    }

    .system-row:last-child {
        border-bottom: 0;
    }

    .online {
        color: #4ade80;
        font-size: 12px;
    }

    .pending {
        color: #fbbf24;
        font-size: 12px;
    }

    .feature {
        display: flex;
        gap: 12px;
        padding: 13px 0;
        border-bottom: 1px solid #334155;
    }

    .feature:last-child {
        border-bottom: 0;
    }

    .feature > span {
        font-size: 20px;
    }

    .feature strong,
    .feature small {
        display: block;
    }

    .feature small {
        color: #64748b;
        margin-top: 3px;
    }

    @media (max-width: 900px) {
        aside {
            width: 180px;
        }

        .cards {
            grid-template-columns: 1fr;
        }

        .information {
            grid-template-columns: 1fr;
        }
    }
</style>