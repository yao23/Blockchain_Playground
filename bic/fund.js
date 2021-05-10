process.stdin.resume();
process.stdin.setEncoding('utf8');
// Your code here!

console.log("XXXXXXXX")

console.log("Hello, World!");

const seedAmount = 300 // 300K, unit: grand
let angelAmount = 1000 // 1M
let aAmount = 20000 // 20M 
let seedEvaluation = 3000 // 3M
let angelEvaluation = 10000 // 10M
let aEvaluation = 100000 // 100M
let sR = 0.0
let angelR = 0.0
let aR = 0.0

const seedRatio = () => {
    sR = (seedAmount / seedEvaluation)* 100
    
    console.log(`------- Seed round: -------`)
    console.log(`Seed round investors Ratio: ${ sR }%`)
    console.log(`Total Ratio: ${ sR }%`)
    console.log(`------- Seed round: -------`)
    return sR
}

const angelRatio = () => {
    angelR = (angelAmount / angelEvaluation)* 100
    const newSR = (100 - angelR) * sR / 100
    
    console.log(`------- Angel round: -------`)
    console.log(`Angel round investors Ratio: ${ angelR }%`)
    console.log(`Seed investors Ratio: ${ newSR }%`)
    console.log(`Total Ratio: ${ newSR + angelR }%`)
    console.log(`------- Angel round: -------`)
    return angelR
}

const aRatio = () => {
    sR = seedRatio()
    angelR = angelRatio()
    aR = (aAmount / aEvaluation)* 100
    const newSR = (100 - aR) * (100 - angelR) / 100 * sR / 100
    const newAngelR = (100 - aR) * angelR / 100
    
    console.log(`------- A round Ratio: -------`)
    console.log(`A round investors Ratio: ${ aR }%`)
    console.log(`Angel investors Ratio: ${ newAngelR  }%`)
    console.log(`Seed investors Ratio: ${ newSR }%`)
    console.log(`Total Ratio: ${ newSR + newAngelR + aR }%`)
    console.log(`------- A round Ratio: -------`)
}

const getAAmount = () => {
    sR = seedRatio()
    angelR = angelRatio()
    const angelSR = (100 - angelR) * sR / 100
    const totalRatio = 30 // round A with funding 13.5M for 30% totally, total 35% to expect with 20M
    
    // aR + (1 - aR) * angelR + (1 - aR) * angelSR = totalRatio
    // aR * (100 - angelR - angelSR) = totalRatio - (angelR + angelSR)
    const aR = (totalRatio - (angelR + angelSR)) / (100 - angelR - angelSR) * 100
    const aAmount = aR / 100 * aEvaluation
    
    const newSR = (100 - aR) * (100 - angelR) / 100 * sR / 100
    const newAngelR = (100 - aR) * angelR / 100
    
    console.log(`------- A round Ratio: -------`)
    console.log(`A round investors Ratio: ${ aR }%`)
    console.log(`A round investors amount: ${ aAmount}%`)
    console.log(`Angel investors Ratio: ${ newAngelR  }%`)
    console.log(`Seed investors Ratio: ${ newSR }%`)
    console.log(`Total Ratio: ${ newSR + newAngelR + aR }%`)
    console.log(`------- A round Ratio: -------`)
}

// aRatio()

getAAmount()
