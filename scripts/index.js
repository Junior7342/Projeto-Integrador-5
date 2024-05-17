document.addEventListener('DOMContentLoaded', (event) => {
    const emailInput = document.getElementById('email');
    const senhaInput = document.getElementById('senha');
    const botaoEntrar = document.getElementById('botao-entrar');

    function validarInputs(){
        const emailValue = emailInput.value.trim();
        const senhaValue = senhaInput.value.trim();

        // Código de verificação dos campos se não estão vazios

        if (emailValue && senhaValue){
            botaoEntrar.disabled = false;
        } else {
            botaoEntrar.disabled = true;
        }
    }

    // Listeners aos inputs para validar enquanto o usuário digita
    emailInput.addEventListener('input', validarInputs);
    senhaInput.addEventListener('input', validarInputs);

    // Iniciar com o botão desabilitado
    botaoEntrar.disabled = true;

});

function login_ok() {
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('senha').value.trim();

    if (email && password) {
        console.log("Login bem-sucedido");
        return true; //permite o envio do formulário
    } else {
        console.log("Preencha todos os campos");
        return false; // Impede o envio do formulário
    }

}