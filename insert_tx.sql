set schema 'shopify';

begin transaction;

-- 2 insert statements: insert into

-- This is an insert for pricing plans with the app_id with 00289a9f-9f12-45b1-963b-67e78403f7c7
insert into pricing_plans (id, app_id, title, price) 
values ('d23cc2f0-9f12-45b1-97f1-b7a367593e15', '00289a9f-9f12-45b1-963b-67e78403f7c7', 'Free Trial', 2.99);

-- This is an insert for category, making something up
insert into categories (id, title)
values ('c3f9db73c29bc33660c59e7d44e4b0b1 ','Digital design marketing');

commit;