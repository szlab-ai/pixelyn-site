# Pixelyn website

Bilingual product, support and privacy pages for Pixelyn: TV Screen Test.
Public site: https://szlab-ai.github.io/pixelyn-site/

- `/zh/`, `/en/`: product overview
- `/zh/privacy/`, `/en/privacy/`: fixed app QR destinations — do not rename
- `/zh/support/`, `/en/support/`: guide and public contacts

Static HTML/CSS, no build dependencies, JavaScript, cookies or analytics.
`python3 scripts/check.py` validates all local links and exact privacy paragraphs.
To preview from the parent directory: `python3 -m http.server 8765` then open `/pixelyn-site/`.
Push main to deploy via GitHub Actions. Pages source must be GitHub Actions.

Privacy paragraphs in `scripts/privacy-source.json` are copied verbatim from the app’s M7 `Localizable.xcstrings`. Includes five preferences, language among them. Keep both languages in sync with the app.

Screenshots are actual app interfaces captured in the tvOS Simulator, resized to 1600 × 900. They illustrate the UI, not a particular TV’s measurements. The app has not yet been released; do not add an App Store download link until an actual store listing is live.
