# Black Orchard Labs Landing Page Setup Guide

## 📦 What You Have

Your landing page is ready at: `C:\Hermes\projects\blackorchardlabs.github.io\`

Files:
- `index.html` - Your complete landing page (CSS embedded)
- `black_orchard_logo.png` - Your logo
- `SETUP.md` - This file

## 🚀 GitHub Pages Deployment

### Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository settings:
   - **Repository name:** `blackorchardlabs.github.io`
   - **Description:** "Black Orchard Labs - Building Liberation Technology"
   - **Visibility:** Public
   - **DO NOT** initialize with README, .gitignore, or license
4. Click **"Create repository"**

### Step 2: Push Your Code to GitHub

Open your terminal/command prompt and run:

```bash
cd "C:\Hermes\projects\blackorchardlabs.github.io"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Black Orchard Labs landing page"

# Add GitHub as remote (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/blackorchardlabs.github.io.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** (top right)
3. In the left sidebar, click **"Pages"**
4. Under **"Source"**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **"Save"**
6. Wait 1-2 minutes

Your site will be live at: `https://blackorchardlabs.github.io`

## 🌐 Custom Domain Setup (blackorchardlabs.com)

### Step 4: Configure GitHub Pages for Custom Domain

1. In your repository settings → Pages
2. Under **"Custom domain"**, enter: `blackorchardlabs.com`
3. Click **"Save"**
4. **Check** the box for **"Enforce HTTPS"** (after DNS propagates)

### Step 5: Create CNAME file

In your local repository:

```bash
cd "C:\Hermes\projects\blackorchardlabs.github.io"

# Create CNAME file
echo blackorchardlabs.com > CNAME

# Commit and push
git add CNAME
git commit -m "Add CNAME for custom domain"
git push
```

## ☁️ Cloudflare DNS Configuration

### Step 6: Set Up Cloudflare DNS Records

1. Log in to [Cloudflare](https://dash.cloudflare.com)
2. Select your domain: `blackorchardlabs.com`
3. Go to **DNS** → **Records**
4. Delete any existing A or CNAME records for `@` and `www`
5. Add these DNS records:

#### For Apex Domain (@)

Add **4 A records** pointing to GitHub Pages IPs:

| Type | Name | Content | Proxy Status | TTL |
|------|------|---------|--------------|-----|
| A | @ | `185.199.108.153` | DNS only (gray cloud) | Auto |
| A | @ | `185.199.109.153` | DNS only (gray cloud) | Auto |
| A | @ | `185.199.110.153` | DNS only (gray cloud) | Auto |
| A | @ | `185.199.111.153` | DNS only (gray cloud) | Auto |

#### For www Subdomain

Add **1 CNAME record**:

| Type | Name | Content | Proxy Status | TTL |
|------|------|---------|--------------|-----|
| CNAME | www | `blackorchardlabs.github.io` | DNS only (gray cloud) | Auto |

### Step 7: Important Cloudflare Settings

**⚠️ CRITICAL:** Set proxy status to **"DNS only"** (gray cloud icon)

If you use "Proxied" (orange cloud), HTTPS verification will fail.

After DNS propagates (15 minutes - 48 hours), you can enable Cloudflare proxy.

### Step 8: SSL/TLS Configuration (Cloudflare)

1. In Cloudflare, go to **SSL/TLS** → **Overview**
2. Set encryption mode to: **"Full"** or **"Full (strict)"**
3. Go to **SSL/TLS** → **Edge Certificates**
4. Enable:
   - ✅ Always Use HTTPS
   - ✅ Automatic HTTPS Rewrites
   - ✅ Minimum TLS Version: 1.2

## ✅ Verification Steps

### Test Your Deployment

1. **GitHub Pages default URL:**
   - Visit: `https://blackorchardlabs.github.io`
   - Should show your landing page

2. **Custom domain (after DNS propagates):**
   - Visit: `https://blackorchardlabs.com`
   - Visit: `https://www.blackorchardlabs.com`
   - Both should show your landing page

3. **Check DNS propagation:**
   - Use: https://dnschecker.org
   - Enter: `blackorchardlabs.com`
   - Should show GitHub IPs globally

### Troubleshooting

**DNS not propagating?**
- Wait 24-48 hours
- Clear browser cache
- Try incognito/private mode

**HTTPS not working?**
- Make sure Cloudflare proxy is "DNS only" initially
- Wait for GitHub to issue SSL certificate (can take 24 hours)
- Check "Enforce HTTPS" is enabled in GitHub Pages settings
- **If SSL certificate won't provision:** See `SSL_FIX_GUIDE.md` for step-by-step fix (remove/re-add custom domain)

**404 error?**
- Verify CNAME file exists in your repository
- Verify custom domain is set in GitHub Pages settings
- Check that index.html is in root directory

## 🎨 Making Updates

To update your landing page:

```bash
cd "C:\Hermes\projects\blackorchardlabs.github.io"

# Edit your files (index.html, etc.)

# Commit changes
git add .
git commit -m "Update landing page"
git push

# Changes will be live in 1-2 minutes
```

## 📝 Notes

- GitHub Pages is free for public repositories
- Cloudflare DNS is free (basic plan is sufficient)
- SSL certificates are automatically provided by GitHub
- Your site will auto-deploy on every push to `main` branch

## 🆘 Need Help?

- GitHub Pages Docs: https://docs.github.com/en/pages
- Cloudflare DNS Docs: https://developers.cloudflare.com/dns/
- Custom Domain Guide: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

---

**Your landing page is ready to deploy!** 🚀
