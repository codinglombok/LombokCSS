/* Docs switchers + state propagation via query string (no storage needed) */
(function(){
  var root = document.documentElement;
  var q = new URLSearchParams(location.search);
  var style = q.get('style') || 'modern-corporate-flat';
  var theme = q.get('theme') || 'light';
  var dir   = q.get('dir')   || 'ltr';
  apply();
  function apply(){
    root.setAttribute('data-style', style);
    root.setAttribute('data-theme', theme);
    root.setAttribute('dir', dir);
    root.setAttribute('lang', dir==='rtl'?'ar':'en');
    document.querySelectorAll('[data-style-set]').forEach(function(b){
      b.classList.toggle('is-active', b.getAttribute('data-style-set')===style);
    });
    var dk=document.getElementById('dk'); if(dk) dk.checked = theme==='dark';
    var rt=document.getElementById('rt'); if(rt) rt.checked = dir==='rtl';
    // rewrite internal nav links to carry state
    var qs='?style='+style+'&theme='+theme+'&dir='+dir;
    document.querySelectorAll('a[data-page]').forEach(function(a){
      a.setAttribute('href', a.getAttribute('data-page')+qs);
    });
  }
  document.querySelectorAll('[data-style-set]').forEach(function(b){
    b.addEventListener('click', function(){ style=b.getAttribute('data-style-set'); apply(); });
  });
  var dk=document.getElementById('dk'); if(dk) dk.addEventListener('change',function(e){ theme=e.target.checked?'dark':'light'; apply(); });
  var rt=document.getElementById('rt'); if(rt) rt.addEventListener('change',function(e){ dir=e.target.checked?'rtl':'ltr'; apply(); });
  var bg=document.querySelector('.docs-burger');
  if(bg) bg.addEventListener('click', function(){ document.querySelector('.docs').classList.toggle('nav-open'); });
})();
