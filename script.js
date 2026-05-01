(function(){
  // Header scroll effect
  const header=document.querySelector('.site-header');
  const nav=document.querySelector('.main-nav');
  function onScroll(){
    if(window.scrollY>50){
      header.classList.add('scrolled');
      nav.classList.add('scrolled');
    }else{
      header.classList.remove('scrolled');
      nav.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll',onScroll,{passive:true});
  onScroll();

  // Mobile menu
  const toggle=document.querySelector('.nav-toggle');
  const navList=document.querySelector('.nav-list');
  if(toggle && navList){
    toggle.addEventListener('click',function(){
      navList.classList.toggle('active');
    });
  }

  // Mobile dropdown toggles
  document.querySelectorAll('.has-dropdown > a').forEach(function(a){
    a.addEventListener('click',function(e){
      if(window.innerWidth<=900){
        var li=this.parentElement;
        var dd=li.querySelector('.dropdown');
        if(dd && !li.classList.contains('open')){
          e.preventDefault();
          document.querySelectorAll('.nav-list li.open').forEach(function(o){if(o!==li)o.classList.remove('open');});
          li.classList.toggle('open');
        }
      }
    });
  });

  // Intersection Observer for section animations
  const observer=new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('section-visible');
      }
    });
  },{threshold:0.1});

  document.querySelectorAll('.content-card > div > section').forEach(function(sec){
    observer.observe(sec);
  });
})();
