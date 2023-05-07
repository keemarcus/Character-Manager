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

        // use fetch to get the spells in the current spellbook
        let url = "http://localhost:5000/spellbooks/spells/" + spellbook_id
        let response = await fetch(url)
        spells = await response.text()
        const spell_list = spells.split(",")
        let table = document.getElementById('spell table')
        for (spelll in spell_list){
            // get the full spell info
            let url = "https://www.dnd5eapi.co/api/spells/" + spell_list[spelll]
            let response = await fetch(url)
            spell_info = await response.json()
            console.log(spell_info)

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
            cast_cell.innerText = null
            level_cell.innerText = spell_info["level"]
            if(spell_info["higher_level"].length > 0){
                level_cell.innerText += "+"
            }
            components_cell.innerText = spell_info["components"].join(", ")
            duration_cell.innerText = spell_info["duration"]
            range_cell.innerText = spell_info["range"]
            desc_cell.innerText = spell_info["desc"].join('\n')
        }
    }
}

