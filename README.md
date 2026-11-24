# Gypsos Loutraki — handyman24.com

Static two-language site (Greek at `/`, English at `/en/`) for drywall installation in Loutraki and Corinthia.
Built with the same pattern as the other sites: a Python generator writes plain HTML to `site/`, served by a Cloudflare Worker with static assets.

## Build

```
pip install pillow
python3 src/build.py      # writes site/, checks links and image captions
```

- Texts: `src/pages_el.py`, `src/pages_en.py` (same page keys in both).
- Business details (phone, email, address, name): `CONFIG` block at the top of `src/build.py`.
- Illustrations (own SVGs): `tools/make_ill.py` -> `src/ill/`.
- Photos: `src/photos/*.jpg`, resized to jpg/webp by the build.

## Deploy (Cloudflare)

```
npx wrangler deploy
```

`worker.js` handles `POST /api/lead` and emails the form through the `send_email` binding `LEAD`
(Email Routing must be enabled for the domain and the destination address verified).
Set `REDIRECT` to `"on"` in `wrangler.jsonc` once handyman24.com is attached, so www/workers.dev redirect to the main host.

## To confirm before launch

- Leads: in Cloudflare, enable Email Routing on handyman24.com, verify the owner's inbox as a destination,
  forward info@handyman24.com to it, and set the Worker variable `LEAD_TO` to that inbox. The address is kept out of the code.
- Street address and the company's legal name.
- Replace stock photos with the crew's own work when available.

## Photo credits

All photos are from Unsplash under the Unsplash License (free for commercial use, no attribution required).
The site says so on the privacy page. File -> Unsplash photo ID (`https://unsplash.com/photos/<id>`, image `images.unsplash.com/photo-<id>`):

| File | Unsplash ID |
|---|---|
| tavani-me-tainies-stoko | 1733431772808-82d878e59000 |
| skeletos-chorismaton-diadromos | 1768321914149-5a6428ec2f82 |
| orthostates-chorismatos | 1768321916886-30dc323bddf7 |
| saloni-kryfos-fotismos | 1662454420647-3d20ddcdb8f8 |
| diadromos-kryfos-fotismos | 1643913592529-9989c485507a |
| kogches-rafia-saloni | 1697457643599-77b5d074121f |
| kogchi-ntous | 1780544241838-7b54189f01b0 |
| diadromos-xenodocheiou | 1631049780150-c197bf723954 |
| stokarisma-armon | 1768839725085-829e6ac7ac26 |
| ependysi-toichou-provoleas | 1751486403890-793880b12adb |
| ergotaxio-gypsosanides | 1733431774078-692252a6605e |
| orofi-gypsosanida-ktirio | 1718816281207-3b253cff549a |
