drop table if exists preparedSpells;
drop table if exists spellbooks;

create table spellBooks(
	spellbook_id bigserial primary key,
	spell_casting_class varchar not null,
	class_level int not null
);

create table preparedSpells(
	prepared_spell_id bigserial primary key,
	spellbook_id int not null,
	spell_index varchar not null,
	foreign key (spellbook_id)
		references spellBooks (spellbook_id)
		on delete cascade
		on update cascade
);

insert into spellBooks
	values(1, 'Wizard', 10),
	(2, 'Paladin', 5),
	(3, 'Druid', 12);
	

insert into preparedSpells
	values(1, 1, 'acid-splash'),
	(2, 1, 'mage-hand'),
	(3, 1, 'chill-touch');