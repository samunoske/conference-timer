# Conference Session Timer

A self-contained web app for running conference sessions: build a run of talks and breaks, then let a single countdown advance through every segment automatically.

No build step, no dependencies — open `index.html` in a browser (or deploy it) and you're ready.

## Features

- **Sequenced schedule** — list talks and breaks once; the timer advances to the next segment automatically when the current one ends
- **Phase warnings** — the page and countdown shift green → yellow → orange → red as a talk runs low, with a **WRAP IT UP!!!** full-screen blink at the end
- **On-schedule anchoring** — when a talk runs over, the following break still starts on schedule, so the whole day stays on time
- **Live editing** — edit upcoming lines in the textarea and hit **Update** without disturbing past segments
- **Drag-and-drop reordering** — reorder upcoming segments in the queue preview (past and in-progress ones stay locked)
- **Quick add & presets** — one-click talks/breaks and prebuilt schedules
- **Keyboard shortcuts** — start/pause, skip, reset, fullscreen, sound, dismiss overlay
- **Persistence** — the schedule is saved in `localStorage` and restored on reload
- **Responsive** — stacked panels on narrow screens, a no-scroll two-column layout on wide screens

## Getting started

### Local

Open `index.html` in any modern browser. That's it.

### GitHub Pages

The repo is Pages-ready: push to GitHub, enable Pages on the repo root (Settings → Pages → Deploy from a branch → `main` / root), and the app is served at `https://<your-username>.github.io/<repo>/`.

Or use the included [GitHub Actions workflow](.github/workflows/pages.yml) to deploy on every push.

## Usage

### Writing a schedule

Each line in the schedule editor is one segment:

```
talk, 25, Opening talk
break, 5, Short buffer
talk, 50, Featured session
break, 60, Lunch break
```

- `talk` or `break` first
- then a number of minutes
- then the title (anything after the second comma)

### Keyboard shortcuts

| Key | Action |
| --- | --- |
| `Space` | Start / pause |
| `N` | Next segment |
| `R` | Reset current segment |
| `F` | Fullscreen |
| `O` | Dismiss the WRAP IT UP overlay |
| `M` | Toggle sound |

## Project structure

```
index.html   App markup
styles.css   All styling
app.js       All logic
archive/     Historical single-file versions (v10–v18)
```

## License

[MIT](LICENSE)
