async function carregarAnimais(){
    const response = await axios.get('http://localhost:8000/animais')

    const animais = response.data

    const lista = document.getElementById('lista-animais')

    lista.innerHTML = ''

    animais.forEach(animal => {
        const item = document.createElement('li')

        const linha = `${animal.nome} - Idade: ${animal.idade} - Sexo: ${animal.sexo} - Cor: ${animal.cor}`
        
        item.innerText = linha
        
        lista.appendChild(item)
    })
}

function manipularFormulario(){
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')
    const input_idade = document.getElementById('idade')
    const input_sexo = document.getElementById('sexo')
    const input_cor = document.getElementById('cor')

    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        const nome_animal = input_nome.value
        const idade_animal = input_idade.value
        const sexo_animal = input_sexo.value
        const cor_animal = input_cor.value

        await axios.post('http://localhost:8000/animais', {
            nome: nome_animal,
            idade: idade_animal,
            sexo: sexo_animal,
            cor: cor_animal
        })
        
        carregarAnimais()
        alert(`${nome_animal} cadastrado`)
        input_nome.value = ''
        input_idade.value = ''
        input_sexo.value = ''
        input_cor.value = ''
    }
}

function App(){
    console.log('App iniciado')
    carregarAnimais()
    manipularFormulario()
}

App()
