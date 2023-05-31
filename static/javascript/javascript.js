    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const navBar = document.querySelector('.nav-bar');
    const navItem = document.querySelector('.nav-item')

    hamburgerMenu.addEventListener('click', () => {
    hamburgerMenu.classList.toggle('active');
    navBar.classList.toggle('active');
    navItem.classList.toggle('active');
    });

    document.querySelectorAll(".nav-bar").forEach(n => n.addEventListener("click",() =>{
        hamburgerMenu.classList.remove("active");
        navBar.classList.remove("active");

    }))


    const projectContainer = document.querySelector('.project-container');
    const containerWidth = projectContainer.clientWidth;
    const cardWidth = projectCard.clientWidth;
    const numCardsPerRow = Math.floor(containerWidth / cardWidth);
    const excessSpace = containerWidth - numCardsPerRow * cardWidth;
    const gutterWidth = excessSpace / (numCardsPerRow - 1);

     const projectCards = projectContainer.querySelectorAll('.project-card');
     projectCards.forEach((card, index) => {
        if ((index + 1) % numCardsPerRow === 0) {
         card.style.marginRight = 0;
     } else {
        card.style.marginRight = gutterWidth + 'px';
            }
    });
    