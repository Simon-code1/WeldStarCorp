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

    const projectCard = document.querySelector('.project-card');
    const projectContainer = document.querySelector('.project-container');
    let numCardsPerRow = 3; // Default to 3 cards per row
    let gutterWidth = 16; // Default gutter width (adjust as needed)
    
    function updateProjectLayout() {
      const containerWidth = projectContainer.clientWidth;
      const cardWidth = projectCard.clientWidth;
    
      // Update the number of cards per row and gutter width based on screen width
      if (containerWidth < 786) {
        numCardsPerRow = 2; // When screen width is less than 786px, display 2 cards per row
        gutterWidth = 8; // Adjust the gutter width as needed
      } else {
        numCardsPerRow = 3; // When screen width is 786px or more, display 3 cards per row
        gutterWidth = 16; // Adjust the gutter width as needed
      }
    
      const projectCards = projectContainer.querySelectorAll('.project-card');
      projectCards.forEach((card, index) => {
        if ((index + 1) % numCardsPerRow === 0) {
          card.style.marginRight = 0;
        } else {
          card.style.marginRight = gutterWidth + 'px';
        }
      });
    }
    
    // Call the function to initially set the layout and update on window resize
    updateProjectLayout();
    window.addEventListener('resize', updateProjectLayout);
    

    const sliderContainer = document.querySelector('.slider-container');
    const slides = document.querySelectorAll('.slider-slide');
    let currentIndex = 0;
    
    function showSlide(index) {

        const translateX = -index * 100;
        slides.forEach((slide) => {
            slide.style.transform = `translateX(${translateX}%)`;
          });
    }
    
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }
    
    setInterval(nextSlide, 4000); 
    showSlide(currentIndex); 