// Primitive data types
// int, float, bool, char

//Integer
//Rust has (+ and -) and unsigned
//integer (only+) types of different sizes.
// i8, i16, i32, i64, i128: Signed Integers
// u8, u16, u32, u64, u128: Unsigned integers.
//

fn main() {
    let x: i32 = -42; //Can be negative values
    let y: u64 = 100; // Only positive value
    println!("Signed Integer: {}", x);
    println!("Unsigned Integer: {}", y);
    // diff bet i32 (32 bits) and i64(64 bits)
    // range :
    // i32 - 2147483647
    // i64 - 922337203854775807
    let e: i32 = 2147483647;
    println!("i32 Max value is: {}", e);
    let i: i64 = 922337203854775807;
    println!(r#"i64 Max value is: {}"#, i);
    // =========================================
    // Floats [Floating Point types]
    // f32, f64
    let pi: f64 = 3.14;
    println!("Value of pi: {}", pi);
    // =========================================
    // Boolean Values: true or false
    let is_raining: bool = true;
    println!("Is it raining ?: {}", is_raining);
    // =========================================
    // Character Type - char
    let letter: char = 'a'; // Char must be encased in ''
    println!("First Letter of the alphabet is: {}", letter);
}
