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

{#if authenticated}

    <Dashboard
        onLogout={handleLogout}
        onNavigate={showPage}
        currentPage={currentPage}
    />

    {#if currentPage === 'weather'}
        <div class="weather-container">
            <Weather />
        </div>
    {/if}

{:else}

    <Login onLogin={handleLogin} />

{/if}

<style>
    .weather-container {
        position: absolute;
        left: 230px;
        top: 73px;
        right: 0;
        min-height: calc(100vh - 73px);
        padding: 35px;
        box-sizing: border-box;
        background: #0f172a;
        color: #e2e8f0;
    }
</style>