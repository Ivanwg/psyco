document.addEventListener('DOMContentLoaded', e => {

  const accs = Array.from(document.querySelectorAll('.js-acc-list'));
  accs.forEach(acc => {
    const items = Array.from(acc.querySelectorAll('.js-acc-item'));
    
    items.forEach(item => {
      const opener = item.querySelector('.js-toggler');
      const hidden = item.querySelector('.js-hidden');
      
      if (!opener || !hidden) return;
  
      const tl = gsap.timeline({paused: true});
      tl.fromTo(hidden, {height: 0}, {height: 'auto', duration: .3});
      opener.animation = tl;
  
      opener.onclick = e => {
        opener.classList.toggle('active');
        if (opener.animation) {
          opener.animation.pause();
        } else return;
  
        if (opener.classList.contains('active')) {
          opener.animation.restart();
        } else {
          opener.animation.reverse();
        }
      }
    });
  });
});