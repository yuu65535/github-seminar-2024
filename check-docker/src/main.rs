use check_docker::check_docker;

#[tokio::main]
async fn main() {
    let result = check_docker().await;
    match result {
        Ok(()) => println!("Docker is running"),
        Err(e) => eprintln!("Error: {}", e),
    }
}
