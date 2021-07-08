async function f1() {
    const a = await f2(3)
    console.log(a)

    const b = await f2(2)
    console.log(b)

    const c = await f2(1)
    console.log(c)
}

function f2(n) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(n)
        }, 1000)
    })
}

f1()
