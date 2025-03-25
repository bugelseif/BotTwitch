const pessoa = document.querySelectorAll('#pessoa')
pessoa.forEach(pessoa => {
    console.log(pessoa.textContent)

    const posicaoAleatoriaX = Math.random() * (500);
    const posicaoAleatoriaY = Math.random() * (500);
    pessoa.style.left = `${posicaoAleatoriaX}px`;
    pessoa.style.top = `${posicaoAleatoriaY}px`;

    
    setInterval(() => {move(pessoa)}, 1000);
});

const move = function(item){
let xm = Math.random() * 500
gsap.to(item, {duration: 20, x:xm})
let ym = Math.random() * 500
gsap.to(item, {duration: 20, y:ym})
}