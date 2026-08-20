# www.isedrepresentative.com

Static site. `python3 build.py` renders `content/**/*.md` into `dist/` with schema, sitemap, robots, llms.txt, RSS, redirects and headers. Netlify runs the build on every push (see `netlify.toml`).

## Publish (first time)

```
git remote add origin https://github.com/kobysmutylo/isedrepresentative-site.git
git push -u origin main
```

Then in Netlify: Add new site → Import from Git → pick the repo. Build command and publish dir are read from `netlify.toml`. Set the custom domain to `www.isedrepresentative.com` and make it primary (apex redirects to www). Enable Forms (Site configuration → Forms) and add a notification email to info@isedrepresentative.com for the `order`, `revision` and `contact` forms.

Optional environment variables in Netlify: `GA4_ID` (G-XXXXXXX) to enable analytics; `INDEXNOW_KEY` to publish the IndexNow key file.

## Add or edit a page

Create or edit a Markdown file under `content/`. Front matter keys: `title`, `description`, `h1`, `short` (breadcrumb label), `type` (page | guide | industry | country | faq | howto | service | pricing), `date`, `updated`, `order`, `noindex`. Wrap Q&A blocks in `<!--faq--> ... <!--/faq-->` using `### Question` headings to get FAQPage schema. Commit and push; Netlify rebuilds.

## After launch

Submit `https://www.isedrepresentative.com/sitemap.xml` in Google Search Console (domain property `sc-domain:isedrepresentative.com`) and Bing Webmaster Tools; request indexing on the homepage, /pricing/, /faq/ and the first four guides.
