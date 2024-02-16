set schema 'shopify';

begin transaction;

-- 2 delete statements: delete from
delete from reviews where app_id = '7a282c82-620e-4b4b-955a-e91a2fbb0d9e' and author = '261 Boutique';

delete from reviews where app_id = '7a282c82-620e-4b4b-955a-e91a2fbb0d9e' and author = '4 Paws Pet Stuff';

delete from reviews where app_id = '7a282c82-620e-4b4b-955a-e91a2fbb0d9e' and author = 'A2Depot';
commit;