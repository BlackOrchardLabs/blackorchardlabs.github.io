# SSL Certificate Fix for blackorchardlabs.com

## Problem
GitHub Pages isn't automatically provisioning an SSL certificate for the custom domain `blackorchardlabs.com`, resulting in HTTPS errors or warnings.

## Solution
Re-trigger GitHub's SSL certificate generation by removing and re-adding the custom domain.

---

## Step-by-Step Instructions

### 1. Navigate to GitHub Pages Settings
1. Go to https://github.com/BlackOrchardLabs/blackorchardlabs.github.io
2. Click **"Settings"** tab (top right of repository page)
3. In the left sidebar, click **"Pages"**

### 2. Remove Custom Domain
1. Under **"Custom domain"** section, you'll see `blackorchardlabs.com` in the text field
2. **Delete the text** so the field is empty
3. Click **"Save"** button
4. **Wait 30 seconds** (this allows GitHub to fully process the removal)

### 3. Re-add Custom Domain
1. In the now-empty **"Custom domain"** field, type: `blackorchardlabs.com`
2. Click **"Save"** button
3. You'll see a message: "DNS check in progress..."

### 4. Wait for SSL Certificate Provisioning
1. **Wait 5-10 minutes** for GitHub to:
   - Verify DNS records
   - Request SSL certificate from Let's Encrypt
   - Provision certificate to GitHub's CDN

2. **Refresh the page** periodically to check status

3. You'll know it's ready when you see:
   - ✅ "DNS check successful"
   - The **"Enforce HTTPS"** checkbox becomes available

### 5. Enable HTTPS Enforcement
1. Once the SSL certificate is provisioned, **check the box** next to:
   - ☑️ **"Enforce HTTPS"**
2. Click **"Save"** (if needed)

---

## Verification

After completing these steps, verify your site is working:

1. **Visit your site:**
   - https://blackorchardlabs.com
   - https://www.blackorchardlabs.com

2. **Check for:**
   - ✅ Green padlock icon in browser address bar
   - ✅ No certificate warnings
   - ✅ Site loads correctly

3. **Test SSL certificate:**
   - Go to: https://www.ssllabs.com/ssltest/
   - Enter: `blackorchardlabs.com`
   - Should receive **A** or **A+** rating

---

## Troubleshooting

### "DNS check failed" message
**Cause:** DNS records aren't configured correctly in Cloudflare

**Solution:**
1. Go to Cloudflare → DNS → Records
2. Verify you have all 4 A records pointing to GitHub IPs:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
3. Verify CNAME record for `www` points to `blackorchardlabs.github.io`
4. Make sure proxy status is **"DNS only"** (gray cloud)
5. Wait 15-30 minutes for DNS propagation

### "Enforce HTTPS" stays grayed out
**Cause:** SSL certificate provisioning is still in progress

**Solution:**
- Wait longer (can take up to 24 hours in rare cases)
- Make sure DNS is fully propagated (check with dnschecker.org)
- Try removing and re-adding the domain again

### Certificate shows wrong domain
**Cause:** Browser is caching old certificate

**Solution:**
- Hard refresh: `Ctrl + F5` (Windows) or `Cmd + Shift + R` (Mac)
- Clear browser cache
- Try in incognito/private mode

### "Too many certificates" error
**Cause:** Let's Encrypt rate limit (5 certificates per 7 days)

**Solution:**
- Wait 7 days before trying again
- Don't repeatedly remove/re-add the domain

---

## Timeline

| Step | Duration |
|------|----------|
| Remove domain | Instant |
| Wait | 30 seconds |
| Re-add domain | Instant |
| DNS verification | 1-5 minutes |
| SSL certificate request | 5-10 minutes |
| Certificate propagation | 5-10 minutes |
| **Total** | **10-25 minutes** (typically) |

---

## What's Happening Behind the Scenes

When you re-add the custom domain, GitHub:

1. **Verifies DNS** - Checks that your domain points to GitHub IPs
2. **Requests certificate** - Sends request to Let's Encrypt with domain validation
3. **Provisions certificate** - Installs certificate on GitHub's CDN servers
4. **Enables HTTPS** - Makes the "Enforce HTTPS" option available

---

## Prevention

To avoid this issue in future:

1. **Set up DNS first** before adding custom domain in GitHub Pages
2. **Use "DNS only" mode** in Cloudflare during initial setup
3. **Wait for DNS propagation** (24-48 hours) before adding custom domain
4. **Don't remove custom domain** once SSL is working (GitHub will auto-renew)

---

## Additional Resources

- **GitHub Pages Docs:** https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
- **SSL Certificate Troubleshooting:** https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages
- **Cloudflare DNS Guide:** See `CLOUDFLARE_DNS.md` in this repo

---

## Status Checklist

Use this to track your progress:

- [ ] Navigated to GitHub.com → Settings → Pages
- [ ] Removed `blackorchardlabs.com` from Custom domain field
- [ ] Clicked Save
- [ ] Waited 30 seconds
- [ ] Re-added `blackorchardlabs.com` to Custom domain field
- [ ] Clicked Save
- [ ] Waited 5-10 minutes
- [ ] Saw "DNS check successful" message
- [ ] "Enforce HTTPS" checkbox became available
- [ ] Checked "Enforce HTTPS"
- [ ] Verified site loads with HTTPS
- [ ] Verified green padlock appears in browser

---

**Last Updated:** 2025-01-18
**Expected Resolution Time:** 10-25 minutes
**Success Rate:** ~95% (if DNS is configured correctly)
