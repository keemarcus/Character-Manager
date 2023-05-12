drop table if exists preparedSpells;
drop table if exists spellSlots;
drop table if exists spellbooks;
drop table if exists chars;
drop table if exists users;

create table users(
	user_id bigserial primary key
);

create table chars(
	character_id bigserial primary key,
	character_name varchar not null,
	user_id int not null,
	str_score int not null,
	dex_score int not null,
	con_score int not null,
	int_score int not null,
	wis_score int not null,
	cha_score int not null,
	foreign key (user_id)
		references users (user_id)
		on delete cascade
		on update cascade
);

create table spellBooks(
	spellbook_id bigserial primary key,
	user_id int not null,
	character_id int not null,
	spell_casting_class varchar not null,
	class_level int not null,
	foreign key (user_id)
		references users (user_id)
		on delete cascade
		on update cascade,
	foreign key (character_id)
		references chars (character_id)
		on delete cascade
		on update cascade
);

create table spellSlots(
	spell_slot_id bigserial primary key,
	spellbook_id int not null,
	spell_level int not null,
	slots_total int not null,
	slots_available int not null,
	foreign key (spellbook_id)
		references spellBooks (spellbook_id)
		on delete cascade
		on update cascade
);

create table preparedSpells(
	prepared_spell_id bigserial primary key,
	spellbook_id int not null,
	spell_index varchar not null,
	spell_level int not null,
	foreign key (spellbook_id)
		references spellBooks (spellbook_id)
		on delete cascade
		on update cascade
);

insert into users values
	(default),
	(default);

insert into chars values
	(default, 'CharacterName', 1, 10, 10, 10, 10, 10, 10),
	(default, 'Roland', 1, 10, 10, 10, 10, 10, 10),
	(default, 'Tony', 2, 10, 10, 10, 10, 10, 10);

insert into spellBooks values
	(default, 1, 1, 'wizard', 10),
	(default, 1, 2, 'paladin', 5),
	(default, 2, 3, 'druid', 12);

insert into spellSlots values
	(default, 1, 1, 4, 4),
	(default, 1, 2, 3, 3),
	(default, 1, 3, 3, 3),
	(default, 1, 4, 3, 3),
	(default, 1, 5, 2, 2);
	
insert into preparedSpells values
	(default, 1, 'acid-splash', 0),
	(default, 1, 'mage-hand', 0),
	(default, 1, 'chill-touch', 0);