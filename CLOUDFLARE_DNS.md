# Cloudflare DNS Quick Reference

## DNS Records for blackorchardlabs.com → GitHub Pages

Copy these exact settings into Cloudflare DNS:

### A Records (Apex Domain)

```
Type: A
Name: @
Content: 185.199.108.153
Proxy: DNS only (gray cloud)
TTL: Auto
```

```
Type: A
Name: @
Content: 185.199.109.153
Proxy: DNS only (gray cloud)
TTL: Auto
```

```
Type: A
Name: @
Content: 185.199.110.153
Proxy: DNS only (gray cloud)
TTL: Auto
```

```
Type: A
Name: @
Content: 185.199.111.153
Proxy: DNS only (gray cloud)
TTL: Auto
```

### CNAME Record (www subdomain)

```
Type: CNAME
Name: www
Content: blackorchardlabs.github.io
Proxy: DNS only (gray cloud)
TTL: Auto
```

## ⚠️ Important

1. **Set proxy to "DNS only"** (gray cloud) initially
2. Wait 24 hours for GitHub to issue SSL certificate
3. After HTTPS works, you can enable proxy (orange cloud) if desired

## SSL/TLS Settings

In Cloudflare → SSL/TLS:

- **Encryption mode:** Full or Full (strict)
- **Always Use HTTPS:** ON
- **Automatic HTTPS Rewrites:** ON
- **Minimum TLS Version:** 1.2

## Verification

Check DNS propagation:
- https://dnschecker.org
- Enter: `blackorchardlabs.com`
- Should show: `185.199.108.153` (and other GitHub IPs)

Check HTTPS:
- https://www.ssllabs.com/ssltest/
- Enter: `blackorchardlabs.com`
- Should get A or A+ rating (after 24 hours)

## Timeline

- DNS propagation: 15 minutes - 48 hours
- SSL certificate issuance: Up to 24 hours
- Full HTTPS: 24-48 hours after DNS propagates

---

**Note:** These are GitHub Pages official IPs. They rarely change, but verify at:
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
