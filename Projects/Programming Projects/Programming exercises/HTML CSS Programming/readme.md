# Documentation of Learning **HTML & CSS**

---

## What are **HTML** and **CSS**?

- **HTML (HyperText Markup Language)** is the standard markup language used to create the structure and content of web pages (headings, paragraphs, images, links, lists, forms, etc.).
    
- **CSS (Cascading Style Sheets)** is the language used to describe the presentation of HTML — layout, colors, fonts, spacing, responsive behavior, and visual polish.
    

### Key Ideas

- **Separation of concerns**: HTML = structure/content; CSS = presentation/style.
    
- **Declarative**: you declare _what_ the page contains (HTML) and _how_ it should look (CSS).
    
- **Responsive**: CSS enables pages to adapt to different screen sizes (mobile, tablet, desktop).
    

### What they are used for

- Building websites & web apps (static pages, marketing sites, documentation)
    
- UI for web applications (when combined with JavaScript)
    
- Email templates (HTML + inline CSS)
    
- Prototyping and design systems
    
- Static sites and static site generators (Jekyll, Hugo, Eleventy)
    

### Why they matter

- Every web page uses HTML & CSS — they are fundamental skills for front-end development.
    
- Learning them gives you the foundation to move on to JavaScript, frameworks, and full-stack development.
    

---

## Useful links

- HTML Living Standard / documentation: [https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    
- CSS docs & guides: [https://developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    

---

## How to run & preview locally

### 1) Open directly in browser

Double-click `index.html` or open via your browser's **File → Open**.  
Good for quick checks, but some features (fetch/Ajax, modules) require a server.

### 2) Run a simple static HTTP server with Python (recommended)

From the project folder (where `index.html` lives), run:

- Python 3:
    

`python -m http.server 8000`

- Then open in your browser:
    

`http://localhost:8000`

Notes:

- Default port is 8000; you may pick any available port (e.g., `python -m http.server 3000`).
    
- To stop the server, press `Ctrl+C` in the terminal.
    

### 3) Other useful local servers / dev tools

- **Live Server (VS Code extension)** — serves files and reloads the page on save.
    
- **http-server** (Node.js): `npm i -g http-server` → `http-server`
    
- Static site generators (Jekyll, Hugo, Eleventy) for more advanced projects.
    

---

## Useful HTML & CSS tips

- Use semantic HTML (`<header>`, `<main>`, `<article>`, `<section>`, `<nav>`, `<footer>`) for accessibility and SEO.
    
- Keep CSS modular: use classes and avoid over-specific selectors.
    
- Responsive basics: `meta viewport` in HTML and CSS techniques (flexbox, grid, media queries).
    
- Developer tools: use your browser DevTools (Elements, Console, Network, Performance) to inspect and debug.
    
- Prefer external CSS files for maintainability; inline styles are ok for one-off tests.
    

### Quick responsive example (CSS media query)

`.container { display: grid; grid-template-columns: 1fr 320px; gap:1rem; } @media (max-width: 700px) {   .container { grid-template-columns: 1fr; } }`

---

## Deployment (quick options)

- **GitHub Pages** — free for personal projects (push repo, enable Pages).
    
- **Netlify / Vercel** — easy drag-and-drop deploy or connect Git repo; free tier available.
    
- **S3 + CloudFront** — static hosting on AWS for production-grade sites.
    

---

## Next steps & learning path

1. Learn semantic HTML elements and forms.
    
2. Master CSS layout: Flexbox and Grid.
    
3. Learn responsive design and accessibility basics (ARIA, alt text, keyboard nav).
    
4. Learn basic JavaScript for interactivity.
    
5. Explore frameworks/libraries (Tailwind, Bootstrap) and front-end frameworks (React/Vue/Svelte) when ready.
    

---

## Example commands recap

- Start Python static server:
    

`python -m http.server 8000 # visit http://localhost:8000`

- Create virtual project folder (example):
    

`mkdir my-site && cd my-site # create index.html and styles.css, then: python -m http.server`

---

##### Back to [README](../../../../README.md) Mainpage