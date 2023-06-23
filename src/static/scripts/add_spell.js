var prepared_spells
set_up_page()

async function set_up_page() {
    prepared_spells = new Set()

    // use fetch to get the id of the current spellbook
    let url = "http://localhost:5000/session/spellbook_id"
    let response = await fetch(url)
    spellbook_id = await response.text()

    if (spellbook_id === 'None') {
        console.log("No spellbook id found")
    } else {
        // use fetch to get the spell stats
        let url = "http://localhost:5000/spellbooks/" + spellbook_id
        let response = await fetch(url)
        spells_stats = await response.json()

        // use fetch to get the number of spells and cantrips known
        url = "https://www.dnd5eapi.co/api/classes/" + spells_stats["_spell_casting_class"] + "/levels/" + spells_stats["_spell_casting_level"]
        response = await fetch(url)
        class_level_info = await response.json()

        let stats_table = document.getElementById('spell stats')
        // create new table row
        let row = stats_table.insertRow(-1)
        let character_cell = row.insertCell(0)
        let class_cell = row.insertCell(1)
        let level_cell = row.insertCell(2)
        let spells_known_cell = row.insertCell(3)
        let cantrips_known_cell = row.insertCell(4)

        // insert the data into the new row
        character_cell.innerText = spells_stats["_character_id"].toString().split('-')[1]
        class_cell.innerText = spells_stats["_spell_casting_class"].charAt(0).toUpperCase() + spells_stats["_spell_casting_class"].substring(1)
        level_cell.innerText = spells_stats["_spell_casting_level"]
        if (class_level_info["spellcasting"]["spells_known"]) {
            spells_known_cell.innerText = class_level_info["spellcasting"]["spells_known"]
        } else {
            // handle this later
            // set a limit to the number of spells we can add to the spellbook
        }
        if (class_level_info["spellcasting"]["cantrips_known"]) {
            cantrips_known_cell.innerText = class_level_info["spellcasting"]["cantrips_known"]
        } else {
            // handle this later
            // set a limit to the number of cantrips we can add to the spellbook
        }

        // use fetch to get the spell slots
        url = "http://localhost:5000/spellbooks/slots/" + spellbook_id
        response = await fetch(url)
        spell_slots = await response.json()

        let spell_slot_levels = new Set()

        let slot_level_row = document.getElementById('slot level row')
        let total_slots_row = document.getElementById('total slots row')
        for (let i = 1; i <= (Object.keys(spell_slots).length / 2); i++) {
            // create new table row
            let slot_level_cell = document.createElement("th")
            slot_level_row.appendChild(slot_level_cell)
            let slots_total_cell = total_slots_row.insertCell(-1)

            // insert the data into the new row
            slot_level_cell.innerText = i
            slots_total_cell.innerText = spell_slots[i.toString() + "_total"]

            spell_slot_levels.add(slot_level_cell.innerText)
        }

        // use fetch to get the spells already in the current spellbook
        url = "http://localhost:5000/spellbooks/spells/" + spellbook_id
        response = await fetch(url)
        spells = await response.text()
        const spell_list = spells.toString().split(",")
        let table = document.getElementById('current spells table')
        for (spelll in spell_list) {
            // get the full spell info
            let url = "https://www.dnd5eapi.co/api/spells/" + spell_list[spelll]
            let response = await fetch(url)
            spell_info = await response.json()
            if (!spell_info["desc"]) { break }

            // create new table row
            let row = table.insertRow(-1)
            let name_cell = row.insertCell(0)
            let level_cell = row.insertCell(1)
            let remove_cell = row.insertCell(2)
            // let components_cell = row.insertCell(3)
            // let duration_cell = row.insertCell(4)
            // let range_cell = row.insertCell(5)
            // let desc_cell = row.insertCell(6)
            // desc_cell.classList.add("desc")

            // insert the data into the new row
            name_cell.innerText = spell_info["name"]
            prepared_spells.add(spell_info["name"])
            if (spell_info["level"] == 0) {
                level_cell.innerText = "Cantrip"
            } else {
                level_cell.innerText = spell_info["level"]
            }
            if (spell_info["higher_level"].length > 0) {
                level_cell.innerText += "+"
            }
            // add the button to remove the spell from the spellbook
            var btn = document.createElement('input')
            btn.type = "button"
            btn.value = "Remove"
            btn.setAttribute('onclick', 'javascript: remove_spell(' + spellbook_id + ', "' + spell_list[spelll] + '");');
            remove_cell.appendChild(btn)
            // components_cell.innerText = spell_info["components"].join(", ")
            // if(components_cell.innerText.includes('M')){
            //     components_cell.innerText += " (" + spell_info["material"].replace('.', '') + ")" 
            // }
            // duration_cell.innerText = spell_info["duration"]
            // range_cell.innerText = spell_info["range"]
            // console.log(spell_info["desc"])
            // let spell_desc = document.createElement("ul")
            // spell_desc.classList.add("desc")
            // for(line in spell_info["desc"]){
            //     let spell_desc_line = document.createElement("li")
            //     spell_desc_line.classList.add("desc")
            //     spell_desc_line.innerText = spell_info["desc"][line]
            //     spell_desc.appendChild(spell_desc_line)
            // }
            // desc_cell.appendChild(spell_desc)
        }

        // use fetch to get the spells available to add to the current spellbook 
        get_cantrips(spells_stats["_spell_casting_class"])       
        for (spell_slot_level of spell_slot_levels.values()) {
            //console.log(spell_slot_level)

            // use fetch to get the available spells at the given level
            url = "https://www.dnd5eapi.co/api/classes/" + spells_stats["_spell_casting_class"] + "/levels/" + spell_slot_level + "/spells"
            response = await fetch(url)
            available_spells = await response.json()
            //console.log(available_spells)

            let add_table = document.getElementById('available spells table')

            for (available_spell in available_spells["results"]) {
                //console.log(available_spells["results"][available_spell])
                if (prepared_spells.has(available_spells["results"][available_spell]["name"])) {
                    continue
                }

                // create new table row
                let row = add_table.insertRow(-1)
                let name_cell = row.insertCell(0)
                let level_cell = row.insertCell(1)
                let remove_cell = row.insertCell(2)

                // insert the data into the new row
                name_cell.innerText = available_spells["results"][available_spell]["name"]
                if (spell_slot_level == 0) {
                    level_cell.innerText = "Cantrip"
                } else {
                    level_cell.innerText = spell_slot_level
                }
                // if (spell_info["higher_level"].length > 0) {
                //     level_cell.innerText += "+"
                // }
                // add the button to remove the spell from the spellbook
                var btn = document.createElement('input')
                btn.type = "button"
                btn.value = "Add"
                btn.setAttribute('onclick', 'javascript: add_spell(' + spellbook_id + ', "' + available_spells["results"][available_spell]["index"] + '");');
                remove_cell.appendChild(btn)
            }
        }
    }
}

