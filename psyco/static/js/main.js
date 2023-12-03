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




  const quiz = document.querySelector('.js-quiz-page');
  if (quiz) {
    const first = quiz.querySelector('.js-first-quiz');
    const finish = quiz.querySelector('.js-finish-quiz');
    if (finish && first) {
      const start = first.querySelector('.js-quiz-start');
      const results = quiz.querySelector('.js-quiz-results');

      if (start && results) {
        const cards = Array.from(quiz.querySelectorAll('.js-quiz'));
  

        // cards.forEach(c => {
        //   const inputs = c.querySelectorAll('input[type="radio"');
        //   inputs.forEach(input => {
        //     input.onchange = e => {
        //       console.log(input.value)
        //     }
        //   })
        // });


        start.onclick = e => {
          gsap.set(first, {display: 'none'});
          gsap.fromTo(results, {display: 'none', autoAlpha: 0}, {display: 'inline-block', autoAlpha: 1, duration: .2})
          gsap.fromTo('.js-quiz', {display: 'none', autoAlpha: 0}, {display: 'flex',  autoAlpha: 1, duration: .3})
        }

        results.querySelector('button').onclick = e => {
          gsap.set(results, {PointerEvent: 'none'});
          gsap.to(results, {autoAlpha: 0, display: 'none'});
          window.scrollTo(0, 0)
          const count = quiz.querySelector('.js-count-answers');
          let amount = 0;
          cards.forEach(c => {
            const form = c.querySelector('.js-quiz-form');
            if (!form.elements["answer"].value) {
              c.setAttribute('aria-label', 'empty')
            } else if ( form.elements["answer"].value == form.querySelector('input[type="radio"].r').value) {
              amount += 1;
              c.setAttribute('aria-label', 'ok')
            } else {
              c.setAttribute('aria-label', 'err')
            }
          });
          
          
          count.textContent = `${amount}`;
          gsap.fromTo(finish, {display: 'none', autoAlpha: 0}, {display: 'inline-block', autoAlpha: 1, duration: .2})
        }

      }

    }
  }
});