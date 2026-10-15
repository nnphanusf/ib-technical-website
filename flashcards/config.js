/* Supabase connection.
   From the project's Settings -> API Keys. Leave both empty to drop the page
   back to browser-only mode (profiles and progress in localStorage).

   SUPA_KEY is the PUBLISHABLE key: it is meant to ship in public page code and
   carries no more privilege than an anonymous visitor. The row level security
   policies in supabase/schema.sql are what protect the data. Never put a
   secret key (sb_secret_...) or the database password in this file. */
window.SUPA_URL = "https://luijiocpivkzszbqmulh.supabase.co";
window.SUPA_KEY = "sb_publishable_YuXqBZehemSAtTIK3X4MJA_K15a85Cj";