async function get_cantrips(class_name){
    let add_table = document.getElementById('available spells table')

    // use fetch to get all the spells available for the class
    let url = "https://www.dnd5eapi.co/api/classes/" + class_name + "/spells"
    let response = await fetch(url)
    all_spells = await response.json()

    let cantrips = new Set()

    for(cantrip in all_spells["results"]){
        cantrips.add(all_spells["results"][cantrip]["name"])
    }

    for(i = 1; i < 10; i++){
        // use fetch to get all the non-cantrip spells available for the class
        url = "https://www.dnd5eapi.co/api/classes/" + class_name + "/levels/" + i + "/spells"
        response = await fetch(url)
        non_cantrips = await response.json()

        for(spell in non_cantrips["results"]){
            cantrips.delete(non_cantrips["results"][spell]["name"])
        }
    }

    for (cantrip of cantrips.values()) {
        //console.log(available_spells["results"][available_spell])
        if (prepared_spells.has(cantrip)) {
            continue
        }

        // create new table row
        let row = add_table.insertRow(0)
        let name_cell = row.insertCell(0)
        let level_cell = row.insertCell(1)
        let remove_cell = row.insertCell(2)

        // insert the data into the new row
        name_cell.innerText = cantrip
        level_cell.innerText = "Cantrip"
        
        // add the button to remove the spell from the spellbook
        var btn = document.createElement('input')
        btn.type = "button"
        btn.value = "Add"
        btn.setAttribute('onclick', 'javascript: add_spell(' + spellbook_id + ', "' + cantrip.replaceAll(' ', '-').toLowerCase() + '");');
        remove_cell.appendChild(btn)
    }
}

function remove_spell(spellbook_id, spell_index) {
    const request = new XMLHttpRequest();
    request.open("DELETE", "http://localhost:5000/spellbooks/" + spellbook_id + "/" + spell_index);
    request.send(null);

    location.reload()
}

function add_spell(spellbook_id, spell_index) {
    const request = new XMLHttpRequest();
    request.open("POST", "http://localhost:5000/spellbooks/" + spellbook_id + "/" + spell_index);
    request.send(null);

    location.reload()
}