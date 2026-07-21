/* Docs switchers + state propagation via query string (no storage needed) */
(function(){
  var root = document.documentElement;
  var q = new URLSearchParams(location.search);

  function sanitizeStyle(value){
    var allowed = ['modern-corporate-flat', 'modern-corporate-neumorph'];
    return allowed.indexOf(value) !== -1 ? value : 'modern-corporate-flat';
  }

  function sanitizeTheme(value){
    return value === 'dark' ? 'dark' : 'light';
  }

  function sanitizeDir(value){
    return value === 'rtl' ? 'rtl' : 'ltr';
  }

  function sanitizeDataPage(value){
    if (!value) return null;
    if (/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(value)) return null;
    if (!/^[a-zA-Z0-9._\-\/]+\.html(?:#[a-zA-Z0-9_\-]+)?$/.test(value)) return null;
    return value;
  }

  var style = sanitizeStyle(q.get('style'));
  var theme = sanitizeTheme(q.get('theme'));
  var dir   = sanitizeDir(q.get('dir'));
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
    var qs='?' + new URLSearchParams({ style: style, theme: theme, dir: dir }).toString();
    document.querySelectorAll('a[data-page]').forEach(function(a){
      var dataPage = sanitizeDataPage(a.getAttribute('data-page'));
      if (dataPage) a.setAttribute('href', dataPage + qs);
    });
  }
  document.querySelectorAll('[data-style-set]').forEach(function(b){
    b.addEventListener('click', function(){ style=sanitizeStyle(b.getAttribute('data-style-set')); apply(); });
  });
  var dk=document.getElementById('dk'); if(dk) dk.addEventListener('change',function(e){ theme=e.target.checked?'dark':'light'; apply(); });
  var rt=document.getElementById('rt'); if(rt) rt.addEventListener('change',function(e){ dir=e.target.checked?'rtl':'ltr'; apply(); });
  var bg=document.querySelector('.docs-burger');
  if(bg) bg.addEventListener('click', function(){ document.querySelector('.docs').classList.toggle('nav-open'); });
})();
