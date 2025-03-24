// Program to check if any person is 18 or older

const people = [
    { name: "John", age: 25 },
    { name: "Jane", age: 30 },
    { name: "Bob", age: 20 },
    { name: "Alice", age: 22 },
]

people.some((person) => {
    return person.age > 18;
})