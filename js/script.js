// Omax Dental — shared interactions. Minimal, dependency-free.
(function(){
  "use strict";

  /* Mobile nav */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.querySelector(".primary-nav");
  if(toggle && nav){
    toggle.addEventListener("click", function(){
      var isOpen = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      document.body.style.overflow = isOpen ? "hidden" : "";
    });
    nav.querySelectorAll("a").forEach(function(a){
      a.addEventListener("click", function(){
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded","false");
        document.body.style.overflow = "";
      });
    });
  }

      document.addEventListener("click", function(e){
      var clickedInsideNav = nav.contains(e.target);
      var clickedToggle = toggle.contains(e.target);
      if(nav.classList.contains("open") && !clickedInsideNav && !clickedToggle){
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded","false");
        document.body.style.overflow = "";
      }
    });
    
  /* Scroll reveal */
  var revealEls = document.querySelectorAll(".reveal");
  if("IntersectionObserver" in window && revealEls.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold:.14, rootMargin:"0px 0px -60px 0px" });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add("in"); });
  }

  /* Button ripple */
  document.querySelectorAll(".btn").forEach(function(btn){
    btn.addEventListener("click", function(e){
      var rect = btn.getBoundingClientRect();
      var span = document.createElement("span");
      var size = Math.max(rect.width, rect.height);
      span.className = "ripple";
      span.style.width = span.style.height = size + "px";
      span.style.left = (e.clientX - rect.left - size/2) + "px";
      span.style.top = (e.clientY - rect.top - size/2) + "px";
      btn.appendChild(span);
      setTimeout(function(){ span.remove(); }, 650);
    });
  });

  /* FAQ accordion */
  document.querySelectorAll(".faq-item").forEach(function(item){
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    if(!q || !a) return;
    q.addEventListener("click", function(){
      var isOpen = item.classList.contains("open");
      item.closest(".faq-list").querySelectorAll(".faq-item.open").forEach(function(o){
        if(o !== item){
          o.classList.remove("open");
          o.querySelector(".faq-a").style.maxHeight = null;
          o.querySelector(".faq-q").setAttribute("aria-expanded","false");
        }
      });
      if(isOpen){
        item.classList.remove("open");
        a.style.maxHeight = null;
        q.setAttribute("aria-expanded","false");
      } else {
        item.classList.add("open");
        a.style.maxHeight = a.scrollHeight + "px";
        q.setAttribute("aria-expanded","true");
      }
    });
  });

  /* Gallery filter */
  var filters = document.querySelectorAll(".gfilter");
  var figures = document.querySelectorAll(".masonry figure");
  if(filters.length){
    filters.forEach(function(btn){
      btn.addEventListener("click", function(){
        filters.forEach(function(b){ b.classList.remove("active"); b.setAttribute("aria-pressed","false"); });
        btn.classList.add("active");
        btn.setAttribute("aria-pressed","true");
        var group = btn.getAttribute("data-filter");
        figures.forEach(function(fig){
          var show = group === "all" || fig.getAttribute("data-group") === group;
          fig.style.display = show ? "" : "none";
        });
      });
    });
  }

  /* Lightbox */
  var lightbox = document.querySelector(".lightbox");
  if(lightbox){
    var lbImg = lightbox.querySelector("img");
    var closeBtn = lightbox.querySelector(".lightbox-close");
    document.querySelectorAll(".masonry figure img").forEach(function(img){
      img.addEventListener("click", function(){
        lbImg.src = img.src;
        lbImg.alt = img.alt;
        lightbox.classList.add("open");
      });
    });
    function closeLb(){ lightbox.classList.remove("open"); lbImg.src=""; }
    closeBtn && closeBtn.addEventListener("click", closeLb);
    lightbox.addEventListener("click", function(e){ if(e.target === lightbox) closeLb(); });
    document.addEventListener("keydown", function(e){ if(e.key === "Escape") closeLb(); });
  }

  /* Sticky header shadow on scroll */
  var header = document.querySelector(".site-header");
  if(header){
    window.addEventListener("scroll", function(){
      header.style.boxShadow = window.scrollY > 8 ? "0 8px 24px -18px rgba(34,33,33,.4)" : "none";
    }, { passive:true });
  }
})();
