use reqwest::blocking::get;

pub fn getcont(user: &str, day: &str, returnformalday: bool) -> Result<i32, reqwest::Error> {
    let url = format!("https://github.com/{}", user);
    let page = get(&url)?.text()?;
    
    // Removes everything in the HTML file thats not needed
    let mut page = page
        .split("js-calendar-graph-svg")
        .nth(1)
        .unwrap()
        .split("</g>  </svg>")
        .next()
        .unwrap()
        .split('\n');

    for ln in page {
        if !ln.contains(day) {
            continue;
        }

        let cont = ln[ln.find("\">").unwrap() + 2..ln.find("contribution").unwrap()]
            .parse::<i32>()
            .unwrap_or(0);

        if !returnformalday {
            return Ok(cont);
        } else {
            let formalday = ln[ln.find("contribution").unwrap() + 16..ln.find("</rect>").unwrap()];
            return Ok((cont, formalday.to_owned()));
        }
    }
    Ok(0)
}

fn main(){
    println!("{:?}", getcont("An013r", "03-10", false));
}