document.addEventListener('DOMContentLoaded', (event) => {
    const emailInput = document.getElementById('email');
    const senhaInput = document.getElementById('senha');
    const botaoEntrar = document.getElementById('botao-entrar');

    function validarInputs() {
        const emailValue = emailInput.value.trim();
        const senhaValue = senhaInput.value.trim();

        // Verificar se o email é válido
        const emailValido = validarEmail(emailValue);

        if (emailValido && senhaValue) {
            botaoEntrar.disabled = false;
        } else {
            botaoEntrar.disabled = true;
        }
    }

    function validarEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    emailInput.addEventListener('input', validarInputs);
    senhaInput.addEventListener('input', validarInputs);

    botaoEntrar.disabled = true;

    botaoEntrar.addEventListener('click', () => {
        if (!botaoEntrar.disabled) {
            window.location.href = '/html/bem-vindo.html';
        }
    });
});

function login_ok() {
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('senha').value.trim();

    if (email && password) {
        console.log("Login bem-sucedido");
        return true;
    } else {
        console.log("Preencha todos os campos");
        return false;
    }
}
