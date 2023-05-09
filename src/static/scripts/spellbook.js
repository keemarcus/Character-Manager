const available_spell_slots = new Object()
set_up_page()

async function set_up_page() {
    // use fetch to get the id of the current spellbook
    let url = "http://localhost:5000/session/spellbook_id"
    let response = await fetch(url)
    spellbook_id = await response.text()

    if (spellbook_id === 'None') {
        console.log("No spellbook id found")
    }
    else {
        console.log(spellbook_id)
        // use fetch to get the spell stats
        let url = "http://localhost:5000/spellbooks/" + spellbook_id
        let response = await fetch(url)
        spells_stats = await response.json()

        let stats_table = document.getElementById('spell stats')
        // create new table row
        let row = stats_table.insertRow(-1)
        let character_cell = row.insertCell(0)
        let class_cell = row.insertCell(1)
        let level_cell = row.insertCell(2)

        // insert the data into the new row
        character_cell.innerText = spells_stats["_character_id"].split('-')[1]
        class_cell.innerText = spells_stats["_spell_casting_class"].charAt(0).toUpperCase() + spells_stats["_spell_casting_class"].substring(1)
        level_cell.innerText = spells_stats["_spell_casting_level"]

        // use fetch to get the spell slots
        url = "http://localhost:5000/spellbooks/slots/" + spellbook_id
        response = await fetch(url)
        spell_slots= await response.json()

        let slots_table = document.getElementById('slots table')
        for(let i = 1; i <= (Object.keys(spell_slots).length / 2); i++) {
            // create new table row
            let row = slots_table.insertRow(-1)
            let slot_level_cell = row.insertCell(0)
            let slots_available_cell = row.insertCell(1)
            let slots_total_cell = row.insertCell(2)

            // insert the data into the new row
            slot_level_cell.innerText = i
            slots_available_cell.innerText = spell_slots[i.toString() + "_available"]
            slots_total_cell.innerText = spell_slots[i.toString() + "_total"]

            available_spell_slots[i] = spell_slots[i.toString() + "_available"]
        }

        // use fetch to get the spells in the current spellbook
        url = "http://localhost:5000/spellbooks/spells/" + spellbook_id
        response = await fetch(url)
        spells = await response.text()
        const spell_list = spells.split(",")
        let table = document.getElementById('spell table')
        for (spelll in spell_list){
            // get the full spell info
            let url = "https://www.dnd5eapi.co/api/spells/" + spell_list[spelll]
            let response = await fetch(url)
            spell_info = await response.json()
            //console.log(spell_info)

            // create new table row
            let row = table.insertRow(-1)
            let name_cell = row.insertCell(0)
            let cast_cell = row.insertCell(1)
            let level_cell = row.insertCell(2)
            let components_cell = row.insertCell(3)
            let duration_cell = row.insertCell(4)
            let range_cell = row.insertCell(5)
            let desc_cell = row.insertCell(6)

            // insert the data into the new row
            name_cell.innerText = spell_info["name"]
            level_cell.innerText = spell_info["level"]
            if(spell_info["higher_level"].length > 0){
                level_cell.innerText += "+"
            }
            // set up cast buttons
            if(level_cell.innerText.includes("+")){
                for(let spell_level = spell_info["level"]; spell_level <= Object.keys(available_spell_slots).length; spell_level){
                    if(available_spell_slots[spell_level] > 0){
                        var btn = document.createElement('input')
                        btn.type = "button"
                        btn.value = "Cast at level " + spell_level 
                        btn.setAttribute('onclick', 'javascript: cast_spell(' + spellbook_id + ', "' + spells_stats['_character_id'] + '", "' + spell_list[spelll] + '", ' + spell_level + ');' );
                        cast_cell.appendChild(btn)
                    }
                    spell_level++
                }
            }else if (spell_info["level"] == 0 || available_spell_slots[spell_info["level"]] > 0){
                var btn = document.createElement('input')
                btn.type = "button"
                btn.value = "Cast"
                btn.setAttribute('onclick', 'javascript: cast_spell(' + spellbook_id + ', "' + spells_stats['_character_id'] + '", "' + spell_list[spelll] + '", ' + spell_info['level'] + ');' );
                cast_cell.appendChild(btn)
            }
            components_cell.innerText = spell_info["components"].join(", ")
            duration_cell.innerText = spell_info["duration"]
            range_cell.innerText = spell_info["range"]
            desc_cell.innerText = spell_info["desc"].join('\n')
        }
    }
}

function cast_spell(spellbook_id, character_id, spell_index, spell_level){
    const formData = new FormData();

    formData.append("spellbook_id", spellbook_id);
    formData.append("character_id", character_id);
    formData.append("spell_index", spell_index);
    formData.append("spell_level", spell_level);
    
    const request = new XMLHttpRequest();
    request.open("POST", "http://localhost:5000/spellbooks/cast");
    request.send(formData);

    location.reload()
}


