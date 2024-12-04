use std::fs::{create_dir_all, File};
use std::io::{Read, Write};
use std::iter::Iterator;
use std::path::Path;
use reqwest::StatusCode;


pub fn get_input(year: u16, day: u16) -> String {
    let cache_folder_binding = Path::new(file!()).canonicalize().unwrap()
        .ancestors().nth(3).unwrap()
        .join("aoc/cache");
    let year_path = cache_folder_binding.join(year.to_string());
    let cookie_path = cache_folder_binding.join("cookie.txt");
    let file_path = cache_folder_binding.join(format!("{year}/day{day}.txt"));
    println!("{}", file_path.as_path().display());

    match create_dir_all(year_path.as_path()) {
        Ok(_) => {}
        Err(_) => {panic!("Unable to create cache folder for year.")}
    }

    if file_path.as_path().exists() {
        let mut file = File::open(file_path.as_path()).unwrap();
        let mut text = String::new();
        file.read_to_string(&mut text).unwrap();
        return text;
    }

    let mut file = match File::open(cookie_path.as_path()) {
        Ok(file) => file,
        Err(_) => panic!("Need a cookie.txt file in your cache folder.")
    };
    let mut cookie = String::new();
    file.read_to_string(&mut cookie).unwrap();

    let client = reqwest::blocking::Client::new();

    let req = client.get(format!("https://adventofcode.com/{year}/day/{day}/input")).header("Cookie", cookie);
    let res = req.send().unwrap();
    if res.status() >= StatusCode::BAD_REQUEST {
        panic!("Unable to get puzzle input.")
    }
    let input = res.text().unwrap();

    let mut file = File::create(file_path.as_path()).unwrap();
    file.write_all(input.as_bytes()).unwrap();
    return input;
}

