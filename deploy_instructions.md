# GitHub Deployment Instructions

## 1. Create GitHub Repository
```bash
# Go to github.com and create new repository named "metamman-transliterator"
# Don't initialize with README (we already have files)
```

## 2. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/metamman-transliterator.git
git branch -M main
git push -u origin main
```

## 3. Enable GitHub Pages
1. Go to repository Settings
2. Scroll to "Pages" section
3. Source: Deploy from a branch
4. Branch: main
5. Folder: /docs
6. Save

## 4. Access Your Live Site
- URL: https://YOUR_USERNAME.github.io/metamman-transliterator/
- Updates automatically on push to main branch

## 5. Alternative Deployments

### Heroku
```bash
heroku create your-app-name
git push heroku main
```

### Vercel
```bash
npm i -g vercel
vercel --prod
```

## Repository Structure
```
metamman-transliterator/
├── docs/                 # GitHub Pages static site
├── compiler/            # Indic language compiler
├── examples/            # Sample code files
├── static/              # Web assets
├── templates/           # Flask templates
└── main.py             # CLI interface
```