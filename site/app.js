/* Heartbox site — palette swatches, ports, poppy field */
const COLORS = [
  { name: "background", hex: "#090909" },
  { name: "current_line", hex: "#1C1617" },
  { name: "selection", hex: "#56180A" },
  { name: "foreground", hex: "#EDE6DE" },
  { name: "comment", hex: "#8A7874" },
  { name: "sky", hex: "#2A7EB0" },
  { name: "green", hex: "#5A7A42" },
  { name: "orange", hex: "#C45A20" },
  { name: "pink", hex: "#C47A72" },
  { name: "purple", hex: "#454B93" },
  { name: "red", hex: "#B82E18" },
  { name: "yellow", hex: "#C49A3C" },
  { name: "silver", hex: "#B8BEC2" },
];

const PORTS = [
  "alacritty", "kitty", "wezterm", "ghostty", "foot", "windows-terminal",
  "iterm", "xresources", "tmux", "warp", "hyper", "vim", "neovim", "helix",
  "emacs", "sublime", "vscode", "zed", "jetbrains", "nano", "kakoune",
  "bat", "fzf", "rofi", "dunst", "slack", "starship", "btop", "lsd",
  "delta", "lazygit", "gitui", "yazi", "k9s", "waybar", "hyprland", "noctalia",
  "i3", "polybar", "zellij", "fish", "zsh-syntax", "obsidian", "base16", "cava",
  "css", "json", "yaml", "toml",
];

function renderSwatches() {
  const root = document.getElementById("swatches");
  if (!root) return;
  root.innerHTML = COLORS.map((c) => {
    const fg = luminance(c.hex) > 0.45 ? "#090909" : "#EDE6DE";
    return `<article class="swatch" title="${c.name}">
      <div class="chip" style="background:${c.hex};color:${fg}"></div>
      <div class="meta"><span class="name">${c.name}</span><span class="hex">${c.hex}</span></div>
    </article>`;
  }).join("");
}

function luminance(hex) {
  const n = hex.replace("#", "");
  const r = parseInt(n.slice(0, 2), 16) / 255;
  const g = parseInt(n.slice(2, 4), 16) / 255;
  const b = parseInt(n.slice(4, 6), 16) / 255;
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

function renderPorts() {
  const grid = document.getElementById("ports-grid");
  const count = document.getElementById("port-count");
  if (count) count.textContent = `${PORTS.length} apps`;
  if (!grid) return;
  grid.innerHTML = PORTS.map(
    (p) =>
      `<a class="port" href="https://github.com/f00-sh/heartbox/tree/main/themes/${p}">${p}</a>`
  ).join("");
}

function poppyField() {
  const canvas = document.getElementById("poppies");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  let w, h, dpr;
  const flowers = [];

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    seed();
  }

  function seed() {
    flowers.length = 0;
    const n = Math.floor((w * h) / 14000);
    for (let i = 0; i < n; i++) {
      flowers.push({
        x: Math.random() * w,
        y: h * 0.35 + Math.random() * h * 0.7,
        r: 2 + Math.random() * 5,
        a: 0.15 + Math.random() * 0.45,
        phase: Math.random() * Math.PI * 2,
        kind: Math.random() < 0.08 ? "silver" : Math.random() < 0.12 ? "sky" : "red",
      });
    }
  }

  let t = 0;
  function frame() {
    t += 0.008;
    ctx.clearRect(0, 0, w, h);

    // ground wash
    const g = ctx.createLinearGradient(0, h * 0.3, 0, h);
    g.addColorStop(0, "rgba(26,18,20,0)");
    g.addColorStop(0.4, "rgba(44,31,34,0.35)");
    g.addColorStop(1, "rgba(58,36,40,0.55)");
    ctx.fillStyle = g;
    ctx.fillRect(0, h * 0.3, w, h * 0.7);

    for (const f of flowers) {
      const sway = Math.sin(t + f.phase) * 2;
      const x = f.x + sway;
      const y = f.y + Math.cos(t * 0.7 + f.phase) * 1.2;
      // stem
      ctx.strokeStyle = `rgba(95,191,74,${f.a * 0.5})`;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x - sway * 0.3, y + f.r * 4);
      ctx.stroke();
      // bloom
      if (f.kind === "silver") ctx.fillStyle = `rgba(184,192,200,${f.a})`;
      else if (f.kind === "sky") ctx.fillStyle = `rgba(94,200,232,${f.a * 0.7})`;
      else ctx.fillStyle = `rgba(224,32,48,${f.a})`;
      ctx.beginPath();
      ctx.arc(x, y, f.r, 0, Math.PI * 2);
      ctx.fill();
    }
    requestAnimationFrame(frame);
  }

  window.addEventListener("resize", resize);
  resize();
  frame();
}

renderSwatches();
renderPorts();
poppyField();
