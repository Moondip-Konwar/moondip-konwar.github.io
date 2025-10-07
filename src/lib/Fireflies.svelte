<script>
  import { onMount } from 'svelte';
  onMount(() => {
    // paste your fireflies script here
    const c = document.getElementById('firefliesCanvas');
    	  const ctx = c.getContext('2d', { alpha: true });
    	  let w, h, dpr, flies = [], mouse = {x: -9999, y: -9999, down: false}, ripples = [];
    	
    	  const GREEN = getComputedStyle(document.documentElement)
    	    .getPropertyValue('--green').trim() || '#22ff7a';
    	
    	  function resize(){
    	    dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
    	    w = c.width = Math.floor(innerWidth * dpr);
    	    h = c.height = Math.floor(innerHeight * dpr);
    	    c.style.width = innerWidth + 'px';
    	    c.style.height = innerHeight + 'px';
    	  }
    	
    	  function edgeBias(){
    	    // return a random position biased towards edges
    	    const edgeFactor = 0.25; // 25% of width/height is "edge zone"
    	    let x, y;
    	    if (Math.random() < 0.5) {
    	      // bias horizontal
    	      x = Math.random() < 0.5
    	        ? Math.random() * w * edgeFactor
    	        : w - Math.random() * w * edgeFactor;
    	      y = Math.random() * h;
    	    } else {
    	      // bias vertical
    	      y = Math.random() < 0.5
    	        ? Math.random() * h * edgeFactor
    	        : h - Math.random() * h * edgeFactor;
    	      x = Math.random() * w;
    	    }
    	    return {x,y};
    	  }
    	
    	  function makeFlies(count){
    	    flies = Array.from({length: count}, () => {
    	      const pos = edgeBias();
    	      return {
    	        x: pos.x,
    	        y: pos.y,
    	        r: (Math.random() * 1.6 + 1.0) * dpr,
    	        sp: (Math.random() * 0.6 + 0.2) * dpr,
    	        a: Math.random() * Math.PI * 2,
    	        tw: Math.random() * 1500 + 800
    	      };
    	    });
    	  }
    	
    	  function step(t){
    	    ctx.clearRect(0,0,w,h);
    	
    	    // ripple effect
    	    ripples = ripples.filter(r => r.r < Math.max(w,h));
    	    for (const r of ripples){
    	      ctx.globalAlpha = r.a;
    	      ctx.strokeStyle = GREEN;
    	      ctx.lineWidth = 2 * dpr;
    	      ctx.beginPath();
    	      ctx.arc(r.x, r.y, r.r, 0, Math.PI*2);
    	      ctx.stroke();
    	      r.r += 6*dpr; 
    	      r.a *= 0.94;
    	    }
    	
    	    for(const f of flies){
    	      // mouse repulsion
    	      const dx = f.x - mouse.x*dpr, dy = f.y - mouse.y*dpr;
    	      const dist = Math.sqrt(dx*dx + dy*dy);
    	      let speedBoost = 1;
    	      if (dist < 150*dpr) {
    	        speedBoost = 3; // run away fast
    	        f.a = Math.atan2(dy, dx) + (Math.random()-0.5)*0.3;
    	      }
    	
    	      // wander
    	      f.a += (Math.random() - 0.5) * 0.2;
    	      f.x += Math.cos(f.a) * f.sp * speedBoost;
    	      f.y += Math.sin(f.a) * f.sp * speedBoost;
    	
    	      // wrap
    	      if (f.x < -20) f.x = w + 20;
    	      if (f.x > w + 20) f.x = -20;
    	      if (f.y < -20) f.y = h + 20;
    	      if (f.y > h + 20) f.y = -20;
    	
    	      // twinkle
    	      const tw = 0.5 + 0.5 * (0.5 + 0.5 * Math.sin(t / f.tw));
    	
    	      // halo
    	      ctx.globalCompositeOperation = 'lighter';
    	      ctx.globalAlpha = tw;
    	      const grad = ctx.createRadialGradient(f.x, f.y, 0, f.x, f.y, f.r*6);
    	      grad.addColorStop(0, GREEN + 'aa');
    	      grad.addColorStop(1, 'transparent');
    	      ctx.fillStyle = grad;
    	      ctx.beginPath();
    	      ctx.arc(f.x, f.y, f.r*6, 0, Math.PI*2);
    	      ctx.fill();
    	
    	      // core
    	      ctx.fillStyle = GREEN;
    	      ctx.beginPath();
    	      ctx.arc(f.x, f.y, f.r, 0, Math.PI*2);
    	      ctx.fill();
    	    }
    	    ctx.globalAlpha = 1;
    	
    	    requestAnimationFrame(step);
    	  }
    	
    	  resize();
    	  const base = Math.round((innerWidth * innerHeight) / 90000);
    	  makeFlies(Math.min(28, Math.max(12, base))); // ~12–28
    	  requestAnimationFrame(step);
    	
    	  addEventListener('resize', () => { resize(); makeFlies(flies.length); });
    	
    	  document.addEventListener('mousemove', e => {
    	    mouse.x = e.clientX;
    	    mouse.y = e.clientY;
    	  });
    	  document.addEventListener('mouseleave', () => {
    	    mouse.x = -9999;
    	    mouse.y = -9999;
    	  });
    	  document.addEventListener('click', e => {
    	    ripples.push({x: e.clientX*dpr, y: e.clientY*dpr, r: 0, a: 0.6});
    	  });
    	
    	  document.addEventListener('visibilitychange', () => {
    	    if (document.hidden) ctx.clearRect(0,0,w,h);
    	  });    	
  });
</script>

<canvas id="firefliesCanvas" aria-hidden="true"></canvas>
