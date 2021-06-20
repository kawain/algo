export {};

interface Theme {
  getColor(): string;
}

class DarkTheme implements Theme {
  getColor(): string {
    return "Dark Black";
  }
}
class LightTheme implements Theme {
  getColor(): string {
    return "Off white";
  }
}
class AquaTheme implements Theme {
  getColor(): string {
    return "Light blue";
  }
}

interface WebPage {
  getContent(): string;
}

class About implements WebPage {
  constructor(private theme: Theme) {}
  getContent(): string {
    return this.theme.getColor() + "のAboutページ";
  }
}

class Careers implements WebPage {
  constructor(private theme: Theme) {}
  getContent(): string {
    return this.theme.getColor() + "のCareersページ";
  }
}

const darkTheme = new DarkTheme();
let about = new About(darkTheme);
let careers = new Careers(darkTheme);

console.log(about.getContent());
console.log(careers.getContent());

const lightTheme = new LightTheme();
about = new About(lightTheme);
careers = new Careers(lightTheme);

console.log(about.getContent());
console.log(careers.getContent());

const aquaTheme = new AquaTheme();
about = new About(aquaTheme);
careers = new Careers(aquaTheme);

console.log(about.getContent());
console.log(careers.getContent());
