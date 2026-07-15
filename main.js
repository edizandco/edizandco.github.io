// Ediz & Co. — Core Interactions & Animations
window.addEventListener('DOMContentLoaded', () => {
  // 1. Dynamic Navigation Highlighting
  const path = window.location.pathname;
  const normPath = path.replace(/\/index\.html$/, '/').replace(/\/$/, '');
  
  document.querySelectorAll('.nav-mid a, .mobile-menu-links a').forEach(link => {
    const linkPath = link.getAttribute('href');
    if (linkPath) {
      const normLinkPath = linkPath.replace(/\/index\.html$/, '/').replace(/\/$/, '');
      const isMatch = (normPath === normLinkPath) || 
                      (normPath === '' && normLinkPath === '/') || 
                      (normPath === '/en' && normLinkPath === '/en/');
      
      if (isMatch) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    }
  });

  // 2. GSAP Navigation Entrance (only if not on home page, home page runs its own animation)
  const isHomePage = normPath === '' || normPath === '/' || normPath === '/en';
  if (!isHomePage && typeof gsap !== 'undefined') {
    gsap.to('#main-nav', { y: 0, duration: 0.4, ease: 'power3.out' });
  }

  // 3. Theme Toggle Handler
  const toggleBtn = document.getElementById('theme-toggle');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      // Dispatch custom event for WebGL canvas reaction
      window.dispatchEvent(new CustomEvent('themechanged', { detail: { theme: newTheme } }));
    });
  }

  // 4. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const mobileOverlay = document.getElementById('mobile-menu-overlay');
  
  if (mobileToggle && mobileOverlay) {
    mobileToggle.addEventListener('click', () => {
      mobileToggle.classList.toggle('active');
      mobileOverlay.classList.toggle('active');
    });
    
    mobileOverlay.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileToggle.classList.remove('active');
        mobileOverlay.classList.remove('active');
      });
    });
  }

  // 5. FAQ Accordion Logic
  document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
      const item = button.parentElement;
      item.classList.toggle('active');
    });
  });

  // 6. Form Input Sanitization (XSS Prevention)
  const contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      const textInputs = contactForm.querySelectorAll('input[type="text"], input[type="email"], textarea');
      textInputs.forEach(input => {
        // Strip potential script injections and HTML tags
        input.value = input.value.replace(/<[^>]*>/g, '').trim();
      });
    });
  }
});
