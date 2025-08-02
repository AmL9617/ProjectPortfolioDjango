/*===== MENU SHOW =====*/ 
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}
showMenu('nav-toggle','nav-menu')

/*===== REMOVE MENU MOBILE =====*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*===== SCROLL SECTIONS ACTIVE LINK =====*/
const sections = document.querySelectorAll('section[id]');

window.addEventListener('scroll', scrollActive);

function scrollActive() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - window.innerHeight / 2; // Adjusted to reveal at mid-viewport
        const sectionId = current.getAttribute('id');

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active');
        } else {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active');
        }
    });
}

window.addEventListener('resize', () => {
    sr.sync(); // Recalculate reveal positions on resize
});


/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',           // Direction from which elements appear
    distance: '80px',        // Distance they travel to reveal
    duration: 2000,          // Duration of animation in ms
    reset: true              // Elements reappear when scrolling up
})

/*SCROLL HOME*/
sr.reveal('.home__title', {})
sr.reveal('.home__scroll', {delay: 200})
sr.reveal('.home__img', {origin:'right', delay: 400})

/*SCROLL ABOUT*/
sr.reveal('.about__img', {delay: 500})
sr.reveal('.about__subtitle', {
    origin: 'bottom',
    distance: '20px',        // Less distance so it starts revealing sooner
    delay: 0,                // Remove delay so it appears immediately
    duration: 800,           // Adjust duration to make reveal smoother
    viewOffset: { top: 300, bottom: 0 }, // Adjust this to trigger reveal earlier
});
sr.reveal('.about__profession', {
    origin: 'bottom',
    distance: '20px',        // Less distance so it starts revealing sooner
    delay: 0,                // Remove delay so it appears immediately
    duration: 800,           // Adjust duration to make reveal smoother
    viewOffset: { top: 300, bottom: 0 }, // Adjust this to trigger reveal earlier
});
/* Adjust ScrollReveal settings for About Text */
sr.reveal('.about__text', {
    origin: 'bottom',
    distance: '20px',        // Less distance so it starts revealing sooner
    delay: 0,                // Remove delay so it appears immediately
    duration: 800,           // Adjust duration to make reveal smoother
    viewOffset: { top: 300, bottom: 0 }, // Adjust this to trigger reveal earlier
});



/*SCROLL SKILLS*/
sr.reveal('.skills__subtitle', {})
sr.reveal('.skills__name', {distance: '20px', delay: 50, interval: 100})
sr.reveal('.skills__img', {delay: 400})

/*SCROLL PROJECTS*/
sr.reveal('.project__img', {interval: 200})

/*SCROLL CONTACT*/
sr.reveal('.contact__subtitle', {interval:200, viewOffset: { top: -200, right: 0, bottom: 0, left: 0 }})
sr.reveal('.contact__text', {interval: 200, viewOffset: { top: -200, right: 0, bottom: 0, left: 0 }})
sr.reveal('.contact__input', {delay: 400})
sr.reveal('.contact__button', {delay: 600})
