fn main() {
    // i32 is integer
    println!("Declaring variables");
    let x = 4;
    println!("x is : {}", x);
    println!("----------------------");
    // mut lets the variable be changeable
    println!("Mutable sample");
    let mut y = 4;
    println!("y is: {}", y);
    y = 5;
    println!("y is: {}", y);
    println!("----------------------");

    println!("Interior and Exterior sample");
    let z = 4;
    println!("z is: {}", z);

    {
        let z = z - 2;
        println!("z is: {}", z);
    }

    let z = z + 5;
    println!("z is: {}", z);
}
