set schema 'shopify';

begin transaction;

-- 2 update statements: update

update key_benefits set description = 'Enhanced Shopping Experience Popups' where app_id = '00289a9f-9f12-45b1-963b-67e78403f7c7' and title = 'Add more products to cart';

update key_benefits set description = 'Increase subscribers with personalized pop-ups that prompt visitors to join newsletters and promotions.' where app_id = '562a0052-f1de-4919-896f-546e453f33cd' and title = 'Subscribe pop-ups';

commit;