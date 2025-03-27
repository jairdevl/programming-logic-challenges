function buildWall(words) {
    //1. Validate input
    if(!words) {
        return "Error: The input not is empty"
    }
    if (words.includes(" ")) {
        return "Error: The input contains spaces"
    }
    if (words.length < 3) {
        return "Error: The input must have at least 3 characters"
    }

    //2. Creating the matrix
    const n = words.length
    const matrix = Array(n).fill(null).map(() => Array(n).fill(null));

    //3. Filling the matrix
    const zone1words = "abcdfghijklm"
    const zone2words = "nopqrstuvwxyz"
    let zone1index = 0
    let zone2index = 0

    for (let i = 0; i < n; i ++) {
        for (let j = 0; j < n; j ++) {
            if (i === j) {
                matrix[i][j] = words[i] // Wall
            } else if (i<j) {
                matrix[i][j] = zone1words[zone1index]
                zone1index = (zone1index + 1) % zone1words.length
            } else {
                matrix[i][j] = zone2words[zone2index]
                zone2index = (zone2index + 1) % zone2words.length
            }
        }
    }

    // 4. Generation of the generales
    const generalesZone1 = selecionarGenerales(zone1words, 3)
    const generalesZone2 = selecionarGenerales(zone2words, 3)

    // 5. Exit
    return {
        matrix: matrix,
        generalesZone1: generalesZone1,
        generalesZone2: generalesZone2
    };

    function selecionarGenerales(words, count) {
        const generales = [];
        for (let i = 0; i < count; i++) {
            const indiceAleatorio = Math.floor(Math.random() * words.length)
            generales.push(words[indiceAleatorio]);
        }
        return generales
    }
}

// 6. Example de oso
const palabra = "oso"
const resultado = buildWall(palabra)
console.log(resultado)