use alligator;
select * from
(
select article.id, article.link, article.title as article, channel.title as channel, category.title as category, row_number() over (partition by category.title) as r from article
inner join channel on article.source_channel_id=channel.id
inner join channel_categories on channel_categories.channel_id=channel.id
inner join category on channel_categories.category_id=category.id
inner join user_categories on user_categories.category_id=category.id
inner join user on user_categories.user_id=user.id
where category.id in (select category.id from category inner join user_categories on user_categories.category_id=category.id where user_categories.user_id=1 order by category.title desc)
#where category.id=19
group by article.id
order by article.id desc, category.title desc
) as main
where main.r < 5
