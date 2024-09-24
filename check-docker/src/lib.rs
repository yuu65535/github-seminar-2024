use bollard::Docker;

// bollardを使って、Dockerの接続が可能かをチェックする
// チェックにはDockerのバージョン取得を試み、サーバー側の情報が得られればOk()とする。
pub async fn check_docker() -> Result<(), Box<dyn std::error::Error>> {
    let docker = Docker::connect_with_local_defaults()?;
    let version = docker.version().await?;
    println!("Docker Engine version: {:?}",
        version.components.unwrap()[0].version);
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn test_check_docker() {
        check_docker().await.unwrap();
    }
}
